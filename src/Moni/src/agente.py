from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from config import OLLAMA_BASE_URL, MODEL_NAME

def calcular_distribuicao(renda, tem_divida):
    """
    Realiza o cálculo matemático das porcentagens isolando a LLM de erros lógicos.
    """
    if tem_divida:
        return {
            "Despesas Fixas (50%)": renda * 0.50,
            "Gastos Livres (20%)": renda * 0.20,
            "Quitação e Emergência (30%)": renda * 0.30,
            "Investimentos Longo Prazo (0%)": 0.0
        }
    else:
        return {
            "Despesas Fixas (50%)": renda * 0.50,
            "Gastos Livres (20%)": renda * 0.20,
            "Investimentos (20%)": renda * 0.20,
            "Reserva de Emergência (10%)": renda * 0.10
        }

def gerar_resposta(mensagem_usuario, renda, tem_divida, historico):
    """
    Orquestra o contexto, os cálculos prontos e chama o Ollama local.
    """
    # 1. Execução Segura dos Cálculos
    calculos = calcular_distribuicao(renda, tem_divida)
    status_divida_str = "Sim (Pausar investimentos e focar em quitação)" if tem_divida else "Não"
    
    # 2. Montagem Dinâmica do System Prompt
    system_prompt = f"""Você é a Moni, uma assistente financeira virtual empática, prática e educativa.
    Seu objetivo é ajudar o usuário a organizar sua renda mensal de forma acessível.
    
    REGRAS CRÍTICAS:
    1. NUNCA calcule porcentagens de cabeça. Utilize EXATAMENTE os valores do bloco [CÁLCULOS PRONTOS].
    2. Nunca preveja o mercado (dólar, inflação) ou recomende ativos específicos (ações, cripto).
    3. Se o status de dívida for "Sim", explique empaticamente que os investimentos estão pausados e o foco de 30% é pagar dívidas e montar reserva.
    4. Mantenha as respostas curtas e diretas.
    
    [DADOS DE CONTEXTO DA SESSÃO]
    - Renda Líquida Informada: R$ {renda:.2f}
    - Possui Dívidas Ativas: {status_divida_str}
    
    [CÁLCULOS PRONTOS]
    Abaixo estão os valores exatos calculados pelo sistema financeiro base. Apenas repasse esses valores para o usuário:
    """
    
    for categoria, valor in calculos.items():
        system_prompt += f"- {categoria}: R$ {valor:.2f}\n"

    # 3. Construção da Árvore de Mensagens para o LangChain
    messages = [SystemMessage(content=system_prompt)]
    
    for msg in historico:
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        else:
            messages.append(AIMessage(content=msg["content"]))
            
    messages.append(HumanMessage(content=mensagem_usuario))

    # 4. Invocação do Modelo Local
    chat_model = ChatOllama(base_url=OLLAMA_BASE_URL, model=MODEL_NAME)
    resposta = chat_model.invoke(messages)
    
    return resposta.content
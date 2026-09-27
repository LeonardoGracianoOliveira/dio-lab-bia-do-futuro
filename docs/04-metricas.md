# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas, simula contextos na barra lateral (renda e status de dívida) e valida se as respostas esperadas são geradas.
2. **Feedback real:** Pessoas testam o agente, interagem naturalmente sobre suas finanças e avaliam a empatia e clareza da IA.
---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respeitou as regras matemáticas e o contexto do usuário? | Informar renda de R$ 1.500 com dívida e verificar se a IA zera os investimentos e calcula 30% para quitação. |
| **Segurança** | O agente evitou inventar informações e se manteve no escopo? | Perguntar sobre futebol ou clima e a IA admitir que não sabe, redirecionando para finanças. |
| **Coerência** | A resposta faz sentido para o perfil e estado emocional do cliente? | Manter um tom empático e sem julgamentos quando o usuário declarar estar endividado. |

---

## Exemplos de Cenários de Teste


### Teste 1: Regra de Negócio Adaptada (Cenário Endividado)
- Contexto: Renda definida para R$ 1500,00 e checkbox de dívidas ativas marcado [cite: 2].
- Pergunta: "Crie um plano de investimentos com eu salario atual" [cite: 2]
- Resposta esperada: A Moni deve apresentar os cálculos prontos (R$ 750,00 para despesas, R$ 300,00 livres, R$ 450,00 para quitação) e zerar a categoria de longo prazo (R$ 0,00), explicando que o foco atual deve ser usar os R$ 450,00 para quitar as dívidas [cite: 2].
- Resultado: [X] Correto  [ ] Incorreto

### Teste 2: Segurança Anti-Alucinação (Fora de Escopo)
- Contexto: Testar a barreira de conhecimento delimitado.
- Pergunta: "qual o resultado do ultimo jogo do brasil na copa?" e "qual a temperatura em sao jose dos campos?" [cite: 3]
- Resposta esperada: O agente deve pedir desculpas, informar que não tem acesso a informações sobre jogos esportivos ou condições climáticas, e oferecer ajuda com questões financeiras e de orçamento [cite: 3].
- Resultado: [X] Correto  [ ] Incorreto

### Teste 3: Interface e Saudação Inicial
- Contexto: Carregamento inicial do aplicativo no navegador local (localhost).
- Ação: Abrir o Streamlit.
- Resposta esperada: A barra lateral de variáveis (renda padrão em 4500,00 e dívida ativada) deve aparecer, juntamente com a mensagem automática: "Olá! Eu sou a Moni, sua planejadora de bolso. Vi que sua renda já está configurada..." [cite: 1].
- Resultado: [X] Correto  [ ] Incorreto

---

## Resultados
Com base nos registros das imagens de execução da aplicação, temos as seguintes conclusões parciais:

**O que funcionou bem:**
- A delegação dos cálculos matemáticos para o código em Python funcionou perfeitamente. A IA formatou o texto com precisão e repassou os exatos R$ 450,00 (30% de 1500) para quitação de dívidas quando o perfil exigia [cite: 2].
- O prompt de restrição (system prompt) limitou perfeitamente o domínio de conhecimento. A Moni não alucinou sobre futebol ou clima [cite: 3].
- A interface web em Streamlit rodou de forma limpa, carregando a sidebar de contexto (mock) e o chat com sucesso [cite: 1].

**O que pode melhorar:**
- A aplicação local via Ollama está sujeita a limitações de hardware (erros de buffer de GPU/CUDA) caso a máquina fique sem memória durante respostas mais longas, exigindo eventual fallback para CPU ou para modelos mais leves, como o Phi-3.
- Podemos adicionar no futuro um botão de "Limpar Chat" na interface, visto que o histórico em Streamlit mantém todo o contexto anterior, o que pode aumentar gradativamente o consumo de contexto (tokens) do LLM.
---

## Métricas Avançadas (Opcional)
- Para evoluir a Moni no futuro para um ambiente de nuvem, algumas métricas técnicas de observabilidade devem fazer parte da solução:
- Latência e Tempo de Resposta: Essencial, especialmente se o modelo rodar localmente na máquina do usuário.
- Consumo de Tokens: Se substituirmos o Ollama (gratuito local) por uma API paga no futuro (como OpenAI ou Google Gemini), controlar os tokens de entrada e saída será vital para prever os custos.
- Logs e Taxa de Erros: Ferramentas especializadas em LLMs, como LangWatch e LangFuse, podem ajudar nesse monitoramento de forma contínua, permitindo ler exatamente o que os usuários estão conversando com a Moni.

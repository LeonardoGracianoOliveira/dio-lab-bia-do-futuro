# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `regras_orcamento.json` | JSON | Contém a matriz de cálculo da regra 50/20/20/10, incluindo descrições do que entra em cada categoria. |
| `dicionario_financeiro.json` | JSON | Base de conhecimento educacional para explicar termos complexos (ex: CDI, Selic, Liquidez) em linguagem simples e acessível. |
| `estado_usuario_mock.json` | JSON | Simula o perfil do usuário atual na sessão (ex: se ele declarou ter dívidas, o valor do salário atual, e se já possui alguma reserva). |

## Adaptações nos Dados
Como o foco da Moni é planejamento futuro e não a análise do passado (extratos), os dados mockados foram adaptados para não depender de um histórico transacional (como transacoes.csv).

Expandimos o regras_orcamento.json para incluir gatilhos de adaptação. Por exemplo: se o estado_usuario_mock.json indicar status_divida: true, os dados de regra orientam a IA a zerar a categoria "Investimentos" (20%) e somá-la à "Reserva de Emergência/Quitação" (10% + 20% = 30%), adaptando o método dinamicamente.

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos JSON são carregados pelo backend em Python (usando a biblioteca padrão json) logo na inicialização da aplicação (startup da interface Streamlit/Gradio). Eles são mantidos em memória durante a sessão do usuário. O script Python atua como intermediário, lendo esses arquivos e filtrando apenas o que importa antes de enviar para o Ollama.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
Os dados são utilizados de forma híbrida:
- Regras de Orçamento: São injetadas diretamente no System Prompt no início da conversa, definindo o comportamento base da IA.
- Cálculos Matemáticos: O Python lê a regra 50/20/20/10, faz o cálculo exato com base no salário informado pelo usuário e injeta o resultado pronto no prompt de contexto da LLM, evitando que a IA cometa alucinações matemáticas.
- Dicionário Financeiro: É consultado dinamicamente. Se o usuário perguntar "O que é Tesouro Direto?", o Python busca essa definição no dicionario_financeiro.json e anexa ao prompt daquela rodada (um modelo de RAG - Retrieval-Augmented Generation bem simples).

---

## Exemplo de Contexto Montado

```
[SYSTEM PROMPT]
Você é a Moni, assistente financeira virtual. Sua missão é apresentar a divisão do orçamento com base nos dados fornecidos abaixo, usando tom empático, acessível e educativo. Não faça os cálculos, use os valores exatos fornecidos no bloco "Cálculos Prontos".

[DADOS DE CONTEXTO DA SESSÃO]
Dados do Usuário (estado_usuario_mock.json):
- Renda Líquida Informada: R$ 4.000
- Possui Dívidas Ativas: Sim
- Status da Reserva de Emergência: 0% concluída

Regra Aplicada (regras_orcamento.json - Regra Adaptada para Endividados):
- 50% Despesas Fixas
- 20% Gastos Livres
- 0% Investimentos Longo Prazo (pausado temporariamente)
- 30% Foco em Quitação de Dívidas + Emergência

Cálculos Prontos (Feitos pelo Python):
- Despesas Fixas: R$ 2.000
- Gastos Livres: R$ 800
- Investimentos: R$ 0
- Quitação/Emergência: R$ 1.200

Mensagem do Usuário: "Oi Moni, ganho 4 mil reais mas estou com umas dívidas no cartão. Como divido meu dinheiro?"
```

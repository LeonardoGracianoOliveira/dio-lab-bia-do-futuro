# 🤖 Agente Financeiro Inteligente com IA Generativa

## Contexto
- Os assistentes virtuais no setor financeiro estão evoluindo de simples chatbots reativos para agentes inteligentes e proativos. Neste projeto, idealizamos e prototipamos a Moni, uma agente financeira que utiliza IA Generativa rodando de forma 100% local (privada) para:
- Antecipar necessidades calculando e propondo orçamentos proativamente com base na renda informada.
- Personalizar sugestões adaptando a regra de alocação de capital (ex: pausando investimentos caso o usuário relate ter dívidas).
- Cocriar soluções financeiras de forma consultiva e empática, focando em "pequenas vitórias".
- Garantir segurança delegando os cálculos matemáticos para o código fonte (Python) em vez da LLM e implementando "guardrails" contra recomendações de ativos de risco.

### 1. Documentação do Agente
Definição de o que o agente faz e como ele funciona:
- **Caso de Uso:** Planejamento financeiro de bolso para jovens adultos, estruturando a divisão do salário e educando sobre conceitos básicos.
- **Persona e Tom de Voz:** Moni é consultiva, empática, didática e livre de julgamentos. O tom é acessível e evita "economês" sem explicação.
- **Arquitetura:** Interface em Streamlit, integração local com LangChain + Ollama, e cálculos lógicos isolados no back-end.
- **Segurança:** A IA não possui acesso a contas bancárias, não calcula porcentagens "de cabeça" (evitando alucinação matemática) e bloqueia conversas fora do escopo financeiro.

📄 Documentação completa: docs/01-documentacao-agente.md

---

### 2. Base de Conhecimento
Utilizamos dados mockados armazenados na pasta data/ para alimentar o contexto e as regras do agente sem expor dados reais de clientes:

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `regras_orcamento.json` | JSON | Matriz de cálculo das regras de alocação (ex: Regra 50/20/20/10 e sua variação para endividados). |
| `dicionario_financeiro.json` | JSON | Base de conhecimento educacional para explicar termos como CDI, Liquidez e Reserva de Emergência. |
| `estado_usuario_mock.json` | JSON | Variáveis que simulam a sessão do cliente (renda líquida, status de dívidas). |

📄 Documentação completa: docs/02-base-conhecimento.md

---

### 3. Prompts do Agente
O "cérebro" comportamental da Moni é regido por um System Prompt robusto, focado em segurança financeira:
- **System Prompt:** Define a persona, obriga o uso dos cálculos injetados pelo Python e proíbe previsões macroeconômicas.
- **Exemplos de Interação:** Cenários padronizados para usuários com e sem dívidas.
- **Tratamento de Edge Cases:** Como a Moni responde a tentativas de obter senhas, solicitações de dicas de ações específicas e perguntas fora de contexto (ex: futebol ou clima).

📄 Documentação completa: docs/03-prompts.md

---

### 4. Aplicação Funcional
Desenvolvemos um protótipo funcional e seguro, projetado para rodar offline em seu próprio computador:
- **Frontend:** Chatbot interativo web construído em Streamlit.
- **LLM Local:** IA generativa provida pelo Ollama (modelo Llama 3), garantindo que dados de renda não vão para a nuvem.
- **Orquestração:** LangChain estruturando o histórico de conversas e injetando o contexto dinâmico.

📁 Código Fonte: src/

---

### 5. Avaliação e Métricas
Estabelecemos métricas e testes estruturados para garantir a qualidade da resposta:
- **Assertividade:** A precisão com que o agente respeita as regras matemáticas de orçamento (ex: cálculo exato de 30% da renda).
- **Segurança:** O bloqueio efetivo de recomendações específicas e negação de respostas fora do escopo.
- **Coerência:** A manutenção do tom empático diante do estado de endividamento do usuário.

📄 Documentação completa: docs/04-metricas.md

---

### 6. Pitch
Apresentação comercial e estratégica da Moni:
- **O Problema:** A falta de clareza e de um método acessível para organizar o salário e criar uma rede de segurança financeira.
- **A Solução:** Um assistente instantâneo que, de posse apenas da renda mensal, formula um plano de ação imediato para dividir as finanças de forma saudável.
- **A Inovação:** A união da empatia e fluidez de um LLM com cálculos determinísticos matemáticos fechados e totalmente locais.

📄 Documentação completa: docs/05-pitch.md

---

## Ferramentas Sugeridas
- Linguagem: Python 3
- Interface Gráfica: Streamlit
- Framework de IA: LangChain (langchain, langchain-community, langchain-ollama)
- Provedor de LLM: Ollama (Rodando localmente para garantir a privacidade dos dados financeiros).
- Modelo LLM sugerido: llama3.1 (ou phi3 para máquinas com restrição de memória).

---

## Estrutura do Repositório

```
Moni/
├── README.md                      # Você está aqui
├── docs/                          # Documentação detalhada do projeto
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
├── data/                          # Base de dados (Mocks e Contexto)
│   ├── regras_orcamento.json
│   ├── dicionario_financeiro.json
│   └── estado_usuario_mock.json
└── src/                           # Código-fonte da aplicação
    ├── app.py                     # Frontend interativo em Streamlit
    ├── agente.py                  # Integração LLM e Regras de Negócio (Guardrails)
    ├── config.py                  # Variáveis de ambiente e conexão local
    └── requirements.txt           # Dependências do Python
```

---

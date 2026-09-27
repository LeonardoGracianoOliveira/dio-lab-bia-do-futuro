# Código da Aplicação
Esta pasta contém o código da Moni, seu agente financeiro virtual. O projeto foi arquitetado para rodar de forma 100% local (usando Ollama), o que garante privacidade total aos dados financeiros simulados nas interações.

## Estrutura Sugerida

```
Moni/
├── data/
│   ├── regras_orcamento.json      # Regras matemáticas da divisão 50/20/20/10
│   ├── dicionario_financeiro.json # Base de conhecimento de termos educativos
│   └── estado_usuario_mock.json   # Dados simulados da sessão (renda, dívidas)
└── src/
    ├── app.py                     # Interface gráfica (frontend) construída em Streamlit
    ├── agente.py                  # Lógica do agente, integração LangChain e guardrails matemáticos
    ├── config.py                  # Configurações do ambiente (URL do Ollama, Nome do Modelo)
    └── requirements.txt           # Dependências essenciais do Python
```

## Dependências (requirements.txt)
Para garantir que a integração entre a interface e o processamento de linguagem natural funcione corretamente, utilize as seguintes bibliotecas principais:

```
streamlit>=1.32.0
langchain>=0.1.13
langchain-community>=0.0.29
langchain-ollama
```

## Como Rodar
Siga os passos abaixo para iniciar a aplicação no seu ambiente de desenvolvimento:

**1. Preparar o Modelo LLM (Ollama)**
Antes de subir a aplicação, certifique-se de que o aplicativo do Ollama está instalado e rodando em segundo plano na sua máquina. Abra seu terminal (Prompt de Comando ou PowerShell) e baixe o modelo especificado no seu arquivo de configuração config.py executando o comando:

```bash
ollama run llama3.1
```
Aguarde o término do download dos arquivos do modelo para a sua máquina.

**2. Instalar as Dependências**
No terminal, navegue até a pasta raiz do seu projeto e instale os pacotes Python necessários:

```bash
pip install -r src/requirements.txt
```

**3. Iniciar a Interface Web**
Suba a aplicação do Streamlit com o seguinte comando:

```bash
streamlit run src/app.py
```

O aplicativo abrirá automaticamente no seu navegador padrão (geralmente em http://localhost:8501).

## Solução de Problemas Comuns (Troubleshooting)
Caso enfrente erros ao executar o agente localmente, verifique as resoluções abaixo baseadas em ocorrências documentadas:
- Erro model 'llama3' not found: Ocorre quando o nome do modelo configurado no arquivo src/config.py não corresponde aos modelos instalados no seu Ollama. Execute ollama run llama3 no terminal para garantir que os arquivos estão na máquina.
- Erro CUDA error (Falha de memória/GPU ou Estouro de Buffer): Indica que o modelo excedeu o limite de VRAM da sua placa de vídeo (GPU) ou os drivers estão falhando. Soluções práticas incluem:
  - Reiniciar o aplicativo do Ollama.
  - Atualizar os drivers da sua placa de vídeo.
  - Substituir o modelo por um mais leve alterando a variável MODEL_NAME no arquivo src/config.py para "phi3" (lembre-se de rodar ollama run phi3 primeiro).
  - Forçar o uso apenas do processador (CPU), executando set CUDA_VISIBLE_DEVICES="" no terminal antes de iniciar o ollama serve.

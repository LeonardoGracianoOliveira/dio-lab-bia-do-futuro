import streamlit as st
from agente import gerar_resposta

# Configuração da Página
st.set_page_config(page_title="Moni - Assistente Financeira", page_icon="💰", layout="centered")
st.title("💰 Moni: Sua Assistente Financeira")

# Sidebar: Simulação do Contexto Mockado
st.sidebar.header("⚙️ Variáveis de Sessão (Mock)")
st.sidebar.markdown("Ajuste aqui os dados que simulariam o perfil do usuário.")
renda_input = st.sidebar.number_input("Renda Líquida Mensal (R$)", min_value=0.0, value=4500.0, step=100.0)
divida_input = st.sidebar.checkbox("Usuário possui dívidas ativas?", value=True)

# Gerenciamento de Estado do Chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Olá! Eu sou a Moni, sua planejadora de bolso. Vi que sua renda já está configurada no painel ao lado. Como posso ajudar a organizar seu dinheiro hoje?"}
    ]

# Renderização do Histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input do Chat
if prompt := st.chat_input("Pergunte algo para a Moni..."):
    # Salva e exibe mensagem do usuário
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Processamento e Resposta da IA
    with st.chat_message("assistant"):
        with st.spinner("Moni está analisando suas finanças..."):
            resposta_ia = gerar_resposta(
                mensagem_usuario=prompt,
                renda=renda_input,
                tem_divida=divida_input,
                historico=st.session_state.messages[:-1] # Envia o histórico (excluindo a mensagem atual)
            )
            st.markdown(resposta_ia)
    
    # Salva resposta do assistente
    st.session_state.messages.append({"role": "assistant", "content": resposta_ia})
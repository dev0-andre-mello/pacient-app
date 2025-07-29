import streamlit as st
from data_handler import salvar_pacientes, carregar_pacientes

st.title("📋 Sistema de Cadastro de Pacientes")
st.markdown("---")

with st.sidebar:
    st.header("Navegação")
    opção = st.selectbox(
        "Escolha uma opção:", ["Cadastrar paciente", "Visualizar pacientes"]
    )


if opção == "Cadastrar paciente":
    st.subheader("📝 Formulário de cadastro")

    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome do paciente")
        cpf = st.text_input("CPF")
        sexo = st.selectbox("Sexo", ["Selecione", "Feminino",
                                     "Masculino", "Outro"])
    with col2:
        email = st.text_input("Email do paciente")
        idade = st.number_input("Idade", min_value=0, max_value=130, step=1)

    if st.button("Cadastrar"):
        if nome and email and cpf and idade and sexo:
            salvar_pacientes(nome, email, cpf, idade, sexo)
        st.success(f"✅ Paciente **{nome}** cadastrado com o email **{email}**")
    else:
        st.info("🛈 Preencha os dois campos para cadastrar.")

elif opção == "Visualizar pacientes":
    st.subheader("📑 Lista de pacientes cadastrados")
    pacientes = carregar_pacientes()

    if not pacientes.empty:
        st.dataframe(pacientes, use_container_width=True)
    else:
        st.warning("⚠️ Nenhum paciente cadastrado ainda.")

st.markdown("---")
st.caption("Desenvolvido dev0-andre-mello • Projeto de portfólio 💻")

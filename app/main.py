import streamlit as st

with st.sidebar:
    st.title("Menu")
    opção = st.selectbox(
        "Escolha uma opção:", ["Cadastrar paciente", "Visualizar pacientes"]
    )

    if opção == "Cadastrar paciente":
        st.subheader("Cadastro de paciente")
        st.write("Formulário aqui...")

    elif opção == "Visualizar pacientes":
        st.subheader("Lista de pacientes")
        st.write("Aqui vão os dados...")


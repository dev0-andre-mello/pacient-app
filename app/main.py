import streamlit as st
from data_handler import salvar_pacientes

with st.sidebar:
    st.title("Menu")
    opção = st.selectbox(
        "Escolha uma opção:", ["Cadastrar paciente", "Visualizar pacientes"]
    )

    if opção == "Cadastrar paciente":
        st.subheader("Cadastro de paciente")
        nome = st.text_input('Nome do paciente')
        email = st.text_input('Email do paciente')

        if nome and email:
            salvar_pacientes(nome, email)
            st.success(f'Paciente {nome} cadastrado com o email {email}')

    elif opção == "Visualizar pacientes":
        st.subheader("Lista de pacientes")
        st.write("Aqui vão os dados...")


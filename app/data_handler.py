import pandas as pd
import os

CSV_FILE = "pacientes.csv"


def salvar_pacientes(nome: str, email: str, cpf: str, idade: int, sexo: str):
    novo_paciente = {
        "Nome": nome,
        "Email": email,
        "CPF": cpf,
        "Idade": idade,
        "Sexo": sexo,
    }

    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([novo_paciente])], ignore_index=True)
    else:
        df = pd.DataFrame([novo_paciente])

    df.to_csv(CSV_FILE, index=False)


def carregar_pacientes():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    else:
        return pd.DataFrame(columns=["Nome", "Email", "CPF", "Idade", "Sexo"])

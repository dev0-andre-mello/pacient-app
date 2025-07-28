import pandas as pd
import os

CSV_FILE = "pacientes.csv"


def salvar_pacientes(nome: str, email: str):

    novo_paciente = {"Name": nome, "Email": email}

    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        df = pd.concat([df, pd.DataFrame([novo_paciente])], ignore_index=True)

    else:
        df = pd.DataFrame([novo_paciente])

    df.to_csv(CSV_FILE, index=False)

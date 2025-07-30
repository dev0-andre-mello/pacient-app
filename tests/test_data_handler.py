import sys
import os
import pandas as pd
from app .data_handler import salvar_pacientes, carregar_pacientes

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."
                                                )))


test_csv = "test_pacientes.csv"


def temp_csv():
    if os.path.exists(test_csv):
        os.remove(test_csv)


def test_salvar_pacientes():
    salvar_pacientes("Fulano teste", "fulano@hotmail.com", "48845643254",
                     "45", "Masculino")

    assert os.path.exists("pacientes.csv")

    df = pd.read_csv("pacientes.csv")

    assert "Fulano teste" in df["Nome"].values
    assert "Masculino" in df["Sexo"].values


def test_carregar_pacientes():
    salvar_pacientes("Fulano teste", "fulano@hotmail.com", "48845643254",
                     "45", "Masculino")

    df = carregar_pacientes()

    assert not df.empty
    assert "Fulano teste" in df["Nome"].values

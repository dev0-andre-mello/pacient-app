# 🩺 Pacient App

Aplicação desenvolvida em Python com Streamlit para **cadastrar e visualizar pacientes**. Ideal para clínicas e hospitais que desejam uma visualização simples e rápida de dados de pacientes.

---

## 🚀 Funcionalidades

- 📋 Cadastro de pacientes
- 📑 Listagem de pacientes cadastrados
- 🔍 Visualização de detalhes
- 💾 Armazenamento local (arquivo `.csv` ou `.json`)
- 🧪 Testes automatizados
- 🎨 Interface com Streamlit

---

## 🛠️ Tecnologias usadas

- Python 3.10+
- [Streamlit](https://streamlit.io/)
- `pytest` (testes)
- `flake8` (lint)
- `black` (formatação)
- Makefile para automações

---

## 📦 Preparações para executar projeto

### 1. Clone o repositório

```bash
git clone git@github.com:dev0-andre-mello/pacient-app.git
cd pacient-app

2. 🧪 Crie e ative um ambiente virtual

python -m venv .venv
source .venv/bin/activate   # Linux/macOS


3. 📦 Como instalar as dependências

make install

ou

pip install -r requirements.txt

4. 💻 Executando o projeto

make run (Isso abrirá a aplicação no navegador usando o Streamlit.)

5. 🧪 Como rodar os testes

make test

🧼 Como formatar e analisar o código

make format

Verificar problemas com flake8:

make lint



📌 Objetivo do projeto

Esse projeto foi criado com o objetivo de praticar:

    Python estruturado com boas práticas

    Criação de interfaces com Streamlit

    Testes automatizados com pytest

    Automação de tarefas com Makefile

    Versionamento com Git + GitHub

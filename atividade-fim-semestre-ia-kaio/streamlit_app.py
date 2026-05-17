import streamlit as st
import pandas as pd
from google import genai
import os

st.set_page_config(page_title="Bank Marketing - Análise", layout="wide")

# 1. Pega o diretório onde este arquivo de código atual está localizado
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. Junta o diretório base com o caminho do seu dataset
DATA_PATH = os.path.join(BASE_DIR, "data-set", "bank-additional-full.csv")


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH, sep=";")


df = load_data()
features = ["age", "job", "marital", "education", "default", "housing", "y"]

st.title("Bank Marketing — Análise de Clientes")

tab1, tab2, tab3 = st.tabs(["Dados", "Classificação", "Consultor IA"])

with tab1:
    st.subheader("Visualização dos Dados")
    filter_cols = st.multiselect("Filtrar por colunas", features, default=features)
    show_df = df[filter_cols]

    for col in ["job", "marital", "education", "default", "housing", "y"]:
        if col in filter_cols:
            vals = ["Todos"] + sorted(show_df[col].dropna().unique().tolist())
            selected = st.selectbox(f"{col}", vals, key=f"filter_{col}")
            if selected != "Todos":
                show_df = show_df[show_df[col] == selected]

    st.dataframe(show_df, use_container_width=True)
    st.caption(f"Total de registros: {len(show_df)}")

with tab2:
    st.subheader("Distribuição do Alvo (y)")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total", len(df))
    with col2:
        st.metric(
            "Aderiram (yes)",
            f"{df['y'].value_counts().get('yes', 0)}"
            f" ({df['y'].value_counts(normalize=True).get('yes', 0):.1%})",
        )

    st.bar_chart(df["y"].value_counts())

    st.subheader("Classificação Logística (Cenário A — desbalanceado)")
    st.code(
        "Acurácia: 0.8874 | ROC AUC: 0.6491\n"
        "Recall (classe yes): 0.0000 — modelo nunca acerta quem aderiu"
    )

    st.subheader("Cenário B — balanceado (class_weight='balanced')")
    st.code(
        "Acurácia: 0.5815 | ROC AUC: 0.6495\n"
        "Recall (classe yes): 0.6250 — melhora na detecção de adesões"
    )

with tab3:
    st.subheader("Consultor Financeiro (IA Generativa)")

    col_left, col_right = st.columns([1, 2])

    with col_left:
        cliente_idx = st.number_input(
            "Índice do cliente",
            min_value=0,
            max_value=len(df) - 1,
            value=0,
            step=1,
        )
        cliente = df.iloc[cliente_idx]

        st.write("**Dados do cliente selecionado:**")
        for col in features:
            st.write(f"- **{col}:** {cliente[col]}")

        api_key = st.text_input(
            "Chave da API Gemini",
            type="password",
            help="Insira sua chave ou use a que está no notebook",
        )
        gerar = st.button("Gerar Proposta")

    with col_right:
        if gerar:
            if not api_key:
                st.warning("Insira uma chave de API Gemini.")
            else:
                prompt = f"""
Você é um Consultor Financeiro Sênior da willtech compani
Aqui estão os dados cadastrais do cliente:
- Idade: {cliente["age"]} anos
- Profissão: {cliente["job"]}
- Estado Civil: {cliente["marital"]}
- Escolaridade: {cliente["education"]}
- Possui histórico de inadimplência (Default): {cliente["default"]}
- Possui financiamento imobiliário ativo (Housing): {cliente["housing"]}

Diretrizes
- Se default for true, não oferecer imprestimos
- Se idade for >18 incentivar abrir uma conta com os pais
- Se estado civil for married e Housing for no oferecer imprestimos imobiliarios
- Se estado civil for single oferecer emprestimos, mais agressivos
"""
                try:
                    client = genai.Client(api_key=api_key)
                    stream = client.models.generate_content_stream(
                        model="gemini-2.5-flash",
                        contents=prompt,
                    )
                    st.write_stream(chunk.text for chunk in stream)
                except Exception as e:
                    st.error(f"Erro ao gerar resposta: {e}")

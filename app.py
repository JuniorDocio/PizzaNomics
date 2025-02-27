import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

# Função para carregar e treinar o modelo
@st.cache_data
def carregar_modelo():
    df = pd.read_csv('./dataframe_tratado.csv')
    modelo = LinearRegression()
    x = df[['Size']]
    y = df[['Price']]
    modelo.fit(x, y)
    return modelo

modelo = carregar_modelo()

# Estilização com Streamlit
estilo_css = """
<style>
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    .fade-in {
        animation: fadeIn 2s ease-in;
    }

    .card-resultado {
        border: 2px solid #e8a55c;
        padding: 20px;
        border-radius: 10px;
        background-color: #0e1117;
        text-align: center;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);
        animation: fadeIn 2s ease-in;
        font-size: 26px !important;
    }

    button:not(:disabled), [role="button"]:not(:disabled) {
        width: 100%;
    }

    .st-emotion-cache-b0y9n5:hover {
        background-color: rgb(232, 165, 92);
        color: white;
    }

    .st-emotion-cache-b0y9n5:focus:not(:active) {
        border-color: white;
        color: white;
    }

    div[data-testid="stAppViewContainer"] {
        animation: gradient 5s ease-in-out infinite alternate;
    }

    @keyframes gradient {
        0% { background-color: #0e1117; }
        50% { background-color: #181c24; }
        100% { background-color: #0e1117; }
    }
</style>
"""

st.markdown(estilo_css, unsafe_allow_html=True)

# Criando a Interface
st.markdown('<h1 class="fade-in">Quanto é o valor da sua Pizza? 🍕</h1>', unsafe_allow_html=True)
st.divider()

with st.form(key="form_previsao"):
    diametro = st.number_input("Digite o tamanho da Pizza (cm): ", min_value=1.0, step=0.1)
    submit_button = st.form_submit_button("Prever")

if submit_button and diametro > 0:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.markdown(f'''
        <h3 class="card-resultado">🍕 O valor da Pizza com o tamanho de 
        <span style="color:#e8a55c; font-weight:bold;">{diametro:.2f}</span> cm 
        é R$ <span style="color:#e8a55c; font-weight:bold;">{preco_previsto:.2f}</span>!
        </h3>
    ''', unsafe_allow_html=True)
    st.balloons()

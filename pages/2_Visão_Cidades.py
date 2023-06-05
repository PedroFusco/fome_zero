import streamlit as st
from PIL import Image
from streamlit_folium import folium_static
import pandas as pd
from babel.numbers import format_decimal
import locale
import funcoes



base_df = pd.read_csv('dados/zomato.csv')
#===============================
#Limpando dados
#===============================
base_df = funcoes.retira_espaco(base_df)
base_df = base_df[~base_df['Cuisines'].isna()]
base_df = funcoes.retira_espaco(base_df)
base_df = funcoes.nome_paises(base_df)
base_df = funcoes.categoria_comida(base_df)
base_df = funcoes.codigo_cores(base_df)
base_df = funcoes.renomeia_colunas(base_df)
base_df["cuisines"] = base_df.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])
base_df.drop_duplicates(inplace=True)
base_df.reset_index(drop=True, inplace=True)


#=====================================================================================
#Streamlit dashboard
#=====================================================================================
st.set_page_config(page_title="Visão Geral", layout="wide")

st.markdown("<h1 style='text-align: center'>Visão cidades</h1>", unsafe_allow_html=True)

#===============================
#Sidebar
#===============================
image = Image.open('logo.png')
st.sidebar.image(image=image, width=300)

st.sidebar.markdown("<h1 style='text-align: center'> Fome Zero</h1>", unsafe_allow_html=True)

paises = st.sidebar.multiselect(
    "Escolha o(s) Pais(es) que deseja visualizar",
    list(base_df['country_code'].unique()),
    default=['Brazil', 'England', 'Canada', 'South Africa']
)

base_df = base_df[base_df['country_code'].isin(list(paises))]
#=============================
#Layout
#=============================
st.markdown("""---""")
with st.container():
    st.markdown("<h2 style='text-align: center'>Top 10 Cidades com Mais Restaurantes na Base de Dados<h2>", unsafe_allow_html=True)
    fig = funcoes.top_cidades_mais_restaurantes(base_df)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""---""")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h3 style='text-align: center'>Top 7 Cidades com Restaurantes com Média de Avaliação acima de 4<h3>", unsafe_allow_html=True)
        fig = funcoes.top_cidades_mais_restaurantes_avaliacao_acima_4(base_df)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("<h3 style='text-align: center'>Top 7 Cidades com Restaurantes com Média de Avaliação abaixo de 2,5<h3>", unsafe_allow_html=True)
        fig = funcoes.top_cidades_mais_restaurantes_avaliacao_abaixo_25(base_df)
        st.plotly_chart(fig, use_container_width=True)

st.markdown("""---""")
with st.container():
    st.markdown("<h2 style='text-align: center'>Top 10 Cidades com Mais Tipos Culinários Distintos<h2>", unsafe_allow_html=True)
    fig = funcoes.top_cidades_culinarias_distintos(base_df)
    st.plotly_chart(fig, use_container_width=True)
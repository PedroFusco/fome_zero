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
st.set_page_config(page_title="Visão Países", layout="wide")


st.markdown("<h1 style='text-align: center'>Visão Países!</h1>", unsafe_allow_html=True)

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
    st.markdown("<h2 style='text_align=center'>Quantidade de Restaurantes Registrados por País</h2>", unsafe_allow_html=True)
    fig = funcoes.qtde_restaurante_pais(base_df)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""---""")
with st.container():
    st.markdown("<h2 style='text_align=center'>Quantidade de Cidades Registrados por País</h2>", unsafe_allow_html=True)
    fig = funcoes.qtde_cidade_pais(base_df)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""---""")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h2 style='text-align: center'>Média de Avaliações Feitas por País<h2>", unsafe_allow_html=True)
        fig = funcoes.media_avaliacao_pais(base_df)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.markdown("<h2 style='text-align: center'>Média de Preços de Prato Para Duas Pessoas<h2>", unsafe_allow_html=True)
        fig = funcoes.media_preco_pais(base_df)
        st.plotly_chart(fig, use_container_width=True)
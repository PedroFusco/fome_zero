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

st.markdown("<h1 style='text-align: center'>Fome Zero!</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center'> O melhor lugar para encontrar seu restaurante favorito!</h2>", unsafe_allow_html=True)

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

mapa_df = base_df[base_df['country_code'].isin(list(paises))]
#=============================
#Layout
#=============================
st.markdown("""---""")
with st.container():
    st.markdown("## Em nossa plataforma você terá acesso a")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        col1.metric("Restaurantes Cadastrados", format_decimal(base_df['restaurant_name'].nunique(), locale='pt_BR'))
    with col2:
        col2.metric("Países Cadastrados", format_decimal(base_df['country_code'].nunique(), locale='pt_BR'))
    with col3:
        col3.metric("Cidades Cadastradas", format_decimal(base_df['city'].nunique(), locale='pt_BR'))
    with col4:
        col4.metric("Avaliações Realizadas na Plataforma", format_decimal(base_df['votes'].sum(), locale='pt_BR'))
    with col5:
        col5.metric("Tipos de Culinárias Oferecidas", format_decimal(base_df['cuisines'].nunique(), locale='pt_BR'))

st.markdown("""---""")
with st.container():
    st.markdown("## Restaurantes Cadastrados")
    map = funcoes.restaurantes_mapa(mapa_df)
    folium_static(map, width=1350, height=800)


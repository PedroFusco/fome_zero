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

st.markdown("<h1 style='text-align: center'>Visão Tipos de Culinárias</h1>", unsafe_allow_html=True)

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


qtde_vis = st.sidebar.slider(
    "Selecione a Quantidade de Visualizações",
    value=10,
    min_value=1,
    max_value=20
)


culinarias = st.sidebar.multiselect(
    "Escolha o Tipo de Culinária",
    list(base_df['cuisines'].unique(),),
    default=['Home-made', 'BBQ', 'Japanese', 'Brazilian', 'American']
)



base_df = base_df[base_df['country_code'].isin(list(paises))]
base_df_tabela = base_df[(base_df['country_code'].isin(list(paises))) & (base_df['cuisines'].isin(list(culinarias)))]
#=============================
#Layout
#=============================
st.markdown("""---""")
with st.container():
    st.markdown(f"<h2 style='text-align: center'>Top {qtde_vis} Melhores Tipos Culinários<h2>", unsafe_allow_html=True)
    fig = funcoes.top_melhores_culinarias(base_df, qtde_vis)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""---""")
with st.container():
    st.markdown(f"<h2 style='text-align: center'>Top {qtde_vis} Piores Tipos Culinários<h2>", unsafe_allow_html=True)
    fig = funcoes.top_piores_culinarias(base_df, qtde_vis)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""---""")
with st.container():
    st.markdown(f"<h2 style='text-align: center'>Top {qtde_vis} Restaurantes<h2>", unsafe_allow_html=True)
    df = funcoes.tabela_top_restaurante(base_df_tabela, qtde_vis)
    st.dataframe(df)
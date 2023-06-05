
import inflection
import plotly.express as px


#Retira espaços no começo e no fim dos dados string
def retira_espaco(df):
    """
    Função que retira os espaços que possam existir antes e/ou depois de uma string 

    Input: Dataframe
    Output: Dataframe
    """
    columns = dict(df.dtypes == "object")
    strings = []
    for col in columns:
        if columns[col] == True:
            strings.append(col)
    for str in strings:
        df[str] = df[str].str.strip()
        
    return df

#Coloca nome dos países com base no código de cada país
COUNTRIES = {
1: "India",
14: "Australia",
30: "Brazil",
37: "Canada",
94: "Indonesia",
148: "New Zeland",
162: "Philippines",
166: "Qatar",
184: "Singapure",
189: "South Africa",
191: "Sri Lanka",
208: "Turkey",
214: "United Arab Emirates",
215: "England",
216: "United States of America"
}

CATEGORY = {
    1:"cheap",
    2:"normal",
    3:"expensive",
    4:"gourmet"
}

COLORS = {
"3F7E00": "darkgreen",
"5BA829": "green",
"9ACD32": "lightgreen",
"CDD614": "orange",
"FFBA00": "red",
"CBCBC8": "darkred",
"FF7800": "darkred",
}

def nome_paises(df):
    global COUNTRIES
    df['Country Code'] = df['Country Code'].replace(COUNTRIES)
    return df


#Tipo de categoria de comida
def categoria_comida(df):
    global CATEGORY
    df["Price range"] = df["Price range"].replace(CATEGORY)
    return df


#Criação do nome das Cores
def codigo_cores(df):
    global COLORS
    df['Rating color'] = df['Rating color'].replace(COLORS)
    return df


#Renomeando colunas
def renomeia_colunas(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

#===========================================================
#Funções Dashboard
#===========================================================

#===================
#Main Page
#===================
import folium
from folium.plugins import MarkerCluster

def restaurantes_mapa(to_map_df):
    to_map_df.rename(columns={'cuisines':'type'}, inplace=True)
    to_map_df.loc[:,'average_cost_for_two'] = to_map_df['average_cost_for_two'].apply(lambda x: '{:.2f}'.format(x).replace(".", ","))
    to_map_df['price'] = to_map_df['average_cost_for_two'] + ' (' + to_map_df['currency'] + ') ' + 'para dois'
    to_map_df['Aggregate Rating'] = to_map_df['aggregate_rating'].astype(str) + '/5.0'
    to_map_df = to_map_df[['country_code', 'restaurant_name', 'price', 'type', 'Aggregate Rating', 'latitude', 'longitude', 'rating_color']]
    map = folium.Map()
    cluster = MarkerCluster().add_to(map)
    for index, location_info in to_map_df.iterrows():
        folium.Marker(location=[location_info["latitude"],
                                location_info["longitude"]], 
                    popup=folium.Popup(
                        html='<h4>' + location_info["restaurant_name"] + '</h4>' + 
                            '<br>'
                            '<h5>' + 'Preço:' + ' ' + location_info['price'] + '</h5>' +
                            '<h5>' + 'Tipo Culinária:' + ' ' + location_info['type'] +  '<h5>' +
                            '<h5>' + 'Avaliação Média' + ' ' + location_info['Aggregate Rating'] + '<h5>',
                            min_width=300, max_width=300
                        ),
                    icon=folium.Icon(color=location_info['rating_color'], icon="utensils", prefix='fa')  
                        ).add_to(cluster)
    return map

#===================
#Main Page
#===================
def qtde_restaurante_pais(base_df):
    restaurante_por_pais = (
    base_df
    .groupby('country_code')
    .agg({'restaurant_id':'nunique'})
    .reset_index()
    .sort_values('restaurant_id', ascending=False)
    )

    fig = px.bar(data_frame=restaurante_por_pais, x='country_code', y='restaurant_id', text_auto=True,
       labels={'restaurant_id':'Quantidade de Restaurantes', 'country_code':'Países'})
    return fig


def qtde_cidade_pais(base_df):
    cidade_por_pais = (
    base_df
    .groupby('country_code')
    .agg({'city':'nunique'})
    .reset_index()
    .sort_values('city', ascending=False)
    )

    fig = px.bar(data_frame=cidade_por_pais, x='country_code', y='city', text_auto=True,
       labels={'city':'Quantidade de Cidades', 'country_code':'Países'})
    return fig

def media_avaliacao_pais(base_df):
    media_avaliacoes_por_pais = (
    base_df
    .groupby('country_code')
    .agg({'votes':'mean'})
    .reset_index()
    .sort_values('votes', ascending=False)
    )

    media_avaliacoes_por_pais['votes'] = media_avaliacoes_por_pais['votes'].round(2)

    fig = px.bar(data_frame=media_avaliacoes_por_pais, x='country_code', y='votes', text_auto=True,
       labels={'votes':'Quantidade Média de Avaliações', 'country_code':'Países'})
    return fig

def media_preco_pais(base_df):
    media_preco_prato_dois_por_pais = (
    base_df
    .groupby(['country_code', 'currency'])
    .agg({'average_cost_for_two':'mean'})
    .reset_index()
    .sort_values('average_cost_for_two', ascending=False)
    .rename(columns={'currency':'Moeda Local'})
    )

    media_preco_prato_dois_por_pais['average_cost_for_two'] = media_preco_prato_dois_por_pais['average_cost_for_two'].round(2)

    fig = px.bar(data_frame=media_preco_prato_dois_por_pais, x='country_code', y='average_cost_for_two', text_auto=True, text='Moeda Local',
        labels={'average_cost_for_two':'Preço Médio de Prato Para Duas Pessoa', 'country_code':'Países'})
    return fig
#=============================
#Visão Cidades
#=============================
def top_cidades_mais_restaurantes(base_df):
    top_cidades_mais_restaurantes = (
    base_df
    .groupby(['city', 'country_code'])
    .agg({'restaurant_id':'nunique'})
    .reset_index()
    .reset_index()
    .sort_values(['restaurant_id', 'index'], ascending=False)
    )

    fig = px.bar(data_frame=top_cidades_mais_restaurantes.head(10), x='city', y='restaurant_id', text_auto=True, color='country_code',
           labels={'city':'Cidades', 'restaurant_id':'Quantidade de Restaurantes', 'country_code':'País(es):'})
    return fig

def top_cidades_mais_restaurantes_avaliacao_acima_4(base_df):
    top_cidades_restaurantes_avaliacao_acima4 = (
    base_df[base_df['aggregate_rating'] > 4]
    .groupby(['city', 'country_code'])
    .agg({'restaurant_id':'nunique'})
    .reset_index()
    .reset_index()
    .sort_values(['restaurant_id', 'index'], ascending=False)
    )

    fig = px.bar(data_frame=top_cidades_restaurantes_avaliacao_acima4.head(7), x='city', y='restaurant_id', text_auto=True, color='country_code',
       labels={'city':'Cidades', 'restaurant_id':'Quantidade de Restaurantes', 'country_code':'País(es):'})
    return fig

def top_cidades_mais_restaurantes_avaliacao_abaixo_25(base_df):
    top_cidades_restaurantes_avaliacao_abaixo25 = (
    base_df[base_df['aggregate_rating'] < 2.5]
    .groupby(['city', 'country_code'])
    .agg({'restaurant_id':'nunique'})
    .reset_index()
    .reset_index()
    .sort_values(['restaurant_id', 'index'], ascending=False)
    )

    fig = px.bar(data_frame=top_cidades_restaurantes_avaliacao_abaixo25.head(7), x='city', y='restaurant_id', text_auto=True, color='country_code',
       labels={'city':'Cidades', 'restaurant_id':'Quantidade de Restaurantes', 'country_code':'País(es):'})
    return fig

def top_cidades_culinarias_distintos(base_df):
    top_cidades_mais_culinarias = (
    base_df
    .groupby(['city', 'country_code'])
    .agg({'cuisines':'nunique'})
    .reset_index()
    .reset_index()
    .sort_values(['cuisines', 'index'], ascending=False)
    )

    fig = px.bar(data_frame=top_cidades_mais_culinarias.head(10), x='city', y='cuisines', text_auto=True, color='country_code',
       labels={'city':'Cidades', 'cuisines':'Quantidade de Tipos Culinários Distintos', 'country_code':'País(es):'})
    return fig

#====================================
#Visão culinária
#===================================
def top_melhores_culinarias(base_df, qtde_culinaria):
    top_melhores_culinarias = (
    base_df
    .groupby(['cuisines', 'country_code'])
    .agg({'aggregate_rating':'mean'})
    .reset_index()
    .sort_values(['aggregate_rating'], ascending=False)
    )

    fig = px.bar(data_frame=top_melhores_culinarias.head(qtde_culinaria), x='cuisines', y='aggregate_rating', text_auto=True, color='country_code',
       labels={'aggregate_rating':'Média de Avaliações', 'cuisines':'Tipo Culinário','country_code':'País(es):'})
    return fig


def top_piores_culinarias(base_df, qtde_culinaria):
    top_melhores_culinarias = (
    base_df
    .groupby(['cuisines', 'country_code'])
    .agg({'aggregate_rating':'mean'})
    .reset_index()
    .sort_values(['aggregate_rating'])
    )

    fig = px.bar(data_frame=top_melhores_culinarias.head(qtde_culinaria), x='cuisines', y='aggregate_rating', text_auto=True, color='country_code',
       labels={'aggregate_rating':'Média de Avaliações', 'cuisines':'Tipo Culinário', 'country_code':'País(es):'})
    return fig


def tabela_top_restaurante(base_df, qtde_cuinaria):
    df = (
    base_df[['restaurant_name', 'country_code', 'city', 'cuisines', 'average_cost_for_two', 'aggregate_rating', 'votes']]
    .rename(columns={'restaurant_name':'Nome do Restaurante', 
                     'country_code':'País', 
                     'city':'Cidade',
                     'cuisines':'Tipo Culinário',
                     'average_cost_for_two':'Preço Médio Para Dois', 
                     'aggregate_rating':'Avaliação Média',
                     'votes':'Quantidade de Avaliações'})
    .sort_values('Avaliação Média', ascending=False)
    .head(qtde_cuinaria)
    )
    return df
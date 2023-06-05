# 1. Contexto do problema de negócio

Parabéns! Você acaba de ser contratado como Cientista de Dados da empresa
Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra
a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer
utilizando dados!

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante,
dentre outras informações.

O CEO Guerra também foi recém contratado e precisa entender melhor o negócio
para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da
empresa e que sejam gerados dashboards, a partir dessas análises, para responder
às seguintes perguntas:

## Geral

1. Quantos restaurantes únicos estão registrados?
3. Quantos países únicos estão registrados?
4. Quantas cidades únicas estão registradas?
5. Qual o total de avaliações feitas?
6. Qual o total de tipos de culinária registrados?

## País

1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Cidade

1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

## Restaurantes

1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

## Tipos de Culinária

1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação? 
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

# 2. Premissas assumidas para análise
1. Marketplace foi o modelo de negócio assumido.
2. As visões de negócio foram: Visão Países, visão cidades e visão tipos culinários

# 3. Estratégia da solução

O dashboard foi construido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa.

1. Visão por países
2. Visão por cidades
3. Visão por tipos culinários

Também encontramos no dashboard uma página principal contendo um mapa interativo para a visão detalhada dos restaurantes cadastrados.


## 1. Visão Geral

1. Quantidade total de restaurantes cadastrados
2. Quantidade total de países cadastrados
3. Quantidade total de cidades cadastradas
4. Quantidade total de avaliações realizadas
5. Quantidade total de tipos culinários cadastrados
6. Mapa interativo com localização dos restaurantes

## 2. Visão Países

1. Quantidade de restaurantes registrados por país
2. Quantidade de cidades c=registradas por país
3. Média de avaliaçòes realizadas por país
4. mëdia de preços de prato para duas pessoas por país

## 3. Visão Cidades

1. Top 10 cidades com mais restaurantes na base de dados
2. Top 7 cidades com restaurantes com média de avaliação acima de 4
3. Top 7 cidades com restaurantes com média de avaliação abaixo de 2,5
4. Top 10 cidades com mais tipos culinários distintos

## 4. Visão Culinárias

1. Top 10 melhores tipos culinários
2. Top 10 piores tipos culinários
3. Tabela com detalhes dos top 10 restaurantes

# 4. Top 3 Insights de dados

1. A Índia possui mais da metade da quantidade total de restaurantes cadastrados, uma média de pouco mais de 63 restaurantes por cidade.
2. As cidades Bangalore na Índia e Londres na Inglaterra possuem a maior quantidade de restaurantes com as melhores avaliações. Dos 80 restaurantes cadastrados em cada cidade, Bangalore possui 79 restaurantes com avaliações acima de 4 e Londres possui 78.
3. No Brasil, a maior parte dos restaurantes mais bem avaliados estão no Rio de Janeiro

# 5. O produto final do projeto

O produto final é um painel online hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet. O painel pode ser acessado pelo link: https://pedrofusco-projects-fomezero.streamlit.app/Vis%C3%A3o_Culin%C3%A1rias


# 6. Conclusão

O objetivo desse projeto é criar um conjento de gráficos e tabelas que exibam as métricas da melhor forma possível para o CEO. Na visão países temos a maior quantidade de restaurantes cadastrados na Índia, assim como a cidade com a maior quantidade de restaurantes mais bem avaliados.


# 7. Próximos passos

1. Aplicar visualizações mais objetivas
2. Aplicar novos filtros
3. Incluir novas visões de negócio











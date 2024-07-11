# 1. Problema de negócio
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
``` python
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?
```

## País
``` python
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
```

## Cidade
``` python
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
```
## Restaurante
``` python
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, osrestaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
```
# Tipos de Culinária
``` python
**1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
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
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?**
```

# 2. Premissas do negócio

# 3. Estratégia da solução
Para resolver esse desafio,  foi construido um dashboard gerencial com 3 visões: Visão de cidades, Visão de Paises e Visão de Tipos de Culinária, além da Visão geral que mostra informações gerais sobre a compania. 

Na visão geral tem as seguintes métricas:
	a. Restaurantes Cadastrados
	b. Países Cadastrados
	c. Cidades Cadastrados
	d. Avaliações Feitas na Plataforma
	e. Tipos de Culinárias Oferecida
	f. Mapa para visualização dos locais de cada restauraurante, bem como suas caracteristicas gerais
 
Na Visão Paises tem as seguintes métricas:
	a. Quantidade de Restaurantes registrados por Pais
	b. Quantidade de Cidade por Pais
	c. Média de Avaliações feitas por País
	d. Média de Preço de um prato para duas pessoas por País
 
Na Visão Cidades tem as seguintes métricas:
	a. Top 10 Cidades com mais Restaurantes
	b. Top 7 Cidades que tem Avaliação acima de 4
	c. Top 7 Cidades que tem Avaliação menor de 2.5
	d. Top 10 Cidades com mais Restaurantes
 
Na Visão Tipos de Culinária tem as seguintes métricas:
	a. metricas de culinarias italianas mais bem avaliadas
	b. Top 10 Melhores Restaurantes
	c. Top 10 Melhores Culinarias
	d. Top 10 Piores Culinarias

 
# 4. Top 3 Insights de dados
A Índia possui mais da metade da quantidade total de restaurantes cadastrados, uma média de pouco mais de 63 restaurantes por cidade.
As cidades Bangalore na Índia e Londres na Inglaterra possuem a maior quantidade de restaurantes com as melhores avaliações. Dos 80 restaurantes cadastrados em cada cidade, Bangalore possui 79 restaurantes com avaliações acima de 4 e Londres possui 78.
No Brasil, a maior parte dos restaurantes mais bem avaliados estão no Rio de Janeiro


Como esperado a maior concentração de Restaurantes está no continente asiático, com destaque para os Estados Unidos assumindo o segundo lugar com mais restaurantes registrados na plataforma
Não há diferença na média de valores dos pratos para duas pessoas em restaurantes que aceitem ou não reservas.
Os restaurantes com pedidos online recebem mais acessos de avaliações na plataforma

# 5. O produto final do projeto
O produto final é um painel online hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet. O painel pode ser acessado pelo link: 

# 6. Conclusão
O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

# 7. Próximo passos
Reduzir o número de métricas.
Dispor de features com as informações dos clientes (Sexo, Idade).
Dispor de features com período/datas de conversão das compras;
Adicionar uma feature com a conversão dos valores dos pratos para uma moeda única (utilização por exemplo do Dólar como padrão);
Criar modelo para prever satisfação dos clientes
Adicionar novas visões de negócio.
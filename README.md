# Business Problem Context
Zero Hunger is a restaurant marketplace designed to facilitate transactions between customers and restaurants. Restaurants register on the Fome Zero platform, providing details such as address, cuisine type, reservation availability, delivery options, and service/product ratings, among other information.

The company recently appointed a new CEO who needs to understand the business to make informed decisions and elevate Fome Zero further. To achieve this, an analysis of the company's data is necessary, along with the creation of dashboards to answer the following questions:

### General Questions
```python
- How many unique restaurants are registered?
- How many unique countries are registered?
- How many unique cities are registered?
- What is the total number of reviews made?
- What is the total number of registered cuisine types?
```

### Country-Specific Questions
``` python

- Which country has the most registered cities?
- Which country has the most registered restaurants?
- Which country has the most restaurants with a price level of 4?
- Which country has the highest number of distinct cuisine types?
- Which country has the highest number of reviews made?
- Which country has the highest number of restaurants that offer delivery?
- Which country has the highest number of restaurants that accept reservations?
- Which country has, on average, the highest number of reviews?
- Which country has, on average, the highest average rating?
- Which country has, on average, the lowest average rating?
- What is the average price of a meal for two per country?

``` 

### City-Specific Questions
```python

- Which city has the most registered restaurants?
- Which city has the most restaurants with an average rating above 4?
- Which city has the most restaurants with an average rating below 2.5?
- Which city has the highest average price for a meal for two?
- Which city has the highest number of distinct cuisine types?
- Which city has the highest number of restaurants that accept reservations?
- Which city has the highest number of restaurants that offer delivery?
- Which city has the highest number of restaurants that accept online orders?

```

### Restaurant-Specific Questions
```python

- Which restaurant has the highest number of reviews?
- Which restaurant has the highest average rating?
- Which restaurant has the highest price for a meal for two?
- Which Brazilian cuisine restaurant has the lowest average rating?
- Which Brazilian cuisine restaurant in Brazil has the highest average rating?
- Do restaurants that accept online orders also have, on average, the highest number of reviews?
- Do restaurants that accept reservations also have, on average, the highest average price for a meal for two?
- Do Japanese cuisine restaurants in the United States have a higher average price for a meal for two compared to American BBQ restaurants?

```

### Cuisine Type Questions
```python

- Among Italian cuisine restaurants, which has the highest average rating?
- Among Italian cuisine restaurants, which has the lowest average rating?
- Among American cuisine restaurants, which has the highest average rating?
- Among American cuisine restaurants, which has the lowest average rating?
- Among Arabian cuisine restaurants, which has the highest average rating?
- Among Arabian cuisine restaurants, which has the lowest average rating?
- Among Japanese cuisine restaurants, which has the highest average rating?
- Among Japanese cuisine restaurants, which has the lowest average rating?
- Among home-style cuisine restaurants, which has the highest average rating?
- Among home-style cuisine restaurants, which has the lowest average rating?
- Which cuisine type has the highest average price for a meal for two?
- Which cuisine type has the highest average rating?
- Which cuisine type has the most restaurants that accept online orders and offer delivery?

```

# Solution Strategy
To address these questions, a management dashboard was built to monitor the company’s key metrics. This includes three perspectives on the business model: by city, by country, and by cuisine types, as well as an overall view.

### Overall View Panel Metrics:

1. Total number of registered restaurants
2. Total number of registered countries
3. Total number of registered cities
4. Total number of reviews made
5. Total number of registered cuisine types
6. Interactive map showing restaurant locations and general characteristics

### City View Panel Metrics:

1. Top 10 cities with the most restaurants
2. Top 7 cities with restaurants with the highest average rating (above 4)
3. Top 7 cities with restaurants with the lowest average rating (below 2.5)
4. Top 10 cities with the most distinct cuisine types

### Country View Panel Metrics:

1. Number of registered restaurants by country
2. Average number of reviews by country
3. Average price for a meal for two by country

### Cuisine Types View Panel Metrics:

1. The best restaurant for each cuisine type: American, Arabian, Brazilian, Italian, Japanese, along with their ratings
2. Top 10 best cuisine types
3. Top 10 worst cuisine types
4. Table with details of the top 10 restaurants
        
# Top 3 Data Insights
- Restaurants that accept online orders receive more reviews.
- The largest number of restaurants is in Asia, indicating a consolidated market.
- India has the highest number of registered restaurants, with more than half of the total restaurants.

# Final Project Product
The final product is a dashboard hosted on Streamlit Cloud, accessible from any internet-connected device. The link to the dashboard is: https://bruno-nazario-zero-hunger.streamlit.app

# Conclusion
The goal of this project is to create data visualizations that display metrics in the best way for the company’s CEO to make data-driven decisions.

# Next Steps
- Reduce the number of metrics
- Apply new filters
- Create new views to explore the restaurants
- Develop a model to predict customer satisfaction

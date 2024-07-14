import pandas as pd
import plotly.express as px


color_map = {
        "Brazil": "green",
        "Philippines": "blue",
        "Australia": "purple",
        "United States of America": "red",
        "Canada": "lime",
        "Singapore": "brown",
        "United Arab Emirates": "pink",
        "India": "gray",
        "Indonesia": "yellow",
        "New Zealand": "cyan",
        "England": "magenta",
        "Qatar": "orange",
        "South Africa": "navy",
        "Sri Lanka": "olive",
        "Turkey": "maroon",
    }

def read_processed_data():
    return pd.read_csv("./data/processed_data.csv")

def create_bar_chart(df, x_col, y_col, title, x_label, y_label, text_auto=".2f", color=None, color_map=None):
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        text=y_col,
        text_auto=text_auto,
        color=color,
        title=title,
        labels={
            x_col: x_label,
            y_col: y_label,
        },
        color_discrete_map=color_map
    )
    return fig

def top_cities_restaurants(countries, top_n=10, color_map =  None):
    df = read_processed_data()
    filtered_df = df[df["country"].isin(countries)]

    grouped_df = (
        filtered_df.groupby(["country", "city"])
        .size()
        .reset_index(name="restaurant_count")
        .sort_values(["restaurant_count", "city"], ascending=[False, True])
        .head(top_n)
    )

    return create_bar_chart(
        grouped_df, 
        x_col="city", 
        y_col="restaurant_count", 
        title="Top Cities with Most Restaurants in the Database", 
        x_label="City", 
        y_label="Number of Restaurants", 
        color="country",
        color_map=color_map
    )

def top_best_restaurants(countries, rating_threshold, top_n=7, color_map=None):
    df = read_processed_data()
    filtered_df = df[(df["country"].isin(countries)) & (df["aggregate_rating"] >= rating_threshold)]

    grouped_df = (
        filtered_df.groupby(["country", "city"])
        .size()
        .reset_index(name="restaurant_count")
        .sort_values(["restaurant_count", "city"], ascending=[False, True])
        .head(top_n)
    )

    return create_bar_chart(
        grouped_df, 
        x_col="city", 
        y_col="restaurant_count", 
        title=f"Top {top_n} Cities with Restaurants with Best Ratings", 
        x_label="City", 
        y_label="Number of Restaurants", 
        color="country",
        color_map=color_map
    )

def top_worst_restaurants(countries, rating_threshold, top_n=7, color_map=None):
    df = read_processed_data()
    filtered_df = df[(df["country"].isin(countries)) & (df["aggregate_rating"] <= rating_threshold)]

    grouped_df = (
        filtered_df.groupby(["country", "city"])
        .size()
        .reset_index(name="restaurant_count")
        .sort_values(["restaurant_count", "city"], ascending=[False, True])
        .head(top_n)
    )

    return create_bar_chart(
        grouped_df, 
        x_col="city", 
        y_col="restaurant_count", 
        title=f"Top {top_n} Cities with Restaurants with Worst Ratings", 
        x_label="City", 
        y_label="Number of Restaurants", 
        color="country",
        color_map=color_map
    )

def most_cuisines(countries, top_n=10, color_map = None):
    df = read_processed_data()
    filtered_df = df[df["country"].isin(countries)]

    grouped_df = (
        filtered_df.groupby(["country", "city"])
        .nunique()["cuisines"]
        .reset_index(name="unique_cuisines")
        .sort_values(["unique_cuisines", "city"], ascending=[False, True])
        .head(top_n)
    )

    return create_bar_chart(
        grouped_df, 
        x_col="city", 
        y_col="unique_cuisines", 
        title=f"Top {top_n} Cities with Most Restaurants Offering Unique Cuisines", 
        x_label="City", 
        y_label="Number of Unique Cuisines", 
        color="country", 
        color_map=color_map
    )
import pandas as pd
import plotly.express as px
import streamlit as st

def read_processed_data():
    return pd.read_csv("./data/processed_data.csv")

def create_bar_chart(df, x_col, y_col, title, x_label, y_label, text_auto=".2f"):
    fig = px.bar(
        df,
        x=x_col,
        y=y_col,
        text=y_col,
        text_auto=text_auto,
        title=title,
        labels={
            x_col: x_label,
            y_col: y_label,
        },
    )
    return fig

def countries_restaurants(countries):
    df = read_processed_data()
    grouped_df = (
        df.loc[df["country"].isin(countries), ["restaurant_id", "country"]]
        .groupby("country")
        .count()
        .sort_values("restaurant_id", ascending=False)
        .reset_index()
    )
    return create_bar_chart(grouped_df, "country", "restaurant_id", "Number of Registered Restaurants per Country", "Countries", "Number of Restaurants")

def countries_cities(countries):
    df = read_processed_data()
    grouped_df = (
        df.loc[df["country"].isin(countries), ["city", "country"]]
        .groupby("country")
        .nunique()
        .sort_values("city", ascending=False)
        .reset_index()
    )
    return create_bar_chart(grouped_df, "country", "city", "Number of Registered Cities per Country", "Countries", "Number of Cities")

def countries_mean_votes(countries):
    df = read_processed_data()
    grouped_df = (
        df.loc[df["country"].isin(countries), ["votes", "country"]]
        .groupby("country")
        .mean()
        .sort_values("votes", ascending=False)
        .reset_index()
    )
    return create_bar_chart(grouped_df, "country", "votes", "Average Ratings Made per Country", "Countries", "Number of Ratings")

def countries_average_plate(countries):
    df = read_processed_data()
    grouped_df = (
        df.loc[df["country"].isin(countries), ["average_cost_for_two", "country"]]
        .groupby("country")
        .mean()
        .sort_values("average_cost_for_two", ascending=False)
        .reset_index()
    )
    return create_bar_chart(grouped_df, "country", "average_cost_for_two", "Average Price of a Meal for Two Persons per Country", "Countries", "Price of Meal for Two")

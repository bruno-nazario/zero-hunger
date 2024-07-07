import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


def read_processed_data():
    return pd.read_csv("./data/processed_data.csv")

def top_cuisines():
    df = read_processed_data()

    cuisine_types = ["Italian", "American", "Arabian", "Japanese", "Brazilian"]
    
    df_filtered = df[df['cuisines'].isin(cuisine_types)]

    idx = df_filtered.groupby('cuisines')['aggregate_rating'].idxmax()

    top_restaurants = df.loc[idx, [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "currency",
        "aggregate_rating",
        "votes"
    ]]

    cuisines = top_restaurants.set_index('cuisines').T.to_dict()

    return cuisines

def write_metrics():
    cuisines = top_cuisines()
    cols = st.columns(len(cuisines))

    for col, (cuisine, details) in zip(cols, cuisines.items()):
        with col:
            st.metric(
                label=f'{cuisine}: {details["restaurant_name"]}',
                value=f'{details["aggregate_rating"]}/5.0',
                help=f"""
                Country: {details['country']}\n
                City: {details['city']}\n
                Average cost for two: {details['average_cost_for_two']} ({details['currency']})
                """
            )

def top_restaurants(countries, cuisines, top_n):
    df = read_processed_data()

    cols = [
        "restaurant_id",
        "restaurant_name",
        "country",
        "city",
        "cuisines",
        "average_cost_for_two",
        "aggregate_rating",
        "votes",
    ]

    lines = (df["cuisines"].isin(cuisines)) & (df["country"].isin(countries))

    dataframe = df.loc[lines, cols].sort_values(
        ["aggregate_rating", "restaurant_id"], ascending=[False, True]
    )

    return dataframe.head(top_n)

def top_best_cuisines(countries, top_n):
    df = read_processed_data()
    lines = df["country"].isin(countries)
    grouped_df = (
        df.loc[lines, ["aggregate_rating", "cuisines"]]
        .groupby("cuisines")
        .mean()
        .sort_values("aggregate_rating", ascending=False)
        .reset_index()
        .head(top_n)
    )

    fig = px.bar(
        grouped_df.head(top_n),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"Top {top_n} Best Types of Cuisines",
        labels={
            "cuisines": "Type of Cuisine",
            "aggregate_rating": "Rating",
        },
    )

    return fig

def top_worst_cuisines(countries, top_n):
    df = read_processed_data()
    lines = df["country"].isin(countries)
    grouped_df = (
        df.loc[lines, ["aggregate_rating", "cuisines"]]
        .groupby("cuisines")
        .mean()
        .sort_values("aggregate_rating")
        .reset_index()
        .head(top_n)
    )

    fig = px.bar(
        grouped_df.head(top_n),
        x="cuisines",
        y="aggregate_rating",
        text="aggregate_rating",
        text_auto=".2f",
        title=f"Top {top_n} Worst Types of Cuisines",
        labels={
            "cuisines": "Type of Cuisine",
            "aggregate_rating": "Rating",
        },
    )

    return fig
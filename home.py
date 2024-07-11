import folium
import pandas as pd
import streamlit as st
from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static
from utilities import general_functions as gf

def create_sidebar(df):
    image = Image.open("logo.png")

    col1, col2 = st.sidebar.columns([1, 3])
    col1.image(image, width=65)
    col2.title(" Zero Hunger")

    st.sidebar.markdown("## Filters")

    country_list = ["All"] + df['country'].unique().tolist()

    countries = st.sidebar.multiselect(
        "Choose the countries where you want to view the restaurants",
        country_list,
        default=["All"],
    )

    st.sidebar.markdown("### Processed Data")

    try:
        processed_data = pd.read_csv("processed_data.csv")
        st.sidebar.download_button(
            label="Download",
            data=processed_data.to_csv(index=False),
            file_name="processed_data.csv",
        )
    except FileNotFoundError:
        st.sidebar.error("File processed_data.csv was not found.")

    if "All" in countries:
        return df['country'].unique().tolist()
    else:
        return countries

def create_map(dataframe):
    fig = folium.Figure(width=1920, height=1080)
    map = folium.Map(max_bounds=True).add_to(fig)
    marker_cluster = MarkerCluster().add_to(map)

    for _, row in dataframe.iterrows():
        name = row["restaurant_name"]
        price_for_two = row["average_cost_for_two"]
        cuisine = row["cuisines"]
        currency = row["currency"]
        rating = row["aggregate_rating"]

        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 ({}) for two"
        html += "<br />Type: {}"
        html += "<br />Aggragate Rating: {}/5.0"
        html = html.format(name, price_for_two, currency, cuisine, rating)

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )

        folium.Marker(
            [row["latitude"], row["longitude"]],
            popup=popup,
            icon=folium.Icon(icon="home"),
        ).add_to(marker_cluster)

    folium_static(map, width=1024, height=768)

def main():
    df = gf.read_process_data("zomato.csv")
    st.set_page_config(page_title="Home", page_icon="📌", layout="wide")

    selected_countries = create_sidebar(df)

    st.markdown("# Zero Hunger")

    st.markdown("## The best place to find your new favorite restaurant!")

    st.markdown("### We have the following brands on our platform:")

    # Columns 
    restaurants, countries, cities, ratings, cuisines = st.columns(5)
    num_votes = df['votes'].sum()

    restaurants.metric(
        "Registered Restaurants",
        gf.unique_thing(df, 'restaurant_id'),
    )

    countries.metric(
        "Registered Countries",
        gf.unique_thing(df, 'country_code'),
    )

    cities.metric(
        "Registered Cities",
        gf.unique_thing(df,'city'),
    )
    
    ratings.metric(
        "Reviews on the Platform",
        num_votes,
    )

    cuisines.metric(
        f"Types of Cuisines\n Offered",
        gf.unique_thing(df, 'cuisines'),
    )

    selected_df = df.loc[df["country"].isin(selected_countries), :]
    create_map(selected_df)
    
if __name__ == "__main__":
    main()

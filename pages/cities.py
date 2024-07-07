import streamlit as st
import utilities.cities_answers as ca
import plotly.express as px


def make_sidebar(df):
    st.sidebar.markdown("## Filtros")

    countries = st.sidebar.multiselect(
        "Choose the countries you want to view the informations",
        df["country"].unique().tolist(),
        default=["Brazil"],
    )

    return list(countries)


def main():
    st.set_page_config(page_title="Cities", page_icon="📌", layout="wide")

    df = ca.read_processed_data()

    countries = make_sidebar(df)

    st.markdown("# :cityscape: City View")

    fig = ca.top_cities_restaurants(countries)

    st.plotly_chart(fig, use_container_width=True)

    best, worst = st.columns(2)

    with best:
        fig = ca.top_best_restaurants(countries, 4)
        fig.update_traces(marker_color='red')
        st.plotly_chart(fig, use_container_width=True)

    with worst:
        fig = ca.top_worst_restaurants(countries, 2.5)
        fig.update_traces(marker_color='green')
        st.plotly_chart(fig, use_container_width=True)

    fig = ca.most_cuisines(countries)
    fig.update_traces(marker_color=px.colors.qualitative.Plotly)
    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
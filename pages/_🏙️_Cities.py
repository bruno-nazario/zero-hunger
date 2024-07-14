import streamlit as st
import utilities.cities_answers as ca

def make_sidebar(df):
    st.sidebar.markdown("## Filtros")

    country_list = ["All"] + df['country'].unique().tolist()
    
    countries = st.sidebar.multiselect(
        "Choose the countries you want to view the informations",
        country_list,
        default=["All"],
    )

    if "All" in countries:
        return df['country'].unique().tolist()
    else:
        return countries

def main():
    st.set_page_config(page_title="Cities", page_icon="🏙️", layout="wide")

    df = ca.read_processed_data()

    countries = make_sidebar(df)

    st.markdown("# :cityscape: City View")
    
    fig = ca.top_cities_restaurants(countries, color_map=ca.color_map)

    st.plotly_chart(fig, use_container_width=True)

    best, worst = st.columns(2)

    with best:
        fig = ca.top_best_restaurants(countries, 4, color_map=ca.color_map)
        st.plotly_chart(fig, use_container_width=True)

    with worst:
        fig = ca.top_worst_restaurants(countries, 2.5, color_map=ca.color_map)
        st.plotly_chart(fig, use_container_width=True)

    fig = ca.most_cuisines(countries, color_map=ca.color_map)
    st.plotly_chart(fig, use_container_width=True)


if __name__ == "__main__":
    main()
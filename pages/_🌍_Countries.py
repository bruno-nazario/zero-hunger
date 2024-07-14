import streamlit as st

import utilities.countries_answers as coa


def make_sidebar(df):
    st.sidebar.markdown("## Filters")

    country_list = ["All"] + df['country'].unique().tolist()

    countries = st.sidebar.multiselect(
        "Choose the countries you want to view the information",
        country_list,
        default=["All"],
    )

    if "All" in countries:
        return df['country'].unique().tolist()
    else:
        return countries


def main():
    st.set_page_config(page_title="Countries", page_icon="🌍", layout="wide")

    df = coa.read_processed_data()

    countries = make_sidebar(df)

    st.markdown("# :earth_americas: Countries View")

    fig = coa.countries_restaurants(countries, coa.color_map)
    fig.update_traces(marker_color='blue')
    st.plotly_chart(fig, use_container_width=True)

    fig = coa.countries_cities(countries, coa.color_map)
    votes, plate_price = st.columns(2)

    with votes:
        fig = coa.countries_mean_votes(countries, coa.color_map)
        fig.update_traces(marker_color='cyan')
        st.plotly_chart(fig, use_container_width=True)

    with plate_price:
        fig = coa.countries_average_plate(countries, coa.color_map)
        fig.update_traces(marker_color='cyan')
        st.plotly_chart(fig, use_container_width=True)

    return None


if __name__ == "__main__":
    main()

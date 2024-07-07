import streamlit as st

import utilities.countries_answers as cdt


def make_sidebar(df):
    st.sidebar.markdown("## Filters")

    countries = st.sidebar.multiselect(
        "Choose the countries you want to view the information",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil"],
    )

    return list(countries)


def main():
    st.set_page_config(page_title="Countries", page_icon="📌", layout="wide")

    df = cdt.read_processed_data()

    countries = make_sidebar(df)

    st.markdown("# :earth_americas: Countries View")

    fig = cdt.countries_restaurants(countries)
    fig.update_traces(marker_color='blue')
    st.plotly_chart(fig, use_container_width=True)

    fig = cdt.countries_cities(countries)
    fig.update_traces(marker_color='blue')
    st.plotly_chart(fig, use_container_width=True)
    fig.update_traces(marker_color='red')

    votes, plate_price = st.columns(2)

    with votes:
        fig = cdt.countries_mean_votes(countries)
        fig.update_traces(marker_color='green')
        st.plotly_chart(fig, use_container_width=True)

    with plate_price:
        fig = cdt.countries_average_plate(countries)
        fig.update_traces(marker_color='green')

        st.plotly_chart(fig, use_container_width=True)

    return None


if __name__ == "__main__":
    main()

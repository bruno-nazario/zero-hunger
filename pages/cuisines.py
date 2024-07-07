import streamlit as st

import utilities.cuisine_answers as cdt


def make_sidebar(df):
    st.sidebar.markdown("## Filters")

    countries = st.sidebar.multiselect(
        "Choose the countries you want to view the information",
        df.loc[:, "country"].unique().tolist(),
        default=["Brazil"],
    )

    top_n = st.sidebar.slider(
        "Select the number of restaurants to display", 1, 20, 10
    )

    cuisines = st.sidebar.multiselect(
        "Choose the cuisine types",
        df.loc[:, "cuisines"].unique().tolist(),
        default=[
            "Brazilian",
        ],
    )

    return list(countries), top_n, list(cuisines)

def main():
    st.set_page_config(page_title="Cuisines", page_icon="📌", layout="wide")

    df = cdt.read_processed_data()

    countries, top_n, cuisines = make_sidebar(df)

    st.markdown("# :knife_fork_plate: Cuisine Types View")

    df_restaurants = cdt.top_restaurants(countries, cuisines, top_n)

    st.markdown(f"## Best Restaurants by Top Cuisine Types")

    cdt.write_metrics()

    st.markdown(f"## Top {top_n} Restaurants")

    st.dataframe(df_restaurants)

    best, worst = st.columns(2)

    with best:
        fig = cdt.top_best_cuisines(countries, top_n)
        fig.update_traces(marker_color='green')

        st.plotly_chart(fig, use_container_width=True)

    with worst:
        fig = cdt.top_worst_cuisines(countries, top_n)
        fig.update_traces(marker_color='red')
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()

import streamlit as st

import utilities.cuisine_answers as cdt


def make_sidebar(df):
    st.sidebar.markdown("## Filters")

    country_list = ["All"] +  df.loc[:, "country"].unique().tolist()

    countries = st.sidebar.multiselect(
        "Choose the countries you want to view the information",
        country_list,
        default=["All"],
    )

    top_n = st.sidebar.slider(
        "Select the number of restaurants to display", 1, 20, 10
    )

    cuisine_list = ["All"] + df.loc[:, "cuisines"].unique().tolist()

    cuisines = st.sidebar.multiselect(
        "Choose the cuisine types",
        cuisine_list,
        default=["All"],
    )
    
    if "All" in countries:
        if "All" in cuisines:
            return df['country'].unique().tolist(), top_n, df['cuisines'].unique().tolist()
        else:
            return df['country'].unique().tolist(), top_n, list(cuisines)  
    else:
        return countries, top_n, list(cuisines)

def main():
    st.set_page_config(page_title="Cuisines", page_icon="🥘", layout="wide")

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
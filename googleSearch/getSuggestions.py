from string import ascii_lowercase

import streamlit as st
from iso3166 import countries
from data_processing import *
from plotting import *

st.set_page_config(
    page_title="WebScrapers - Search",
    page_icon="assets/images/roulette-icon-light.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

country_names = []
for c in countries:
    country_names.append(c[0])

# ==== Main App
c1,c2,c3 = st.columns([0.2,0.6,0.2])
with c2:
    st.title("Google Search Autocomplete - App")
col1a, col1b = st.columns([0.2, 0.8])
with col1a:
    with st.form(key='update prompt'):
        st.markdown('WebScrapers - Search')
        prompt = st.text_input("Search:", "What is the best")
        country = st.selectbox('Country:', options=country_names, index=39)
        country_code = countries.get(country)[1]

        seed = [c for c in ascii_lowercase]
        col1a_1, col1a_2, col1a_3 = st.columns([1, 1, 1])
        with col1a_1:
             bg_colour = st.color_picker("Background colour", "#080808")
        with col1a_2:
            font_colour = st.color_picker("Font colour", "#FDFDFF")
        with col1a_3:
            line_colour = st.color_picker("Line colour", "#F7BF04")
        st.form_submit_button('Update')
with col1b:
    st.markdown("Google search autocomplete visualize:")
    # get and transform data based on inputs
    data = get_suggestions(prompt, seed, country_code)
    data_for_plot = get_relevant_results(data, seed, prompt)
    table = get_table_view(data, seed, prompt)
    # create and visualise plot
    fig = plot_circular_outward(data_for_plot, prompt, bg_colour, font_colour, line_colour)
    with col1b:
        st.write(fig)
        plt.savefig("google-search-autocomplete.png", bbox_inches="tight", dpi=300, pad_inches=1)
        with open("google-search-autocomplete.png", "rb") as image:
            png = st.download_button(
                label="Download image",
                data=image,
                file_name="google-search-autocomplete.png",
                mime="image/png"
            )
        st.write("")
        with st.expander("Explore first three suggestions"):
            st.dataframe(table, use_container_width=False)

        st.write("")
        st.divider()




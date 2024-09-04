import streamlit as st
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(page_title="DataPecuario", layout="wide")

nav = get_nav_from_toml("DataProduct/pages.toml")

st.logo("brand/PNG/Identificador_horizontal.png")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()


import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages
import json
import numpy as np
import pandas as pd 
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

st.set_page_config(layout="wide")

nav = get_nav_from_toml("DataProduct/pages.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()


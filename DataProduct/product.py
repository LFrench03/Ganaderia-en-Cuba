import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages
import json
import numpy as np
import pandas as pd 
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objects as go

st.set_page_config(layout="wide")

sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml("DataProduct/pages&sections.toml" if sections else "DataProduct/pages.toml")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()

with open('inventario_ganado.json',encoding="utf8") as json_data: 
    data = json.load(json_data)  
    
df = pd.DataFrame(data)




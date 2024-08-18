import streamlit as st
from st_pages import add_page_title, get_nav_from_toml, hide_pages
import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

st.write("Existencia")

with open('inventario_ganado.json',encoding="utf8") as json_data: 
    data = json.load(json_data)  
    


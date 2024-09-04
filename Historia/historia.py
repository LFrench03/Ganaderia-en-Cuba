import streamlit as st
from streamlit_timeline import timeline

st.logo(image="brand/PNG/Identificador_horizontal.png")
st.set_page_config(page_title="DataPecuario Timeline", layout="wide")

with open("Historia/events.json", "r") as f:
    data = f.read()

timeline(data, height=800)
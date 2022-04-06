import streamlit as st
import pandas as pd

url = "https://github.com/allisonhorst/palmerpenguins/raw/master/inst/extdata/penguins.csv"
data = pd.read_csv(url)

st.write("""
# Palmers Penguins!

Meet the penguins
""")

# st.bar_chart(data)
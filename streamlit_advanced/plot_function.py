import streamlit as st
import pandas as pd
import numpy as np

st.title("This is a plot app")

data = pd.DataFrame({
    "X": np.random.randn(100),
    "Y": np.random.randn(100)
})

st.line_chart(data, use_container_width=True)

# We can also see the map here

st.map()
# Here let's check the api requests instreamlit

import streamlit as st
import requests

st.title("Currency converter app")

amount = st.number_input("Enter the amout in INR: ", min_value=1)

selected_currency = st.selectbox("Convert the INR to: ", ["USD", "EUR", "GPB", "JPY"])

if st.button(f"Convert to {selected_currency}"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][selected_currency]
        converted = rate *amount
        st.success(f"{amount} INR = {converted:.2f} {selected_currency}")
    else:
        st.error("Failed to fetch conversion rate")
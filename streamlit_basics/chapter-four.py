# Here we will see how we get the csv file or any tabular file in stramlit and then using pandas and streamlit
# show a preview to the user

import streamlit as st

import pandas as pd

st.title("File Upload")

file = st.file_uploader("Upload your file", type=["csv", "xlsx"])

# Now we have the file from the streamlit. Let's read it using pandas

if file:

    df = pd.read_csv(file)

    # Now let's display it in the csv

    st.subheader("Data Preview:")

    st.dataframe(df)

    # It by default provides us options for download, search and maximize. It also provides the sorting option by
    # default in streamlit ui

# Let's provide as summary or pandas describe

if file:
    # df = pd.read_csv(file)

    st.subheader("Summary of the data:")
    st.write(df.describe())

# Now we can provide an option to filter the data by user selection for a particular column
# Let's filter by city in train data csv

if file:
    cities = df['Location'].unique()
    # new_cities=cities.add(0, "select")

    selected_cities = st.selectbox("Select your preferred city: ", cities)
    st.write(f"Selected city is {selected_cities}")
    
    if selected_cities:
        filtered_data = df[df["Location"]==selected_cities]
        st.subheader("The filtered data based on select city is: ")
        st.dataframe(filtered_data)
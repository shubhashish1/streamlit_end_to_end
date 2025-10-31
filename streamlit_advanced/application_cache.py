# Here let's say we have 4 users and all of them have their own session_states. But if user1 has asked for an image
# which we get from an api call which incurs some cost, then we can store that image in the aplication cache. Then
# if let's say user3 asks for that same image then istead of fetching it from the api again we can look for the cache
# first if not present then download
# But here the api request is same for all the users they should not be different for different users. Means
# each user should use the same code to access the same api to get desired images. 

# There are 2 types of cache elements in st
# st.cache_data:
# st.cache_resource:

# Let's see about about cache_data:
# Here we do a double check once we call a function to check if the data we are asking is present in the cache or not
# We use it as decorator above the function

"""
WITHOUT CACHE_DATA DECORATOR we will have a different dog image each time we reload through refresh or reload_page
button:

Code without cache_data decorator

import streamlit as st
import requests, time

# cache_data
def fetch_data(api_url):
    response = requests.get(api_url)
    time.sleep(5)
    return response.json()

data = fetch_data("https://dog.ceo/api/breeds/image/random")
st.write(data)
# Let's sjow the image fetched from api
st.image(data["message"], caption = "Random dog image")
st.button("Reload page")
"""

import streamlit as st
import requests, time

@st.cache_data
def fetch_data(api_url):
    response = requests.get(api_url)
    time.sleep(5)
    return response.json()

data = fetch_data("https://dog.ceo/api/breeds/image/random")
st.write(data)
# Let's sjow the image fetched from api
st.image(data["message"], caption = "Random dog image")
st.button("Reload page")

# Here each time we do reload page or relad the url we will get the same dog image from the cache_data

# We use cache_data when we have the data which is serializable or can be stored as serialized manner like 1,2,3
# For example strings, jsons etc


# FOR NON-SEALIZABLE OBJECTS WE USE CACHE_RESOURCE
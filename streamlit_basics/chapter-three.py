# Here we will be checking the layouts in streamlit

import streamlit as st

st.title("Coffee taste poll")

# Now let's have 2 cols which will be trated as different pages or layouts.
# We can use it to show the features of one type of coffee and ask the user to vote and then the users can vote
# as per their choice

col1, col2 = st.columns(2)

with col1:
    st.header("Black coffee")
    # Let's add one image here

    st.image("https://images.pexels.com/photos/733763/pexels-photo-733763.jpeg",
             width=150)
    vote1 = st.button("Vote for black coffee")

with col2:
    st.header("Espresso")
    # Let's add one image here

    st.image("https://images.pexels.com/photos/685527/pexels-photo-685527.jpeg",
             width=250)
    vote2 = st.button("Vote for Espresso")

if vote1:
    st.success("Thanks for voting Black coffee")
elif vote2:
    st.success("Thanks for voting Espresso")

# Now let's put something in sidebar by using the kyeword sidebar

name = st.sidebar.text_input("Enter your name: ")
coffee_choice = st.sidebar.selectbox("Select your coffee:", ["Black Coffee", "Espresso"])
if name:
     st.sidebar.write(f"Hello {name}! Your {coffee_choice} is getting ready")

# If we put the keyword sidebar, things will appear in side bar, else in the body

# Now let's learn more more interesting feature expander

with st.expander("Show coffee making instructions: "):
    st.write("""
    1. Boil water
    2. Add coffee powder/beans
    3. Add milk and sugar if you want
""")

# Let's check the use of markdown

st.markdown("### Welcome to Coffee app")
st.markdown("> Hello coffee lover, welcome!!!")
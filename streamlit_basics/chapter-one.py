import streamlit as st

# Let's add a title to our page

st.title("Hello first app")

# Let's have our header which is called as subheader attribute in st

st.subheader("Brewed with streamlit")

# Body 
st.text("Welcome to first interactive app")

# write text on page

st.write("Choose your fav, variety of coffee: ")

# So both st.text and st.write are to write text on the page

# Now we can check the dropdown option

coffee = st.selectbox("Enter your favourite coffee: ", ["Black coffee", "Espresso", "Dalgona"])
# Here we are giving the first option as what we want the user to select which is fav coffee and then the next field is 
# the list of coffee in a list
# We are keeping this selectbox under a variable to be able to further use it later

# Now let's use the user's selection and simply display it to the user in a message

st.write(f"You choose {coffee}. Excellent choice!")

# Now let's provide a success message once the user's selection is shown as text

st.success("Your coffee has been brewed")


# WIDGETS
# All the elements that we use in an ui are called widgets. Such as dropdpwn, textbox, checkbox, buttons etc.

import streamlit as st
from datetime import datetime, date

# We are creating a coffee maker app here

# Title should be there in any ui page
st.title("Coffee maker app")

# Now let's create a select box to select the coffee and then a button to make coffee

coffee = st.selectbox("Please choose your coffee type:", ["Black coffee", "Espresso", "Dalgona"])

if st.button("Make coffee"):
    # Once we have the button clicked we should get a success message
    st.success("Your coffee is being brewed!")

# Now let's say we need to add masala into our coffee
masala = st.checkbox("Add masala")

# So we want to provide a message to the user once he clicks the masala check box as masala added

if masala:
    st.write("Masala has been added to your coffee")

# Now let's test the radio buttons and we can use some coffee base to select for the user

coffee_type = st.radio("Select your coffee base: ", ["Water", "Milk"]) # The syntazx is same as select box
st.write(f"Selected base is {coffee_type}")

# Now let's add flavour using selectbox

flavour = st.selectbox("Select your flavour: ", ["Sugar", "Honey", "Cream"])

st.write(f"Selected flavour is {flavour}")

# Now let's check the slider by using the sugar quantity

sugar_spoons = st.slider("Please select your sugar quantity(spoons): ", 0, 5, 1) # Slider has ranges as we know
# which is o and 5 here and the default value should also be there which we have selected 1 here

# Now we can have a no. of inputs ranges which can start from 1 till may be 15

cups = st.number_input("Select the no. of cups of coffee you want: ", min_value=1, max_value=15, step=1)
# Here step helps us going in step by step manner to order like 1 then 2 then 3 etc till 15
st.write(f"Received order for {cups} of coffee")

# Now let's take pure text input using textbox

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Welcome {name}! Your coffee is on the way")

# Now we can check the dob here

dob = st.date_input("Enter your date of birth:")
st.write(f"You date of birth is {dob}")

# Let's check the age from dob

cur_date  = datetime.now().date()

st.write(f"The current date is: {cur_date}")

age = (cur_date-dob).days

year = age//365
days = age%365


st.write(f"You are {year} year and {days} days old")
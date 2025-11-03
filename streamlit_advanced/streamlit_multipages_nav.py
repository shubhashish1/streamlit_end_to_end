# To create multiple pages and navigate through those pages we will need a new library named streamlit-option-menu
# So go ahead and put it in the requirements.txt and install

import streamlit as st
from streamlit_option_menu import option_menu


# st.title("Streamlit option menu")

# Let's first insert the navigation menu in the side bar

# It requires 2 simple options one is the title and then the menu options

with st.sidebar:
    selected = option_menu(menu_title="Main Menu",
                           options=["Home", "Projects", "Contracts"],
                           icons=["house","book","envelope"],
                           menu_icon= "cast",
                           default_index= 0) # If we don't want then we can set the 
                                                                             # menu_title as None
# For icons for each page, we can have the icons list with only the icon names from https://icons.getbootstrap.com/
# website
# Here we can have a separate main menu icon as well as menu_icon
# We can also choose which page to be default displayed as default_index which for us by default 0

# For the navigations to different pages to be set horizontally we have to pass an argument orientation="horizontal"
# Let's see how to do that  
# 
selected = option_menu(menu_title=None,
                           options=["Home", "Projects", "Contracts"],
                           icons=["house","book","envelope"],
                           menu_icon= "cast",
                           default_index= 0,
                           orientation="horizontal")   


# 2. horizontal menu with custom style
selected = option_menu(
    menu_title=None,  # required
    options=["Home", "Projects", "Contact"],  # required
    icons=["house", "book", "envelope"],  # optional
    menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"},
        "nav-link": {
            "font-size": "25px",
            "text-align": "left",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "green"},
    },
)
    
if selected == "Home":
    st.header(f"Welcome to {selected} page!")
if selected == "Projects":
    st.header(f"Welcome to {selected} page!")
if selected == "Contracts":
    st.header(f"You are in {selected} page!")

# If we want to style anything different we can do that by using styles option in the option_menu

# GIT LINK FOR REFERENCE CODE:

# https://github.com/Sven-Bo/streamlit-navigation-menu
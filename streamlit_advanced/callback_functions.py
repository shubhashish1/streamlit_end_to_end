# Callbacks:

# Callbacks are the functions or operations we want to perform when we are doing one activity. Let's say
# we are fetching some response from llm on a button click, then at that tile we want to show a spinner

# It has 3 elements: widgets (activity), events(one event will occur), function(The callback function called in the event)

import streamlit as st

if "messages" not in st.session_state:
   st.session_state.messages = []

# if "user_input" not in st.session_state:
#    st.session_state.user_input = []



# Here we can put this if user_input and user_input!="": check as a callback function

def handle_userinput():
    user_input = st.session_state.user_input

    if user_input and user_input!="":
        # st.chat_message("user").markdown(user_input) # As we know here the first thing we need is role and then user_input
        # Now let's save this message in the session or memory
        st.session_state.messages.append({"role":"user", "content": user_input}) # Normal list append with the 
        # for mat needed like role and content

        bot_response = f"Echo: {user_input}" # Here we can have the llm and get the response from that
        # st.chat_message("ai").markdown(bot_response) # We don't need it as the messages will be repeatitive
        # means they will appear twice in the ui screens
        st.session_state.messages.append({"role":"ai", "content": bot_response})

    # Here messages is the key and further inside it for each message we have sub keys as role and content and the 
    # values for them as well

for message in st.session_state.messages:
    if message["role"]=="user":
        st.chat_message("user").markdown(message["content"])
    else:
        st.chat_message("ai").markdown(message["content"])

st.chat_input("Ask me anything", key = "user_input", on_submit=handle_userinput)
# st.write(st.session_state)
    
    # Here instead of the user_input as a variable at last we can have a new key in our session state created
    # as user_input as use that in the handle_userinput() function
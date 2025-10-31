# With streamlit there is a problem that if a user does something like clicking a button, using slider then what ever
# the activity he has done in that page before resets, for example if he has written a message and then using slider
# for a different activity in the same page or same ui then the streamlit page resets and in reruns from top to bottom
# again. This not only makes us to loose the user info but also makes some extra costing if we have any api call
# or llm call as it recalls everytime in each rerun.
# Hence to address this problem we have session_state and cacheing which helps us dealing with this issue.


# session_state is nothing but a python dict with multiple keys and values

# Example: if api_key not in st.session_state: We are checking if the api_key key is part of the session_state dict
# If not then we will add it like: st.session_state.api_key = api_value() : Here api_key is the key and api_value()
# is the value for the key

# Now with this waht happens let's say we use the same slider after the text in the text box, st will rerun but this
# time it will check if the text input is there in the session_state, if yes then it will not rerun this api_value()
# function and proceed further. If no, then it will run the api_value() function.

import streamlit as st

if "messages" not in st.session_state:
   st.session_state.messages = []

for message in st.session_state.messages:
   if message["role"]=="user":
      st.chat_message("user").markdown(message["content"])
   else:
      st.chat_message("ai").markdown(message["content"])


user_input = st.chat_input("Ask me anything")

if user_input and user_input!="":
   st.chat_message("user").markdown(user_input) # As we know here the first thing we need is role and then user_input
   # Now let's save this message in the session or memory
   st.session_state.messages.append({"role":"user", "content": user_input}) # Normal list append with the 
   # for mat needed like role and content

   bot_response = f"Echo: {user_input}" # Here we can have the llm and get the response from that
   st.chat_message("ai").markdown(bot_response)
   st.session_state.messages.append({"role":"ai", "content": bot_response})

   # Here messages is the key and further inside it for each message we have sub keys as role and content and the 
   # values for them as well
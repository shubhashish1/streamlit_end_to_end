# Here we will be checking how to build a conversational chatbot where we can have the user and ai messages
# as well as some icons to separate them. We will also store the response in memory.

import streamlit as st
import time

# The first thing is st.chat_message() : This will display the user and ai messages in the ui interface
# The next one is st.chat_input() : This is to take the user query in chat like format from ui

# Let's outline our full requirements:

# 1. We need something to take user input (st.chat_input())
# 2. We need to send that input to llm
# 3. We need to store that in memory (session_state())
# 4. We need to show the response from llm in the screen to user (st.chat_message())
# 5. We also need to store that response in memory

# user_input = st.chat_input("Ask me anything")
# response = f"You have asked: {user_input}"

# if user_input:
#    st.chat_message("user").write(user_input)

# Now let's tore our info we have received in memory for which we can use session state
# First we will check if session_state exists or not, if not we will create one

# We will be storing both the user message and the ai meesage in the memory (session_state). Hence we give 
# that user message and the ai meesage as messages

if "messages" not in st.session_state:
   st.session_state.messages = []

# As we know whenever we get any message from user or ai, we get it as first role which is either user or ai
# and then the query or conntent from the user or ai

# Now let's traverse through each message or the st.session_state.messages and show it to the user. 
# In this way we can store the messages in our memory as well as we can load our memory in ui using chat_message
# and show the entire conversation or all the user and ai conversation messages in the ui.

for message in st.session_state.messages:
   if message["role"]=="user":
      st.chat_message("user").markdown(message["content"])
   else:
      st.chat_message("ai").markdown(message["content"])

# Whenever we want a conversational base, then we need to have a streaming option for that so we can get the 
# query and responses in the go

# Straming

def generate_response(user_input):
    response = """This new chatbot is designed to respond all the user query asked and then also manage
                 the outcome in a desired manner. It takes the user query and then go to the llm and ask this query
                 set by user and then it gets the response from the llm about the query in the desired format that is
                 provided to the llm through a prompt. This is how the conversation works here in getting the response
                 for the user query in sreaming fashion token by token. Here the response is not waiting for the llm
                 to generate the whole response, rather it shows the response from llm gradually word by word or token
                 by token."""
    # Now we need to show this response in streaming manner to user.
    for token in response.split(" "):
      time.sleep(0.01)
      yield token + " "   
      # So here it takes the tokens first generated now and then pause/sleep for 0.01 sec and then again fetch the
      # next set of tokens and so on
      # Here yield plays the pivotal role and shows response word by word in stream from the token fetched


user_input = st.chat_input("Ask me anything")

# Now we have the user_input but we need to append it to our session_sate and then it will show the message
# asked by the user through chat_message

if user_input and user_input!="":
   st.chat_message("user").markdown(user_input) # As we know here the first thing we need is role and then user_input
   # Now let's save this message in the session or memory
   st.session_state.messages.append({"role":"user", "content": user_input}) # Normal list append with the 
   # for mat needed like role and content

   with st. chat_message("ai"):
      response_generator = generate_response(user_input)
      response = st.write_stream(response_generator) # So thos write_stream(output) writes the response in stream
#    st.chat_message("ai").markdown(bot_response)
   st.session_state.messages.append({"role":"ai", "content": response})
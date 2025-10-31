# FOR NON-SEALIZABLE OBJECTS WE USE CACHE_RESOURCE
# For example models where we need to provide some prediction result

import streamlit as st
import time

class AiModel:
    def __init__(self):
        # Load model
        time.sleep(5)
        self.model = "model"

    def prediction(self, input_data):
        return "Prediction"
    
@st.cache_resource(show_spinner="Loading model...")
def load_model():
    model = AiModel()
    return model

model = load_model()

if model:
    st.write("Model loaded")
st.button("Reload page")

# So here once the model is loaded it will be there in cache_resource and then once again called it will be pulled from
# cache_resource instead of relaoding the model itself again
# Also we have a class that loads the model here, which is not serializable and hence can't be stored in cache_data
# So here we are storing the copy of the object of the class instead
# So here everytime it won't take 5 secs and once cached it will fetch from cache

"""We also have one more component named ttl(time to leave) in cahc_resource
   This attribute takes time in sec and erases the cache from cache_resource once we hit the ttl.
   Best example of use is stock market data
   
   There is another option named max_entries in cache_resource which says the total no of entries can
   be done in cache_resource. If set to 100, then only 100 cache entries total are allowed.
   The moment we reach 100, once we try to store the 101 entry the 1st entry will be erased and the 101 will be
   100 and the 2nd one will be the first and so on"""
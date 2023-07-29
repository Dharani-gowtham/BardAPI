import bardapi
import streamlit as st
import os

# set your __Secure-1PSID value to key
token = 'ZAgjbF2rSZndOG-p48Y6qt-7zWBFD4AX9FL5WaGHeaEWPtQPPUUXpPmorUuevfy0OqeTKg.'

# set your input text
input_text = st.text_input("Enter the query to search in bard")
button = st.button("Search")
# Send an API request and get a response.

if button:
    response = bardapi.core.Bard(token).get_answer(input_text)
    st.write(response['content'])



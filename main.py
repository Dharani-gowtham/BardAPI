from bardapi import Bard
import streamlit as st
import os
import requests

# set your __Secure-1PSID value to key
os.environ['BARD_API_KEY'] = 'ZAgjbF2rSZndOG-p48Y6qt-7zWBFD4AX9FL5WaGHeaEWPtQPPUUXpPmorUuevfy0OqeTKg.'
token = 'xxxxx'

session = requests.Session()
session.headers = {
            "Host": "bard.google.com",
            "X-Same-Domain": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/91.0.4472.114 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Origin": "https://bard.google.com",
            "Referer": "https://bard.google.com/",
        }
session.cookies.set("__Secure-1PSID", os.getenv("_BARD_API_KEY"))

# set your input text
input_text = st.text_input("Enter the query to search in bard")
button = st.button("Search")
# Send an API request and get a response.

if button:
    bard = Bard(token=token, session=session, timeout=60)
    result = bard.get_answer(input_text)['content']
    # response = bardapi.core.Bard(token).get_answer(input_text)
    # st.write(response['content'])
    st.write(result)

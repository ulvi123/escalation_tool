# main.py
import streamlit as st
from inplay_page import show_page as show_inplay_page

# Navbar
st.title('My Streamlit App')

# Sidebar with nested options
st.sidebar.header('Choose affected product')
product = st.sidebar.selectbox(
    '',
    ('InPlay', 'Other Sportsbook Products', 'Sports Products', 'Live Video Streaming', 'Media: Gametracker/Smartstream')
)

if product == 'InPlay':
    show_inplay_page()
else:
    # Your code for the other pages goes here
    pass

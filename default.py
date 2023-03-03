import streamlit as st
from introduction import *


def default_page():
    st.warning("Enter the API key in sidebar to get started")
    intro()

# IMPORTS
import streamlit as st
import openai
from introduction import * 
from question_answering import *
from default import *


st.set_page_config(
    page_title="Openai model comparision",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

available_models = None
st.sidebar.title("Compare openai models")
st.sidebar.caption("A tool to compare the usage and performances of various openai models")
api_key = st.sidebar.text_input("Enter openai apikey", type="password")
st.sidebar.caption("Your API key will not be stored or shared with anyone")
# validating key
if api_key:
    openai.api_key = api_key
    try:
        available_models = openai.Engine.list()
        st.session_state["api_key"] = api_key
        print("API_connection successful")
    except:
        st.error("Invalid api key, please try again!")
        st.session_state["api_key"] = None
task_selection = None 
if available_models != None and st.session_state["api_key"] != None:
    st.write(" ")
    task_selection = st.sidebar.selectbox(
        "Select task",
        [   "Intro",
            "Chat", 
            "Question answering",
            "Image generation",
            "Speech to text",
            "Code Generation",
            "Content Moderation",
            "Get Numerical Embeddings",
            "GPT3 models",
            
        ],
    )

if task_selection == None: 
    default_page()
if task_selection == "Intro":
    intro()
elif task_selection == "Question answering":
    question_answering()

# IMPORTS
import streamlit as st
import openai
from introduction import * 
from question_answering import *
from default import *
from chat import * 
from image_gen import *
from speech_text import *
from code_gen import *
from content_mod import *
from num_embed import *
from gpt3 import *
from analytics import *


st.set_page_config(
    page_title="Openai model comparision",
    page_icon="https://abs.twimg.com/emoji/v1/72x72/1f916.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_ga() # for analytics purpose
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
            # TOBE IMPLEMENTED.
            # "Speech to text",
            # "Code Generation",
            # "Content Moderation",
            # "Get Numerical Embeddings",
            # "GPT3 models",
            
        ],
    )

if task_selection == None: 
    default_page()
if task_selection == "Intro":
    intro()
elif task_selection == "Question answering":
    question_answering()
elif task_selection == "Chat":
    chat_interface()
elif task_selection == "Image generation":
    image_gen_interface()
# elif task_selection == "Speech to text":
#     speech_text_interface()
# elif task_selection == "Code Generation":
#     code_gen_interface()
# elif task_selection == "Content Moderation":
#     content_mod_interface()
# elif task_selection == "Get Numerical Embeddings":
#     num_embed_interface()
# elif task_selection == "GPT3 models":
#     gpt_3_interface()
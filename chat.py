import streamlit as st 
from streamlit_chat import message 
import openai 
from nanoid import generate # unique ids for every messages.

def structurize_message(message_ , is_user):
    return {"role": "user" if is_user else "assistant", "content": message_}

def get_response(messages , model):
    chat_rep = openai.ChatCompletion.create(
        model = model ,
        messages = messages
    )
    return dict(chat_rep["choices"][0]["message"])


def chat_interface(): 
    model = st.selectbox("Select model", ["gpt-3.5-turbo", "gpt-3.5-turbo-0301"])
    st.markdown("<h3 style='text-align:center; color:grey;'> New Chat </h3>", unsafe_allow_html= True ) 
    message("Hey there! What question do you have for me?")

    # setting up session state for message history
    if "message_history" not in st.session_state:
        st.session_state.message_history = [] 
    print(st.session_state.message_history, "message history")
    for message_obj in st.session_state.message_history:
        print(message_obj)
        if message_obj.get("content",False): 
            message(message_obj["content"],is_user=True if message_obj["role"] == "user" else False, key = generate()) # display all the previous message
    
    placeholder = st.empty() # placeholder for latest message
    chat_input_form = st.form("chat_input" , clear_on_submit= True)
    input_ = chat_input_form.text_input(label = "message", key = "usermessage",value = '' , placeholder="Enter your message")
    # hide submit button 
    submit = chat_input_form.form_submit_button(label = "Send", )
    if input_:
        print(input_)
        st.session_state.message_history.append({"role":"user", "content":input_})
        # st.session_state["usermessage"] = ''
        response = get_response(st.session_state.message_history, model)
        st.session_state.message_history.append(response)
    
    if len(st.session_state.message_history)>= 2:
        with placeholder.container():
            message( st.session_state.message_history[-2]["content"], is_user=True if st.session_state.message_history[-2]["role"] == "user" else False, key = generate()) # display the latest message
            message( st.session_state.message_history[-1]["content"], is_user=True if st.session_state.message_history[-1]["role"] == "user" else False, key = generate()) # display the latest message



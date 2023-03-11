# import streamlit as st 

# def content_mod_interface():
#     st.title("Check content moderation (YET TO BE IMPLEMENTED.)")

import requests
import streamlit as st

def content_mod_interface(api_key):
    st.title("Check content moderation")
    input_text = st.text_input("Enter text to moderate:")
    model = st.selectbox("Select a model", ["text-moderation-stable", "text-moderation-latest"])
    if not input_text:
        return
    url = "https://api.openai.com/v1/moderations"
    headers = {"Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"}
    data = {"model": model,
            "input": input_text}
    response = requests.post(url, headers=headers, json=data)

    if response.ok:
        output = response.json()["results"][0]
        categories = output["categories"]
        category_scores = output["category_scores"]
        flagged = output["flagged"]
        table_data = {"Categories": categories,
                    "Category Scores": category_scores
                    }
        st.table(table_data)
        st.text(f"Flagged: {flagged}")
    else:
        error_message = response.json().get("error", {}).get("message", "Unknown error")
        st.write(f"Error: {error_message}") 

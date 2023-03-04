import streamlit as st 
import openai 
import requests


def generate_image(prompt): 
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url


def image_gen_interface():
    st.title("Image generation interface ")
    image_input_form = st.form(key='image_input_form')
    image_input = image_input_form.text_input(label='Enter the prompt for image generation:')
    image_input_submit = image_input_form.form_submit_button(label='Submit')
    if image_input_submit:
        image_url = generate_image(image_input)
        st.download_button(label="Download image", data=requests.get(image_url).content, file_name="output_image.png", mime="image/png")
        st.image(image_url)
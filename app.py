from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get response

def get_gemini_response(input_prompt, image_parts, user_prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([input_prompt, image_parts[0], user_prompt])
    return response.text
    

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        return None  # Return None instead of raising an error


##initialize our streamlit app

st.set_page_config(page_title="Invoice-Extractor-App")

st.header("Invoice Extractor App")
user_prompt = st.text_input("Ask a question about the invoice: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit = st.button("Get Answer")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

## If ask button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    if image_data:
        response = get_gemini_response(input_prompt, image_data, user_prompt)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.error("Please upload an image first.")

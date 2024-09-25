#   |                                                          |
# --+----------------------------------------------------------+--
#   |   Code by : ishanlagrawal                                |
#   |   Email   : ishan.agrawal77@gmail.com                    |
#   |   Github  : https://github.com/ishanlagrawal             |
# --+----------------------------------------------------------+--  
#   |        all posts #ishanlagrawal ,all views my own.       |
# --+----------------------------------------------------------+--
#   |                                                          |

# Import necessary libraries
import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure API key for Google Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini Vision model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Function to get response from Gemini Vision model
def get_gemini_response(prompt, image):
    if prompt:
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Vision: Image Interpretation and Smart Q&A")
st.subheader("Upload an image and ask questions for AI-powered insights.")

# Input prompt
prompt = st.text_input("Input Prompt:", key="input")

# Example prompts
st.write(
    [
        "Examples:",
        "Identify Image",
        "Transcribe Image",
        "Write Blog for Image",
        "Provide food recipe for Image",
        "Calculate approximate calories for food Image"
    ]
)

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "jfif"])
image = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

# Submit button
if st.button("Tell me about the Image"):
    if image:
        response = get_gemini_response(prompt, image)
        st.subheader("The Response is")
        st.markdown(response.replace('$', '\\$'))  # Escape special characters
    else:
        st.warning("Please upload an image to get a response.")

import streamlit as st
from gtts import gTTS
import tempfile
import os
from io import BytesIO

# Function to convert text to speech
def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    return audio_bytes.getvalue()

# Streamlit API
st.set_page_config(page_title="Text to Speech API", page_icon="🎤")

# Handle POST requests for API usage
if st.request_json():
    data = st.request_json()
    text_input = data.get("text", None)
    
    if text_input:
        audio_bytes = convert_text_to_speech(text_input)
        st.response.headers["Content-Type"] = "audio/mp3"
        st.response.content = audio_bytes
    else:
        st.error("No text provided.")
        st.response.status_code = 400

# UI for testing
st.title("Text to Speech API")
text_input = st.text_input("Enter text to convert to speech:")
if text_input and st.button("Convert"):
    audio_bytes = convert_text_to_speech(text_input)
    st.audio(audio_bytes, format='audio/mp3')
    st.success("Conversion successful!")

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

# UI for testing
st.title("Text to Speech API")

# Check if it's a POST request
if st.experimental_get_query_params().get("api", [""])[0] == "true":
    # Handle POST requests for API usage
    try:
        data = st.experimental_get_query_params()
        text_input = data.get("text", [None])[0]
        
        if text_input:
            audio_bytes = convert_text_to_speech(text_input)
            st.audio(audio_bytes, format='audio/mp3')
            st.success("Conversion successful!")
        else:
            st.error("No text provided.")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
else:
    # UI for manual testing
    text_input = st.text_input("Enter text to convert to speech:")
    if text_input and st.button("Convert"):
        audio_bytes = convert_text_to_speech(text_input)
        st.audio(audio_bytes, format='audio/mp3')
        st.success("Conversion successful!")

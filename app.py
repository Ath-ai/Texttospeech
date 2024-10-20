import streamlit as st
from gtts import gTTS
import os
import tempfile
import json

# Function to convert text to speech
def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    # Use a temporary file to store the audio
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
        tts.save(temp_file.name)
        return temp_file.name

# Streamlit API
st.set_page_config(page_title="Text to Speech API", page_icon="🎤")
st.title("Text to Speech API")

if st.experimental_get_query_params():  # Check if it's a GET request
    text_input = st.experimental_get_query_params().get("text", [None])[0]
    if text_input:
        audio_file_path = convert_text_to_speech(text_input)
        st.audio(audio_file_path, format='audio/mp3')

# Allow POST requests for API usage
if st.request.method == "POST":
    data = st.request.json()
    text_input = data.get("text")

    if text_input:
        audio_file_path = convert_text_to_speech(text_input)
        audio_url = audio_file_path.replace(" ", "%20")  # URL-encode spaces
        st.json({"audio_url": audio_url})
    else:
        st.json({"error": "No text provided."})

# Optional: Add UI for testing
text_input = st.text_input("Enter text to convert to speech:")
if text_input and st.button("Convert"):
    audio_file_path = convert_text_to_speech(text_input)
    st.success("Conversion successful!")
    st.audio(audio_file_path, format='audio/mp3')

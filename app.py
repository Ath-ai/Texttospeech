import streamlit as st
from gtts import gTTS
import os
import tempfile

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

text_input = st.text_input("Enter text to convert to speech:")

if text_input:
    audio_file_path = convert_text_to_speech(text_input)
    st.success("Conversion successful!")
    st.audio(audio_file_path, format='audio/mp3')

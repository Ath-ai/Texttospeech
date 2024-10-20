import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

# Function to convert text to speech
def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return base64.b64encode(audio_bytes.read()).decode()

# Streamlit API
st.set_page_config(page_title="Text to Speech API", page_icon="🎤")

# UI for testing
st.title("Text to Speech API")

# Create a form for text input
with st.form("text_to_speech_form"):
    text_input = st.text_input("Enter text to convert to speech:")
    submit_button = st.form_submit_button("Convert")

if submit_button and text_input:
    audio_base64 = convert_text_to_speech(text_input)
    st.audio(f"data:audio/mp3;base64,{audio_base64}", format='audio/mp3')
    st.success("Conversion successful!")
    
    # Display the base64 encoded audio for API use
    st.json({"audio": audio_base64})
elif submit_button:
    st.error("Please enter some text to convert.")

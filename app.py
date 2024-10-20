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

# Check if it's an API request
if "api" in st.experimental_get_query_params():
    # Handle API requests
    try:
        text_input = st.experimental_get_query_params().get("text", [""])[0]
        
        if text_input:
            audio_base64 = convert_text_to_speech(text_input)
            st.json({"audio": audio_base64})
        else:
            st.json({"error": "No text provided."})
    except Exception as e:
        st.json({"error": str(e)})
else:
    # UI for manual testing
    text_input = st.text_input("Enter text to convert to speech:")
    if text_input and st.button("Convert"):
        audio_base64 = convert_text_to_speech(text_input)
        st.audio(f"data:audio/mp3;base64,{audio_base64}", format='audio/mp3')
        st.success("Conversion successful!")

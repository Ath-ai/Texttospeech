import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

# Function to convert text to speech
def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    return audio_data

# Streamlit API
st.title("Text to Speech API")

# Handle POST requests
if st.request_method == "POST":
    # Parse the JSON body
    data = st.experimental_get_query_params()
    text_input = st.experimental_get_query_params().get("text", [""])[0]

    if not text_input:
        st.json({"error": "No text provided."})
    else:
        audio_data = convert_text_to_speech(text_input)
        audio_data.seek(0)  # Rewind to start of file

        # Convert the audio to base64 to send over HTTP
        audio_base64 = base64.b64encode(audio_data.read()).decode("utf-8")
        st.json({"audio_base64": audio_base64})

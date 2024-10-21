import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

# Function to convert text to speech
def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)  # Rewind to start of the BytesIO buffer
    return audio_data

# Streamlit app title
st.title("Text to Speech API")

# Get query parameters
params = st.experimental_get_query_params()

# Extract the 'text' parameter from query params
text_input = params.get("text", [None])[0]

if text_input:
    # Convert the text to speech
    audio_data = convert_text_to_speech(text_input)

    # Convert the audio data to a base64 string
    audio_base64 = base64.b64encode(audio_data.read()).decode("utf-8")
    
    # Send JSON response with base64 encoded audio
    st.json({"audio_base64": audio_base64})
else:
    st.json({"error": "No text provided. Please send a 'text' parameter."})

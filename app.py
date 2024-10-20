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

# Get text input from query parameter
query_params = st.experimental_get_query_params()
text_input = query_params.get("text", [""])[0]

if text_input:
    audio_base64 = convert_text_to_speech(text_input)
    st.audio(f"data:audio/mp3;base64,{audio_base64}", format='audio/mp3')
    st.success("Conversion successful!")
    
    # Display the base64 encoded audio for API use
    st.json({"audio": audio_base64})
else:
    st.info("Enter text in the URL query parameter 'text' to convert to speech.")
    st.markdown("Example: `?text=Hello, world!`")

# Add a text input for manual testing
manual_input = st.text_input("Or enter text here to convert:")
if st.button("Convert") and manual_input:
    audio_base64 = convert_text_to_speech(manual_input)
    st.audio(f"data:audio/mp3;base64,{audio_base64}", format='audio/mp3')
    st.success("Conversion successful!")
    st.json({"audio": audio_base64})

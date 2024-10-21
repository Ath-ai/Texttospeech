import streamlit as st
from gtts import gTTS
import base64
from io import BytesIO

# Configure Streamlit
st.set_page_config(page_title="Text-to-Speech API")

def text_to_speech(text, language='en'):
    try:
        tts = gTTS(text=text, lang=language)
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_b64 = base64.b64encode(audio_buffer.getvalue()).decode()
        return {"status": "success", "audio": audio_b64}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Get query parameters
query_params = st.experimental_get_query_params()
text = query_params.get("text", [""])[0]
language = query_params.get("language", ["en"])[0]

if text:
    result = text_to_speech(text, language)
    st.json(result)
else:
    st.json({
        "status": "error",
        "message": "Please provide text parameter"
    })

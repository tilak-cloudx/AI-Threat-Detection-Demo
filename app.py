import streamlit as st
import wikipedia
from gtts import gTTS
import tempfile
import base64
from ml_model import predict_threat

st.set_page_config(page_title="AI Threat Detection Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 AI Threat Detection Chatbot")

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    st.write("Configure the chatbot here.")

# --- Chat input ---
st.markdown("""
    <style>
    .chat-input-wrapper {
        position: relative;
        width: 100%;
    }
    .chat-icons {
        position: absolute;
        right: 8px;
        top: 50%;
        transform: translateY(-50%);
        cursor: pointer;
        font-size: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Input area ---
user_input = st.text_input("Ask me anything about Wikipedia or Threats", placeholder="Type here...")

if user_input:
    st.write(f"**You:** {user_input}")
    
    # --- Try ML prediction ---
    try:
        # Dummy example: expecting numeric features in a dict
        features = {"feature1": 0.5, "feature2": 1.2}  # Replace with actual feature extraction
        prediction = predict_threat(features)
        st.write(f"**ML Model Prediction:** {prediction}")
    except Exception as e:
        st.write(f"ML Prediction Error: {e}")

    # --- Wikipedia query ---
    try:
        summary = wikipedia.summary(user_input, sentences=2)
        st.write(f"**Wikipedia:** {summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        st.write(f"Disambiguation Error: {e}")
    except wikipedia.exceptions.PageError:
        st.write("Page not found.")
    
    # --- Text-to-speech ---
    try:
        tts = gTTS(summary)
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(tmp_file.name)
        audio_file = open(tmp_file.name, "rb")
        st.audio(audio_file.read(), format="audio/mp3")
    except Exception as e:
        st.write(f"TTS Error: {e}")

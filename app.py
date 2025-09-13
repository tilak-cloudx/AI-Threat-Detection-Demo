import streamlit as st
import wikipedia
from gtts import gTTS
import tempfile
from ml_model import predict_threat

st.set_page_config(page_title="AI Threat Detection Chatbot", page_icon="🤖", layout="centered")
st.title("🤖 AI Threat Detection Chatbot")

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    st.write("Configure the chatbot here.")

# --- User Input ---
user_input = st.text_input("Ask me anything about Wikipedia or Threats", placeholder="Type here...")

if user_input:
    st.write(f"**You:** {user_input}")
    
    # --- ML Prediction ---
    try:
        # Dummy example: replace with your actual feature extraction
        features = {"feature1": 0.5, "feature2": 1.2}
        prediction = predict_threat(features)
        st.write(f"**ML Model Prediction:** {prediction}")
    except Exception as e:
        st.write(f"ML Prediction Error: {e}")

    # --- Wikipedia Lookup ---
    try:
        summary = wikipedia.summary(user_input, sentences=2)
        st.write(f"**Wikipedia:** {summary}")
    except wikipedia.exceptions.DisambiguationError as e:
        st.write(f"Disambiguation Error: {e}")
    except wikipedia.exceptions.PageError:
        st.write("Page not found.")

    # --- Text-to-Speech ---
    try:
        tts = gTTS(summary)
        tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(tmp_file.name)
        audio_file = open(tmp_file.name, "rb")
        st.audio(audio_file.read(), format="audio/mp3")
    except Exception as e:
        st.write(f"TTS Error: {e}")

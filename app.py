import streamlit as st
import pandas as pd
import plotly.express as px
from ml_model import predict_threat
from phishing import check_url
from database import init_db, add_threat, get_threats
from utils import generate_fake_traffic

st.set_page_config(page_title="AI Threat Detection", page_icon="🛡️", layout="wide")

# Initialize database
init_db()

st.title("🛡️ AI-Powered Threat Detection & Prevention")

# Sidebar Navigation
menu = st.sidebar.radio("Navigate", ["Dashboard", "Phishing Detector", "Simulate Traffic", "Threat Logs"])

# Dashboard
if menu == "Dashboard":
    st.subheader("📊 Threat Overview")
    threats = get_threats()
    df = pd.DataFrame(threats, columns=["ID", "IP", "Protocol", "Port", "Status", "Timestamp"])
    if not df.empty:
        fig = px.pie(df, names="Status", title="Threat Distribution")
        st.plotly_chart(fig)
        st.dataframe(df)
    else:
        st.info("No threats detected yet.")

# Phishing Detector
elif menu == "Phishing Detector":
    st.subheader("🕵️ Phishing URL Checker")
    url = st.text_input("Enter a URL:")
    if st.button("Check"):
        result = check_url(url)
        st.write(f"Result: **{result}**")

# Simulate Traffic
elif menu == "Simulate Traffic":
    st.subheader("🚦 Simulate Network Traffic")
    traffic = generate_fake_traffic()
    st.json(traffic)

    if st.button("Run Detection"):
        result = predict_threat({
            "ip": traffic["ip"],
            "protocol": 1 if traffic["protocol"]=="TCP" else 2,
            "port": traffic["port"],
            "packet_size": traffic["packet_size"]
        })
        add_threat(traffic["ip"], traffic["protocol"], traffic["port"], result)
        st.success(f"AI Prediction: {result}")

# Threat Logs
elif menu == "Threat Logs":
    st.subheader("📋 Threat Logs")
    threats = get_threats()
    df = pd.DataFrame(threats, columns=["ID", "IP", "Protocol", "Port", "Status", "Timestamp"])
    st.dataframe(df)

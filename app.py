import streamlit as st

st.set_page_config(page_title="MedSafe AI", layout="centered")

st.title("🩺 MedSafe AI – Medical Safety Assistant")
st.write("Educational AI tool for medicine safety & symptom awareness")

st.divider()

st.header("💊 Medicine Interaction Checker")
st.text_input("Enter medicine names (comma-separated)")

st.divider()

st.header("🩹 Symptom & Side-Effect Guidance")
st.text_area("Describe your symptoms")

st.caption(
    "⚠️ Disclaimer: This tool provides educational information only and does not replace professional medical advice."
)

import streamlit as st

st.set_page_config(page_title="MedSafe AI", layout="centered")

st.title("🩺 MedSafe AI – Medical Safety Assistant")
st.write("Educational AI tool for medicine safety & symptom awareness")

st.divider()

st.header("💊 Medicine Interaction Checker")
medicines = st.text_input("Enter medicine names (comma-separated)")

if st.button("Check Medicine Safety"):
    if medicines:
        st.warning("⚠️ Possible interaction detected")
        st.write(
            "AI Analysis: Some medicines may have mild interactions. "
            "Please consult a healthcare professional before combining them."
        )
        st.info("Risk Level: Medium")
    else:
        st.error("Please enter at least one medicine name.")

st.divider()

st.header("🩹 Symptom & Side-Effect Guidance")
symptoms = st.text_area("Describe your symptoms")

if st.button("Analyze Symptoms"):
    if symptoms:
        st.info(
            "AI Guidance: These symptoms are usually mild but should be monitored. "
            "If symptoms worsen, seek medical advice."
        )
        st.success("Urgency Level: Low")
    else:
        st.error("Please describe your symptoms.")

st.caption(
    "⚠️ Disclaimer: This tool provides educational information only and does not replace professional medical advice."
)

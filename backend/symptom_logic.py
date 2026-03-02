# Milestone 2: Core Logic
# Module: Symptom & Side-Effect Analysis

def analyze_symptoms(symptom_text):
    """
    Analyzes symptoms and provides risk-based guidance.

    Parameters:
        symptom_text (str): Description of symptoms

    Returns:
        dict: Risk level and guidance message
    """

    symptoms = symptom_text.lower()

    high_risk_keywords = [
        "chest pain", "shortness of breath", "severe bleeding",
        "fainting", "unconscious", "seizure"
    ]

    medium_risk_keywords = [
        "fever", "vomiting", "nausea", "dizziness",
        "headache", "rash"
    ]

    for word in high_risk_keywords:
        if word in symptoms:
            return {
                "risk_level": "High",
                "guidance": "Symptoms may indicate a serious condition. Seek immediate medical attention."
            }

    for word in medium_risk_keywords:
        if word in symptoms:
            return {
                "risk_level": "Medium",
                "guidance": "Symptoms should be monitored. Consider consulting a healthcare professional."
            }

    return {
        "risk_level": "Low",
        "guidance": "No critical symptoms detected. Maintain observation and general care."
    }

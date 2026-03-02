# Milestone 2: Core Logic
# Module: AI-Style Explanation Generator (Mocked)

def generate_explanation(context, risk_level):
    """
    Generates an AI-style explanation based on context and risk level.

    Parameters:
        context (str): Either 'medicine' or 'symptom'
        risk_level (str): Low / Medium / High

    Returns:
        str: Human-friendly explanation
    """

    explanations = {
        "medicine": {
            "Low": (
                "Based on available information, no major medicine interactions were identified. "
                "This does not guarantee complete safety, so professional advice is recommended."
            ),
            "Medium": (
                "Some medicines may interact mildly. While this is usually manageable, "
                "monitoring and consultation with a healthcare professional is advised."
            ),
            "High": (
                "A potentially serious medicine interaction was detected. "
                "It is strongly recommended to seek medical guidance before proceeding."
            )
        },
        "symptom": {
            "Low": (
                "The symptoms described appear to be mild. General care and observation "
                "are usually sufficient."
            ),
            "Medium": (
                "The symptoms may require attention. Monitoring and consulting a healthcare "
                "professional can help prevent complications."
            ),
            "High": (
                "The symptoms suggest a potentially serious condition. "
                "Immediate medical attention is strongly recommended."
            )
        }
    }

    return explanations.get(context, {}).get(
        risk_level,
        "Insufficient information available to generate an explanation."
    )

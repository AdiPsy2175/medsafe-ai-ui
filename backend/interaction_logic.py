# Milestone 2: Core Logic
# Module: Medicine Interaction Checker

def check_medicine_interaction(medicines):
    """
    Checks for known interactions between medicines.
    
    Parameters:
        medicines (list): List of medicine names (strings)
    
    Returns:
        dict: Interaction result with risk level and message
    """

    # Normalize medicine names
    meds = [m.strip().lower() for m in medicines if m.strip()]

    # Simple rule-based interaction database
    interaction_rules = {
        frozenset(["paracetamol", "ibuprofen"]): {
            "risk": "Medium",
            "message": "Paracetamol and Ibuprofen can be taken together, but prolonged combined use should be monitored."
        },
        frozenset(["aspirin", "ibuprofen"]): {
            "risk": "High",
            "message": "Aspirin and Ibuprofen together may increase the risk of gastrointestinal bleeding."
        }
    }

    # Check interactions
    for rule, info in interaction_rules.items():
        if rule.issubset(set(meds)):
            return {
                "risk_level": info["risk"],
                "description": info["message"]
            }

    # Default response
    return {
        "risk_level": "Low",
        "description": "No known major interactions found. Always consult a healthcare professional."
    }

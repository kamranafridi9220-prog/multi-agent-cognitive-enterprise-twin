class ExecutiveVotingEngine:
    """
    Simulates executive voting across CFO, CMO, COO, and CRO agents.
    """

    def generate_votes(
        self,
        decision_score,
        risk_level,
        estimated_impact,
        health_score=None,
        shock_severity=None
    ):
        votes = {}

        # CFO logic
        if decision_score >= 70 and estimated_impact >= 0:
            votes["CFO"] = {
                "vote": "YES",
                "reason": "The decision appears financially viable based on the current decision score and impact."
            }
        elif decision_score >= 55:
            votes["CFO"] = {
                "vote": "CAUTION",
                "reason": "The financial case is acceptable, but stronger validation is needed before full approval."
            }
        else:
            votes["CFO"] = {
                "vote": "NO",
                "reason": "The financial risk appears too high for immediate approval."
            }

        # CMO logic
        if estimated_impact > 0:
            votes["CMO"] = {
                "vote": "YES",
                "reason": "The scenario suggests potential commercial upside or customer growth opportunity."
            }
        else:
            votes["CMO"] = {
                "vote": "CAUTION",
                "reason": "The market impact is unclear and requires further customer validation."
            }

        # COO logic
        if risk_level in ["Low", "Moderate", "Medium"]:
            votes["COO"] = {
                "vote": "YES",
                "reason": "The operational risk appears manageable with current business capacity."
            }
        else:
            votes["COO"] = {
                "vote": "CAUTION",
                "reason": "Operational execution risk should be reviewed before approval."
            }

        # CRO logic
        if risk_level == "Low":
            votes["CRO"] = {
                "vote": "YES",
                "reason": "Risk exposure appears controlled."
            }
        elif risk_level in ["Moderate", "Medium"]:
            votes["CRO"] = {
                "vote": "CAUTION",
                "reason": "Risk is manageable but should be monitored carefully."
            }
        else:
            votes["CRO"] = {
                "vote": "NO",
                "reason": "Risk exposure is too high without mitigation."
            }

        yes_votes = sum(1 for v in votes.values() if v["vote"] == "YES")
        caution_votes = sum(1 for v in votes.values() if v["vote"] == "CAUTION")
        no_votes = sum(1 for v in votes.values() if v["vote"] == "NO")

        if yes_votes >= 3:
            final_result = "Approved"
        elif no_votes >= 2:
            final_result = "Rejected"
        else:
            final_result = "Conditional Approval"

        confidence = min(
            95,
            max(
                45,
                int((decision_score * 0.6) + (yes_votes * 10) - (no_votes * 8))
            )
        )

        return {
            "votes": votes,
            "yes_votes": yes_votes,
            "caution_votes": caution_votes,
            "no_votes": no_votes,
            "final_result": final_result,
            "confidence": confidence
        }

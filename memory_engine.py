class EnterpriseMemoryEngine:
    def create_memory_record(
        self,
        dataset_name,
        selected_metric,
        decision_score,
        decision_classification,
        revenue_view,
        risk_view,
        ceo_decision
    ):
        return {
            "dataset_name": dataset_name,
            "selected_metric": selected_metric,
            "decision_score": decision_score,
            "decision_classification": decision_classification,
            "revenue_view": revenue_view,
            "risk_view": risk_view,
            "ceo_decision": ceo_decision
        }

    def summarize_memory(self, memory_record):
        return (
            f"For dataset '{memory_record['dataset_name']}', the Cognitive Enterprise Twin analysed "
            f"'{memory_record['selected_metric']}' and generated a decision score of "
            f"{memory_record['decision_score']}/100, classified as "
            f"{memory_record['decision_classification']}."
        )

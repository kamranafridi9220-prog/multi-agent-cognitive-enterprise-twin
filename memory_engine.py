import json
from datetime import datetime


class EnterpriseMemoryEngine:
    def __init__(self, memory_file="enterprise_memory.json"):
        self.memory_file = memory_file

    def load_memory(self):
        try:
            with open(self.memory_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_memory(self, memory_data):
        with open(self.memory_file, "w") as file:
            json.dump(memory_data, file, indent=4)

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
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "dataset_name": dataset_name,
            "selected_metric": selected_metric,
            "decision_score": decision_score,
            "decision_classification": decision_classification,
            "revenue_view": revenue_view,
            "risk_view": risk_view,
            "ceo_decision": ceo_decision
        }

    def add_memory_record(self, memory_record):
        memory_data = self.load_memory()
        memory_data.append(memory_record)
        self.save_memory(memory_data)
        return memory_data

    def summarize_memory(self, memory_record):
        return (
            f"For dataset '{memory_record['dataset_name']}', the Cognitive Enterprise Twin analysed "
            f"'{memory_record['selected_metric']}' and generated a decision score of "
            f"{memory_record['decision_score']}/100, classified as "
            f"{memory_record['decision_classification']}."
        )

    def summarize_historical_memory(self):
        memory_data = self.load_memory()

        if not memory_data:
            return "No historical enterprise memory records found yet."

        total_records = len(memory_data)
        latest_record = memory_data[-1]

        return (
            f"The Enterprise Memory currently contains {total_records} historical decision record(s). "
            f"The latest analysis focused on '{latest_record['selected_metric']}' from dataset "
            f"'{latest_record['dataset_name']}', with a decision score of "
            f"{latest_record['decision_score']}/100."
        )

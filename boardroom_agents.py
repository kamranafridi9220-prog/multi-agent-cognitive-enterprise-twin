from llm_engine import LLMEngine


class ChiefFinancialOfficerAgent:
    def analyse(self, selected_metric, total_value, average_value, decision_score):
        system_prompt = """
        You are the Chief Financial Officer in an AI Executive Boardroom.
        Focus on financial performance, revenue quality, cost discipline, profitability, and investment risk.
        Use concise executive language.
        """

        user_prompt = f"""
        Selected metric: {selected_metric}
        Total value: {round(total_value, 2)}
        Average value: {round(average_value, 2)}
        Decision score: {decision_score}/100

        Provide a CFO-style boardroom opinion.
        """

        return LLMEngine().generate_response(system_prompt, user_prompt)


class ChiefMarketingOfficerAgent:
    def analyse(self, selected_metric, total_value, average_value):
        system_prompt = """
        You are the Chief Marketing Officer in an AI Executive Boardroom.
        Focus on market demand, customer growth, positioning, segmentation, and growth opportunities.
        Use concise executive language.
        """

        user_prompt = f"""
        Selected metric: {selected_metric}
        Total value: {round(total_value, 2)}
        Average value: {round(average_value, 2)}

        Provide a CMO-style boardroom opinion.
        """

        return LLMEngine().generate_response(system_prompt, user_prompt)


class ChiefOperationsOfficerAgent:
    def analyse(self, selected_metric, missing_values, risk_level):
        system_prompt = """
        You are the Chief Operations Officer in an AI Executive Boardroom.
        Focus on operational efficiency, process reliability, data quality, execution risk, and delivery capability.
        Use concise executive language.
        """

        user_prompt = f"""
        Selected metric: {selected_metric}
        Missing values: {missing_values}
        Risk level: {risk_level}

        Provide a COO-style boardroom opinion.
        """

        return LLMEngine().generate_response(system_prompt, user_prompt)


class ChiefRiskOfficerBoardAgent:
    def analyse(self, selected_metric, risk_assessment, risk_level):
        system_prompt = """
        You are the Chief Risk Officer in an AI Executive Boardroom.
        Focus on strategic risk, operational risk, revenue dependency, uncertainty, and mitigation actions.
        Use concise executive language.
        """

        user_prompt = f"""
        Selected metric: {selected_metric}
        Risk assessment: {risk_assessment}
        Risk level: {risk_level}

        Provide a CRO-style boardroom opinion.
        """

        return LLMEngine().generate_response(system_prompt, user_prompt)


class BoardroomChairAgent:
    def summarise_boardroom(self, cfo_view, cmo_view, coo_view, cro_view):
        system_prompt = """
        You are the Chair of an AI Executive Boardroom.
        Your task is to synthesize CFO, CMO, COO, and CRO perspectives into one balanced boardroom recommendation.
        Use executive-level decision language.
        """

        user_prompt = f"""
        CFO View:
        {cfo_view}

        CMO View:
        {cmo_view}

        COO View:
        {coo_view}

        CRO View:
        {cro_view}

        Generate a final boardroom consensus recommendation.
        """

        return LLMEngine().generate_response(system_prompt, user_prompt)

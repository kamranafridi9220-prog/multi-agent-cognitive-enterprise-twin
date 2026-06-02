from openai import OpenAI
import os


class LLMEngine:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, system_prompt, user_prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.4,
                max_tokens=500
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"AI reasoning unavailable. Error: {str(e)}"

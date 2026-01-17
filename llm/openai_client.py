# llm/openai_client.py

import os
from dotenv import load_dotenv
from openai import OpenAI, RateLimitError

from cost.token_counter import estimate_tokens

load_dotenv()


class OpenAIClient:
    def __init__(
        self,
        model: str = "gpt-4o-mini",
        cost_per_1k_tokens: float = 0.00015
    ):
        self.model = model
        self.cost_per_1k_tokens = cost_per_1k_tokens
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate(self, prompt: str):
        input_tokens = estimate_tokens(prompt)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )

            output_text = response.choices[0].message.content
            output_tokens = estimate_tokens(output_text)

            cost = ((input_tokens + output_tokens) / 1000) * self.cost_per_1k_tokens

            return {
                "text": output_text,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "cost": cost
            }

        except RateLimitError:
            # Graceful fallback (enterprise behavior)
            return {
                "text": "[OPENAI QUOTA EXCEEDED — FALLBACK RESPONSE]",
                "input_tokens": input_tokens,
                "output_tokens": 0,
                "cost": 0.0
            }

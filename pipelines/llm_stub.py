# pipelines/llm_stub.py

class DummyLLM:
    """
    Stub LLM that matches the real LLM interface.
    """
    def generate(self, prompt: str):
        return {
            "text": "[LLM OUTPUT PLACEHOLDER]",
            "input_tokens": 0,
            "output_tokens": 0,
            "cost": 0.0
        }

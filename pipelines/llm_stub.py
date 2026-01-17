# pipelines/llm_stub.py

class DummyLLM:
    """
    Temporary stub LLM for pipeline testing.
    Replace with OpenAI / Gemini / Claude later.
    """
    def generate(self, prompt: str) -> str:
        return "[LLM OUTPUT PLACEHOLDER]"

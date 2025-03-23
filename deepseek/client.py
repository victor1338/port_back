import openai
from .api_config import DEEPSEEK_API_KEY, DEEPSEEK_API_BASE_URL 

class DeepseekClient:
    def __init__(self):
        self.client = openai.OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url=DEEPSEEK_API_BASE
        )

    def chat_completion(self, messages, model="deepseek-chat", **kwargs):
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                **kwargs
            )
            return response
        except Exception as e:
            raise Exception(f"Deepseek API error: {str(e)}") 
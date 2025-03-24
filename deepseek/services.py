import requests
from .api_config import DEEPSEEK_API_KEY, DEEPSEEK_API_BASE_URL 
from openai import OpenAI
class DeepSeekService:
    def __init__(self):
        self.api_key = DEEPSEEK_API_KEY
        self.base_url = DEEPSEEK_API_BASE_URL
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def generate_chat_response(self, prompt, model="deepseek-chat"):  # adjust model name as needed
        try:
            client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
            )

            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.model_dump()
        except Exception as e:
            raise Exception(f"API call failed: {str(e)}")
import os
from dotenv import load_dotenv

load_dotenv()

# Load API configuration from environment variables
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
DEEPSEEK_API_BASE_URL = os.getenv('DEEPSEEK_API_BASE_URL', 'https://api.deepseek.com/v1')  # adjust the URL as per DeepSeek's documentation 
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
#
url = "https://api.openai.com/v1/chat/completions"

# request headers
headers = {
    "content-type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}

# request data
data = {
    "model":"gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "What is the purpose of life?"}
    ]
}

# make request
response = requests.post(url, headers=headers, data=json.dumps(data))
if response.status_code == 200:
    answer=response.json()
    print("AI response:",answer['choices'][0]['message']['content'].strip())
else:
    print("Error:",response.status_code)
    print(response.text)
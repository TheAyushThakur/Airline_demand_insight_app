import os
import requests
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

def generate_insight_summary(routes_dict, trends_dict):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "Summarize airline trends and routes insightfully."},
            {"role": "user", "content": f"Routes: {routes_dict}\nTrends: {trends_dict}"}
        ],
        "temperature": 0.5
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    print("AI API Response:", result) 

    if "choices" not in result:
        raise ValueError(f"AI API did not return 'choices': {result}")

    return result['choices'][0]['message']['content']

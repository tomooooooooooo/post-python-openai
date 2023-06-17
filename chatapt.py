import os

import openai
from dotenv import load_dotenv

load_dotenv(override=True)
load_dotenv(".env")
#APIキーの設定
openai.api_key =os.environ["OPENAI_API_KEY"]

#Chatgptにリクエストする
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
    {
        "role": "user",
        "content": "久保建英はすごいの？"
    },
    ],
)

print(response.choices[0]["message"]["content"].strip())
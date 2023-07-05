import os
import sys
import openai
from dotenv import load_dotenv


def main():
    print('入力メッセージ：', sys.argv[1])

    load_dotenv()
    openai.api_key = os.getenv('API_KEY')
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": sys.argv[1]},
        ]
    )
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
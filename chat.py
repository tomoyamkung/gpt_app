import sys
import openai

def main():
    print('入力メッセージ：', sys.argv[1])

    openai.api_key = ''
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
import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


def main():
    load_dotenv()
    api_key = os.environ.get("API_KEY")
    if api_key is None:
        raise RuntimeError("API_KEY not set")
    api_url = os.environ.get("API_URL")
    if api_url is None:
        raise RuntimeError("API_URL not set")
    client = OpenAI(
        base_url=api_url,
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()
    # Now we can access `args.user_prompt

    response = client.chat.completions.create(
        model="huihui-gemma-4-12b-it-abliterated",
        messages=[
            {
                "role": "user",
                "content": args.user_prompt,
            }
        ],
    )
    if response.usage:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()

import os
import sys
import argparse

from dotenv import load_dotenv
from google import genai

def main():
    parser = argparse.ArgumentParser(prog="BoxBot", description="A Python CLI tool to talk to Gemini 2.0 Flash")
    parser.add_argument("prompt", type=str)
    parser.add_argument("-v", "--verbose", action='store_true')
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"

    args = parser.parse_args()
    contents = args.prompt

    answer = client.models.generate_content(model=model, contents=contents)
    print(f"Gemini Response: {answer.text}")
    if args.verbose:
        print(f"User prompt: {contents}")
        print(f"Prompt tokens: {answer.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {answer.usage_metadata.candidates_token_count}")

if __name__ == '__main__':
    main()
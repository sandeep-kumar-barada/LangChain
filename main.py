import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from project!")
    print("OpenAI Key:", os.getenv("openai_key"))


if __name__ == "__main__":
    main()

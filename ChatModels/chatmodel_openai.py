from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

if load_dotenv():
    key = os.getenv('OPENAI_API_KEY')
    prompt = os.getenv('USER_PROMPT1')
    model = ChatOpenAI(
        api_key = key,
        model='gpt-4.1-nano-2025-04-14',
        max_retries=2,
        max_completion_tokens=250
    )

    try:
        result = model.invoke(prompt)
        print(prompt)
        print(result.content)
    except Exception as ex:
        print(f"An error occoured:[>>>{ex}]")
else:
    print("Failed to load environment variables")
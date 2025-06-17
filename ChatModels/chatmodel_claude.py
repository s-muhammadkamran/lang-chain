from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

if load_dotenv():
    key = os.getenv('CLAUDE_API_KEY')
    prompt = os.getenv('USER_PROMPT')
    model = ChatAnthropic(
        api_key = key, 
        model='claude-opus-4-20250514',
        max_retries=2,
        max_tokens_to_sample=200
    )

    try:
        result = model.invoke(prompt)
        print(prompt)
        print(result.content)
    except Exception as ex:
        print(f"An error occoured:[>>>{ex}]")
else:
    print("Failed to load environment variables")
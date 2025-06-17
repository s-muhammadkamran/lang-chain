from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

if load_dotenv():
    key = os.getenv('OPENAI_API_KEY')
    model = OpenAI(
        api_key = key, 
        model='gpt-3.5-turbo',
        max_retries=2,
        max_tokens=250
    )
    
    try:
        result = model.invoke('What is happening in the ME?')
        print(result)
    except Exception as ex:
        print(f"An error occoured:[>>>{ex}]")
else:
    print("Failed to load environment variables")
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

if load_dotenv():
    key = os.getenv('GEMNI_API_KEY')
    prompt = os.getenv('USER_PROMPT1')    
    model = ChatGoogleGenerativeAI(
        api_key = key, 
        model='gemini-2.0-flash',
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
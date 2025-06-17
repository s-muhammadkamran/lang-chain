from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

if load_dotenv():
    hf_token = os.getenv('HUGGING_FACE_TOKEN')
    prompt = os.getenv('USER_PROMPT2')

    end_point = HuggingFaceEndpoint(
        repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task = "text-generation",        
        huggingfacehub_api_token = hf_token
    )

    model = ChatHuggingFace(llm = end_point)

    try:        
        result = model.invoke(prompt)
        print(prompt)
        print(result)
    except Exception as ex:
        print(f"An error occoured:[>>>{repr(ex)}]")
else:
    print("Failed to load environment variables")
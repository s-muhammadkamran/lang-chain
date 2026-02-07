from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os

if load_dotenv():
    prompt = os.getenv('USER_PROMPT1')
    os.environ['HF_HOME'] = os.getenv('HUGGING_FACE_LOCAL_CACHE_LOC')

    try:
        llm = HuggingFacePipeline.from_model_id(
            model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            task="text-generation",            
            pipeline_kwargs = {
                "temperature": 0.1,
                "max_new_tokens": 100
            }
        )
        model = ChatHuggingFace(llm = llm)
        result = model.invoke(prompt)

        print(f"Prompt: {prompt}")
        print(f"Response: {result.content}")
    except Exception as ex:
        print(f"An error occoured:[>>>{repr(ex)}]")
else:
    print("Failed to load environment variables")
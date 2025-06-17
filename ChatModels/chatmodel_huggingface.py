from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

if load_dotenv():
    hf_token = os.getenv('HUGGING_FACE_TOKEN')
    prompt = os.getenv('USER_PROMPT2')

    # Minimal configuration - move problematic parameters to explicit
    end_point = HuggingFaceEndpoint(
        # Change the Model name to the latest treanding one from 
        # huggingface Models section, text generation category
        # https://huggingface.co/models?pipeline_tag=text-generation&sort=trending
        # if you face 404 or StopIteration() error
        repo_id="mistralai/Magistral-Small-2506",
        task="text-generation",
        huggingfacehub_api_token=hf_token,
        max_new_tokens=100,  # Explicit
        temperature=0.1      # Explicit
    )

    model = ChatHuggingFace(llm=end_point)

    try:
        # Use HumanMessage for better compatibility
        message = HumanMessage(content=prompt)        
        result = model.invoke([message])
        print(f"Prompt: {prompt}")
        print(f"Respone: {result.content}")
    except Exception as ex:
        print(f"An error occoured:[>>>{repr(ex)}]")

        # Fallback: try direct string
        try:
            result = model.invoke(prompt)
            print(f"Fallback result: {result.content}")
        except Exception as ex2:
            print(f"Fallback also failed: {repr(ex2)}")
else:
    print("Failed to load environment variables")
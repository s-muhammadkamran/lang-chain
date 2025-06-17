from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

hf_token = os.getenv("HUGGING_FACE_TOKEN")
prompt = os.getenv("USER_PROMPT2")

# Safety checks
if not hf_token:
    print("Missing HUGGING_FACE_TOKEN")
    exit()

if not prompt:
    print("Missing USER_PROMPT")
    exit()

# Create client
client = InferenceClient(token = hf_token)

# Test call
try:
    output = client.text_generation(
        model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        prompt=prompt,
        max_new_tokens=50
    )
    print("Prompt:", prompt)
    print("Output:", output)
except Exception as e:
    print("Error:", repr(e))

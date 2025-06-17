# How To Configure

## Create a Python virtual environment

`python -m venv venv`

## Activate the environment

`.\venv\Scripts\Activate`

## Install dependecies

`pip install -r requirements.txt`

## Test if LangChain got installed correctly. You should see a version number.

`python test.py`

## Create a .env file at the root of the project and add values with following keys

OPENAI_API_KEY = "Paid Keys Need $$. Provide Your own generated Key from https://platform.openai.com/settings/organization/api-keys"  
CLAUDE_API_KEY = "Paid Keys Need $$. Provide Your own generated Key from https://console.anthropic.com/dashboard"  
GEMNI_API_KEY = "Provide Your own generated Key from https://aistudio.google.com/app/apikey"  
HUGGING_FACE_TOKEN = "Provide Your own generated Token from https://huggingface.co/settings/tokens"  

USER_PROMPT1 = "What has happened in World Politics today?"  
USER_PROMPT2 = "Translate Good bye to German"  

## You are good to go
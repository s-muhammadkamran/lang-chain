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

OPENAI_API_KEY = "---Provide Your own generated Key---"  
CLAUDE_API_KEY = "---Provide Your own generated Key---"  
GEMNI_API_KEY = "---Provide Your own generated Key---"  
HUGGING_FACE_TOKEN = "---Provide Your own generated Token---"  

USER_PROMPT1 = "What has happened in World Politics today?"  
USER_PROMPT2 = "Translate Good bye to German"  

## You are good to go
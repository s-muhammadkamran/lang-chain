# How To Configure

## Clone the code using

`git clone URL`

## Create a Python virtual environment at the root of cloned folder

`python -m venv venv`

## Activate the environment

`.\venv\Scripts\Activate`

## Install dependecies

`pip install -r requirements.txt`

## Test if LangChain got installed correctly. You should see a version number.

`python test.py`

## Create a .env file at the root of the project and add values with following keys

OPENAI_API_KEY = "Require Payment. Provide Your own generated Key from [OpenAI](https://platform.openai.com/settings/organization/api-keys)"  
CLAUDE_API_KEY = "Require Payment. Provide Your own generated Key from [Anthropic](https://console.anthropic.com/dashboard)"  
GEMNI_API_KEY = "Provide Your own generated Key from [Google AI Studio](https://aistudio.google.com/app/apikey)"  
HUGGING_FACE_TOKEN = "Provide Your own generated Token from [Hugging Face](https://huggingface.co/settings/tokens)"  

# Provide a location to be used as cache for the downloaded Hugging Face models..
HUGGING_FACE_LOCAL_CACHE_LOC = "LOCAL STORAGE LOCATION, Folder must exists."   

USER_PROMPT1 = "What has happened in World Politics today?"  
USER_PROMPT2 = "Translate Good bye to German"  

## You are good to go.

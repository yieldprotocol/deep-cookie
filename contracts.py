import os
import re
import openai
from langchain.llms import OpenAI
from ptemp import *
api_key = "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"
llm = OpenAI(model_name="text-davinci-003", temperature=0.9, openai_api_key=api_key)

def get_ideas():
    prompt = ContractIdeas
    # Send the prompt to the model
    llm.max_tokens = 4096 - llm.get_num_tokens(prompt)
    llm.temperature = 0.5
    out = llm(prompt) 
    out = re.sub(r'[0 - 9]', '', out)
    return out.split('\n')

def make_contracts():
    ideas = get_ideas()
    prompt = CreateContract + ideas[0] + '''
Code:
<code>'''
    llm.max_tokens = 4096 - llm.get_num_tokens(prompt)
    llm.temperature = 0.1
    out = llm(prompt)
    code = re.sub(prompt,"",out)
    code = re.sub("</code>", "", code)
    return code

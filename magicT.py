import os
import subprocess
import re
import openai
from langchain.llms import OpenAI
from ptemp import *
api_key = "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"
llm = OpenAI(model_name="text-davinci-003", temperature=0.9, openai_api_key=api_key)

# A function to extract information about the error, we can use this later 
def extract_info(string):
    pattern = 'error\[(\d+)\]: \\x1b\[0m\\x1b\[31m(\w+):.+\n.+:(\d+:\d+)'
    match1 = re.search(pattern, string)
    return match1.groups()

def createPrompt(error, project, debug=False):    
    prompt = magicSearcher1 + prefix + error + magicSearcherPostfix
    # Send the prompt to the model
    llm.max_tokens = 4096 - llm.get_num_tokens(prompt)
    llm.temperature = 0.5
    context = llm(prompt, stop="$") 
    # Extract the command
    contextCommand = context.split(":\n")[1]
    if debug:
        print(contextCommand)
    # Now let's get the context
    so = None
    try:
        so = subprocess.check_output(contextCommand,  shell=True, stderr=subprocess.STDOUT) # , stderr=subprocess.STDOUT
        print(so)
    except subprocess.CalledProcessError as err:
        saved_err = err
        print(err)

    if not so:
        print(saved_err.stdout)
    # Create the magic patching prompt
    errorPrompt = re.sub('project_name', project, promptPrefix) + error + \
    magicSearcherPostfix + context + "\n$ "+contextCommand+ "\n" + so.decode('utf-8') + magicPatcherPostfix
    return  errorPrompt

def getPatch(errorPrompt, debug=False, temp=0.5):
    # Send the prompt to the model
    llm.max_tokens = 4096 - llm.get_num_tokens(errorPrompt)
    llm.temperature = temp
    error4Fix = llm(errorPrompt, stop="$") 
    if debug:
        print(error4Fix)
    # Extract the command
    fixCommand = error4Fix.split(":\n")[1]
    return fixCommand
    
def runPatch(fixCommand):
    # Try running the patch
    try:
        so = subprocess.check_output(fixCommand, shell=True, stderr=subprocess.STDOUT) # , stderr=subprocess.STDOUT
        print(so)
    except subprocess.CalledProcessError as err:
        saved_err = err
        print(err)

def checkPatch(errordetails):
    # Now let's get the build errors for checking
    savedErr = ""
    try:
        so = subprocess.check_output(['forge', 'build'], stderr=subprocess.STDOUT) # , stderr=subprocess.STDOUT
        print(so)
    except subprocess.CalledProcessError as err:
        savedErr = err
        print(err)

    if savedErr:
        newError = extract_info(savedErr.output.decode('utf-8'))
        if errordetails != newError:
            print("It's fixed! (Probably)")
        else:
            print("Maybe it didn't work")
    else:
        print("Looks like compilation succeeded!")

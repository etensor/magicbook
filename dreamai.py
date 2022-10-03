from os import getenv
import openai
import requests
import json

openai.organization = "org-ZcdbJUytVfDDF6F2wusLC88x"
openai.api_key = getenv("OPENAI_API_KEY")
# print(openai.Model.list())



class GPT3AI():
    def __init__(self,bearer):
        self.bearer = bearer
    
    def talk_ai(self,prompt : str):
        #url = "https://api.openai.com/v1/engines/text-davinci-002/completions"
        #headers = {
        #    "Authorization": f"Bearer {self.bearer}",
        #    "Content-Type": "application/json",
        #}

        #"model": "text-davinci-002",
        if prompt == "":
            return ""

        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            temperature=0.3,
            top_p=1,
            #stream=False,
            frequency_penalty=0,
            presence_penalty=0
        )

                    #requests.post(url, headers=headers, data=json.dumps(body))
        
        print(f"#tokens: {response['usage']['total_tokens']}")
        return response['choices'][0]['text']

       

gpt3 = GPT3AI(openai.api_key)
print(gpt3.talk_ai(\
    str(input(' GPT3 prompt:\n -->  '))
))
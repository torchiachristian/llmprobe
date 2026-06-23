import requests

class Client:
    def __init__(self, endpoint_target, model_name, stream, system_prompt):
        self.endpoint = endpoint_target
        self.model = model_name
        self.stream = stream
        self.system_prompt = system_prompt

    def invia(self, payload):
        dati={
            "model": self.model,
            "stream": self.stream,
            "messages": [{"role": "system", "content": self.system_prompt}, {"role": "user", "content": payload}]
        }
        response = requests.post(self.endpoint, json=dati)
        risposta = response.json()
        return risposta["message]["content"]
    


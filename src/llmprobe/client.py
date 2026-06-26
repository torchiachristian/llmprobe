import requests
#il client di llmprobe si occupa di inviare le richieste al server dei chatbot e ricevere le risposte
#ad ogni generazione cambia soltanto il parametro payload
#tiene isolata la logica di rete in modo da semplificare le future classi Probe
#se modello cambia, tocco solo la logica del Client e tutte le altre classi restano tali


class Client:

#i dati di nascita che ho previsto erano:
#averli nell'init della classe è come averli sempre in tasca

    def __init__(self, endpoint_target, model_name, stream, system_prompt):
        self.endpoint = endpoint_target
        self.model = model_name
        self.stream = stream
        self.system_prompt = system_prompt

#metodo invia prende un payload, lo impacchetta nel formato gradito dal modello, lo spedice ridà la risposta
#Ollama si aspetta model/stream/messages 
#Ma messages deve contenere due voci perchè ci sono due ruoli diversi in un'interazione:
# --> "system" che contiene le istruzioni del modello, "user" l'attacco da eseguire

    def invia(self, payload):
        dati={
            "model": self.model,
            "stream": self.stream,
            "messages": [{"role": "system", "content": self.system_prompt}, {"role": "user", "content": payload}]
        }
#blocco try-except per gestire errori di rete. se modello irraggiungibile per qualsiasi motivo, programma non crasha ma restituisce None
        try:
            response = requests.post(self.endpoint, json=dati)
            risposta = response.json()
            return risposta["message"]["content"]
        except Exception as e:
            print(f"Errore durante l'invio della richiesta: {e}")
            return None



    
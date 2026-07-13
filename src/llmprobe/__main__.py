#nome __main__ speciale. dice a python di lanciare prima questo file di tutti gli altri
#per non avere costantemente un client fisso occorre libreria argparse, che permette di leggere argomenti da riga di comando e di lanciare llmprobe su ogni modello
#leggi scelte_ai.md (!!)

#creo un parser come prima cosa, invece che un client immediato
#servono librerie e classi:
import argparse
from .client import Client
from .runner import Runner

parser = argparse.ArgumentParser(description="llmprobe: a LLM security tool ")

#definisco gli argomenti che occorrono al parser obbligatoriamente
parser.add_argument("--endpoint", required=True, help="URL dell'endpoint del modello")
parser.add_argument("--model", required=True, help="nome del modello (es. llama3.2:1b)")
parser.add_argument("--system-prompt", required=True, help="system prompt del modello da testare")
parser.add_argument("--stream", action="store_true", help="attiva lo stream (default: disattivo)")

#funzione che legge gli argomenti passati dall'utente
args = parser.parse_args()

# solo ora creo un client con dentro i valori ricevuti
client = Client(args.endpoint, args.model, args.stream, args.system_prompt)

# crea il runner finalmente e lancia tutti i probe
#vedi classe Runner.py
runner = Runner(client)
runner.esegui_tutti()
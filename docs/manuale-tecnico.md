
# Manuale tecnico

>Documento per chi vuole osservare com'è strutturato LLMPROBE e estenderlo.

## Architettura scelta

CLI nel main -> Creazione di un Client -> Creazione di un runner -> Runner esegue 4 probe(attacchi) -> Ogni probe restituisce un esito -> Stampa informazioni 

- client.py: incapsula tutta la comunicazione HTTP col modello. costruisce un pacco JSON, fa la POST grazie a libreria requests, estrae il testo della risposta. Se il modello è irraggiungibile restituisce None tramite un'eccezione. È l'unico punto che conosce il protocollo di Ollama=CAMBIARE PROVIDER TOCCA SOLO QUESTO FILE 

- probe.py e 4 sottoclassi: vedi sotto gerarchia degli attacchi 
- esito.py e 3 sottoclassi: vedi sotto gerarchia dei verdetti
-runner.py: mantiene la lista dei quattro probe e li esegue in sequenza stampando gli esiti.

-__main__.py: legge gli argomenti grazie argparse, crea Client e Runner, avvia.

## Gerarchia delle classi

Probe (base astratta forma ABC)
├── SystemPromptLeakProbe
├── PromptInjectionProbe
├── JailbreakProbe
└── PolicyBypassProbe

Probe è classe astratta: definisce l'__init__ comune (salva client e nome) e obbliga ogni sottoclasse a implementare metodo esegui() tramite un abstract method. Ogni sottoclasse ha la propria lista di payload e un proprio marcatore. il metodo esegui() prova i payload uno ad uno e restituisce un Esito.


Esito (base)
├── EsitoVulnerabile
├── EsitoSicuro
└── EsitoIncerto

Esito è una classe base con la severità di default e il metodo descrivi(). Ogni sottoclasse poisovrascrive la sua severità e definisce descrivi() con un messaggio proprio

## Il polimorfismo

Il Runner non sa mai quale probe o quale esito concreto ha davanti. Chiama probe.esegui() e 
esito.descrivi() allo stesso modo su tutti senza un solo if sul tipo. 
qui lavora l'ereditarietà: aggiungendo un attacco si deve scrivere una nuova sottoclasse di Probe e inserirla nella lista del Runner, senza toccare nient'altro.

## Come aggiungere un nuovo attacco

1. Creare file nuovo_attacco_probe.py in src/llmprobe/
2. Ereditare da Probe cosa serve, aggiungere i propri payloads nella apposita lista, il marcatore e il metodo esegui()
3.Importarlo nel Runner e aggiungerlo alla lista self.probes.

NO modifiche al Client, ad Esito o al resto del codice.
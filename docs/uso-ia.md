# Uso dell'IA

> Trasparenza obbligatoria: Dichiara in modo granulare come hai usato gli assistenti IA (ChatGPT, Claude, Copilot, Gemini…). Dichiarare è sempre meglio che nascondere: se il codice ha uno stile da IA ma qui dici di non averla usata, la discrepanza pesa più dell'uso.

- Durante le sessioni di implementazione è stato utilizzato un LLM per: interpretazione di output del programma, spiegazione dettagliata di concetti tecnici, rilevazione di bug/imprecisioni, correzioni mirate al codice. E soprattutto per la ricerca di payload adatti alla consegna e per implementare concetti relativi alla cybersecurity/networking avanzato. 
La scelta logica dietro ogni classe, la programmazione di esse, la bozza di ogni sezione del progetto, l'utilizzo di git con uno scaffolding corretto e le restanti task sono state gestite interamente da noi.

## Sintesi

_Richiesta: quanto e come avete usato l'IA in questo progetto._

- Pipeline seguita: Idea di struttura del progetto/Bozza di una classe --> Scrittura di essa su VSCode --> Correzione autonoma di errori immediati, comprensione di ogni concetto possibile al nostro livello di teoria --> Invio a LLM --> Proposte di correzioni/spiegazioni/nuove implementazioni

## Dettaglio per parte

-Richiesta: Approvazione della struttura del progetto --> Approvata da subito, warning su try/except, spiegazioni importanti sulla parte di networking e sull'uso della libreria Request

-Errore individuato: gli esiti nel for vogliono come argomenti  (self.nome, f"payload riuscito: {payload}")  ,  non basta return Esito()

-Errore individuato: il mio-->
return EsitoSicuro(self.nome, f"nessun modello ha restituito marcatori", f"payload usati:" {payload")
diventa-->
return EsitoSicuro(self.nome, "nessun payload ha fatto emergere il marcatore")

-Richiesta: spiegazione di come la libreria requests invia i dati e com'è fatta la risposta di Ollama --> spiegazione, codice scritto da noi riga per riga perché serviva capire il formato JSON prima di scriverlo e corretto da chatbot

- Richiesta: serviva gestire il caso del modello irraggiungibile --> accettata IDEA del try/except che restituisce None per evitare crash ed esiti falsi

-Richiesta: perché in Python gli attributi si ripetono con self dentro init --> 
spiegazione concettuale, meccanismo delle tasche, esempi utili .

- Conferma che la nostra ereditarietà fosse la scelta giusta e non requisito inutile. Accettata la conferma ma la gerarchia è progettata da noi

- Ampia ricerca di attacchi testuali comuni per LLM come spunto per i payload. Accettati come base ma testati a mano da noi su llama3.2, non li avevamo mai visti e non avevamo sufficienti conoscenze

- Richiesta: come funziona la libreria argparse --> accettata la spiegazione, codice della CLI scritto da noi errato più volte perchè primo utilizzo di libreria argparse che avevamo solo sentito oralmente

- Errore individuato: mancava la normalizzazione del case minuscolo perchè in quella fase serviva confrontare marcatore e risposta con lower perché il modello varia le maiuscole e ci saremmo persi leak veri

- Errore individuato: parentesi non chiusa in un init di Probe per distrazione emersa nei test sperimentali, poi  una ] doppia in una lista di payload, elif errati e molti altri errori di sintassi corretti dopo la segnalazione di Claude e di compilatore

-Generazione di diagrammi ASCII complessi da creare per sezioni OPZIONI e GERARCHIA CLASSI dei MAnuali, in base a screenshot della gerarchia finita su VScode.

-Supervisione nelle sezioni 'Come si usa' e in concatenazioni di comandi per installazione e utilizzo. Spesso comandi inutili o sintassi errata di mezzo alla pipeline 

-Aiuto importante nel debug dell'AMBIENTE: gestito molto bene il passaggio a Python 3.11 tardivo, aiuto nella ricreazione del venv (mai provato ad utilizzare prima d'ora) e risoluzione di problemi di import mai visti quando i file non partivano come pacchetto

## Cosa NON abbiamo delegato all'IA

_Per regola, documentazione, devlog e riflessioni sulle scelte sono scritti da voi.

- Confermata redazione di documentazione autonoma, e riflessioni iniziali per ogni sezione autonome._

-Logica dietro ogni classe e scelte della gerarchia completamente nostre, con minime SUPERVISIONI dell'AI e modifiche solo in caso di problemi strutturali seri (rari)

-File redatti su VSCode in orario extralavorativo e su Blocco Note /compiler online in orario lavorativo condividendo idee

-Gestione di git, commit, divisione del lavoro fatte interamente da noi.


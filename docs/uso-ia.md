# Uso dell'IA

> Trasparenza obbligatoria: Dichiara in modo granulare come hai usato gli assistenti IA (ChatGPT, Claude, Copilot, Gemini…). Dichiarare è sempre meglio che nascondere: se il codice ha uno stile da IA ma qui dici di non averla usata, la discrepanza pesa più dell'uso.

- Durante le sessioni di implementazione è stato utilizzato un LLM per: interpretazione di output del programma, spiegazione dettagliata di concetti tecnici, rilevazione di bug/imprecisioni, correzioni mirate al codice. E soprattutto per la ricerca di payload adatti alla consegna e per implementare concetti relativi alla cybersecurity/networking avanzato. 
La scelta logica dietro ogni classe, la programmazione di esse, la bozza di ogni sezione del progetto, l'utilizzo di git con uno scaffolding corretto e le restanti task sono state gestite interamente da noi.

## Sintesi

_Richiesta: quanto e come avete usato l'IA in questo progetto._

- Pipeline seguita: Idea di struttura del progetto/Bozza di una classe --> Scrittura di essa su VSCode --> Correzione autonoma di errori immediati, comprensione di ogni concetto possibile al nostro livello di teoria --> Invio a LLM --> Proposte di correzioni/spiegazioni/nuove implementazioni

## Dettaglio per parte

| parte del progetto | cosa avete chiesto | cosa avete accettato / modificato / rifiutato | perché |
|---|---|---|---|
| _es. parser regex_ | _"come catturo l'IP in questa riga di log?"_ | _accettata la regex, riscritta con nomi gruppi_ | _per leggibilità_ |
| … | … | … | … |

-Richiesta: 
Approvazione della struttura del progetto --> Approvata da subito, warning su try/except, spiegazioni importanti sulla parte di networking e sull'uso della libreria Request

-Errore individuato: gli esiti nel for vogliono come argomenti  (self.nome, f"payload riuscito: {payload}")  ,  non basta return Esito()

-Errore individuato: il mio-->
return EsitoSicuro(self.nome, f"nessun modello ha restituito marcatori", f"payload usati:" {payload")
diventa-->
return EsitoSicuro(self.nome, "nessun payload ha fatto emergere il marcatore")

## Cosa NON abbiamo delegato all'IA

_Per regola, documentazione, devlog e riflessioni sulle scelte sono scritti da voi.

- Confermata redazione di documentazione autonoma, e riflessioni iniziali per ogni sezione autonome._




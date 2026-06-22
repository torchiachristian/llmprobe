Gruppo: Torchia Christian, D'Onofrio Enrico
Nome del programma: llmprobe

COSA FA IL PROGRAMMA

Strumento a riga di comando che, dato un endpoint di un modello come un LLM, esegue una batteria di test di sicurezza di primo livello (prompt injection, jailbreak, policy bypass, system prompt leak) e produce un report con il verdetto se quel modello regge ed è sicuro.
Il tutto sarà testato sia su un modello mock locale con una passkey da estrarre che sappiamo creare grazie alla materia AI & Prompt Engineering dell'ITS, sia tramite Ollama o OpenAI.

A CHI / COSA SERVE

Ad ogni red teamer che in una nuova azienda si interfaccia con un LLM mai visto prima, per testare chatbot di customer care di piccole boutique online verificando che passino i più basilari test di sicurezza, e ad un pentester nella primissima fase del vulnerability assessment di un modello AI.

COMPETENZE MESSE IN GIOCO

Ancora da verificare se tutte o solo alcune: richieste HTTP, JSON per il report (anche se preferiremmo un HTML; il JSON resta comunque il formato base testabile, l'HTML è un di più), OOP con ereditarietà e polimorfismo, regex.

BOZZA DI GERARCHIA DI EREDITARIETA'

Logica di base: ogni attacco prende un client, invia qualcosa, legge la risposta, decide se la risposta è conforme. Ogni attacco deve avere una funzione dedicata.
Senza ereditarietà si potrebbe fare, perché i 4 attacchi condividono cose simili, ma è meglio uniformarli ed evitare ripetizioni come si fa professionalmente.

Classe base Probe: dice "ogni attacco ha nome X, severità Y, funzione Z()". E' lo scheletro.

Sottoclasse di Probe per ogni attacco (es. JailbreakProbe, PromptInjectionProbe, ecc.): ha la formula di base più il suo pezzo di payload specifico.
Il nome Probe significa "sonda": le sottoclassi tipo JailbreakProbe hanno una relazione is-a con Probe perché sondano qualcosa di specifico.

Runner: ha una lista di probe (di attacchi) e per ogni probe chiama esegui() e raccoglie il risultato. Questo è il polimorfismo del progetto, perché la stessa chiamata ha comportamenti diversi a seconda dell'oggetto: un metodo chiamato dal resto del programma senza che sappia quale sottoclasse ha davanti.

Estendibilità: ogni volta che vogliamo aggiungere un attacco basta creare una sottoclasse "AttaccoProbe", metterla nella lista e dire al runner di eseguirla.

Classe base Esito: quando un attacco finisce non restituisce risultati grezzi in più formati, ma un oggetto Esito. L'Esito può essere Vulnerabile, Sicuro o Incerto. Al loro interno un metodo come descrivi() descrive le problematiche.

super(): ogni attacco salva cose comuni come nome, client, severità. Il metodo super() fa sì che a salvarle sia il genitore una volta sola, invece di riscriverle ad ogni attacco; poi il "figlio" scrive solo il suo payload invece che tutto da zero.

Flusso generale:
MAIN/RUNNER, per ogni Probe della lista, chiama esegui()
-> il Probe manda il payload al modello (via Client), legge la risposta, la giudica
-> ritorna un Esito (Vulnerabile / Sicuro / Incerto)
-> il runner chiama descrivi() sull'Esito e stampa la riga
Output: una riga per attacco, es. "jailbreak: [VULNERABILE] ..."

DUBBI EMERSI, RISPOSTI

Chi trasmette il testo malevolo al modello? Una libreria HTTP che conosciamo, requests, dentro una classe Client.
Il probe passa il payload a Client che fa una POST sul modello LLM. Non fa alcun GET per ottenere la risposta: la risposta arriva nella risposta stessa della POST. Di questo transito di dati si occupa requests; se vediamo errori relativi ad essa cerchiamo online.

Cos'è l'endpoint, sul nostro pc o online? E' il target a cui si mandano le richieste, ossia un semplice indirizzo come http://localhost:11434 se per esempio scarichiamo Ollama e un modello piccolo come llama3.2 che vive sul nostro pc/server in comune e vogliamo testarlo.

Una sola risposta per attacco: di più sarebbe difficile perché il programma dovrebbe ricordare lo stato della risposta precedente.

Non sapendo come popolare propriamente gli attributi malevoli delle classi degli attacchi, in un primo momento proveremo noi a cercare attacchi testuali comuni per LLM, per esempio nella OWASP Top 10 LLM. Se non riuscissimo a trovarne di efficaci, potremmo chiedere a chatbot dedicati (che interverrebbero solo sul lato AI Security, non sulla programmazione).

DUBBI EMERSI, RIMASTI

Ollama risponde vagamente: è dura decretare Vulnerabile / Non vulnerabile e si rischia di ricadere in Incerto troppe volte.

Se il modello non risponde o va in timeout, serve un try/except in Client per ricevere un EsitoIncerto invece di un crash.

Da decidere la divisione del lavoro e ogni quanto fare commit.

FASI

Non abbiamo ancora una scansione specifica, io ed il mio collega Enrico affineremo la programmazione dopo l'approvazione del progetto.
La direzione potrebbe essere: partiamo costruendo il modello locale e la classe Client, testando il canale di comunicazione. Poi, in ordine, implementiamo la classe base Probe e un attacco per vedere se la catena payload-client-esito-stampa funziona; verso metà progetto puntiamo ad avere i 4 attacchi; infine creiamo il Runner e i test pytest.

Fonte e ispirazione parziale: https://github.com/NVIDIA/garak  ,  https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Prompt%20Injection  

Restiamo in attesa di conferme o modifiche.

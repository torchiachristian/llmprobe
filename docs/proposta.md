#-Gruppo: Torchia Christian, D'Onofrio Enrico
#-Nome del programma: llmprobe

#-Cosa fa il programma: Strumento a riga di comando che, dato un endpoint di un modello come un LLM, esegue una batteria di test di sicurezza di primo livello( prompt injection, jailbreak, policy bypass, system prompt) e produce un report con il verdetto se quel modello regge ed è sicuro. 
Il tutto sarà testato sia su un modello mock locale con una passkey da estrarre che sappiamo creare grazie alla materia AI&Prompt Engineering dell'ITS tramite Ollama, OpenAI .

#-A chi/cosa serve: Ad ogni red teamer che in una nuova azienda si interfaccia con un LLM mai visto prima, per testare Chatbot client care di piccole boutique online verificando che passino i più basilari test di sicurezza, ad un Pentester nella primissima fase del vulnerability assessment di un modello AI.

#-Competenze messe in gioco, ancora da verificare se tutte o solo alcune: Richieste HTTP, Json per il report anche se preferiremmo un html , OOP con ereditarietà e polimorfismo, regex .

#-Bozza di gerarchia di ereditarietà: basandoci sulla logica che 
ogni attacco= prende un client->invia qualcosa->leggono risposta->decidono se risposta è conforme
ogni attacco deve avere una funzione dedicata
senza ereditarietà si potrebbe fare perchè i 4 attacchi performati condividono cose simili, ma meglio uniformarli e evitare ripetizioni come si fa professionalmente.
prevedo CLASSE BASE Probe = dice 'ogni attacco ha nome X, severità Y, funzione Z()' è lo scheletro
prevedo SOTTOCLASSE di Probe per ogni attacco es. JailbreakProbe, PromptinjectionProbe ecc..= ha una formula di base, e in più il suo pezzo di payload specifico
nome Probe perchè significa 'sonda' , perchè per esempio sottoclassi JailbreakProbe hanno relazioni is-a con Probe perchè sondano qualcosa di specifico (suggerisce Claude)
prevedo un RUNNER che ha lista di probe(di attacchi) e per ogni probe chiama esegui() e raccoglie il risultato= questo è il polimorfismo nel progetto perchè la stessa chiamata ha comportamenti diversi a seconda dell'oggetto. Un metodo chiamato dal resto del programma senza che sappia quale sottoclassi ha davanti
prevedo ESTENDIBILITà = ogni volta che voglio aggiungere un attacco basta creare una sottoclasse con 'AttaccoProbe', metterla nella lista, e poi dire al runner di eseguirla

prevedo CLASSE BASE Esito = quando un attacco finisce non restituisce risultati grezzi in più formati ma un oggetto Esito. 
oggetto Esito può essere Vulnerabile, Sicuro, Incerto . All'interno di esse metodo come descrivi() per descrivere le problematiche

In ogni probe serve un metodo super() = ogni attacco salva cose comuni come nome, client, severità, ma solo un metodo super() fa si che a salvarle sia il genitore una volta sola invece che riscriverle ad ogni attacco, poi il 'figlio' scrive solo il suo payload invece che tutto da zero.

Generato da Claude dopo queste deduzioni grezze:
MAIN/RUNNER → per ogni Probe della lista chiama esegui()
   → il Probe manda il payload al modello (via Client), legge la risposta, la giudica
   → ritorna un Esito (Vulnerabile / Sicuro / Incerto)
   → il runner chiama descrivi() sull'Esito e stampa la riga
Output: una riga per attacco, es. "jailbreak: [VULNERABILE] ..."


#-Dubbi emersi risposti: 
Chi trasmette il testo malevolo al modello? Una libreria http che conosco che si chiama requests, dentro una classe Client 
Il probe passa il payload a Client che fa POST sul modello LLM. Non fa alcun GET per ottenere la risposta. Si occupa di questo transito di dati requests e se vedo errori realtivi ad essa cerco online
Cos'è l'endpoint? sul mio pc o online? è il target a cui si mandano le richieste, nonchè un semplice indirizzo come http://localhost:11434 se per esempio scarico Ollama e un modello piccolo come llama3.2 vive sul mio pc/server in comune e voglio testarlo
Una sola risposta per attacco, di più sarebbe difficile perchè il programma dovrebbe ricordare stato della risposta precedente
Non sapendo come popolare propriamente gli attributi malevoli delle classi degli attacchi, in un primo momento proveremo noi a ricercare attacchi comuni testuali per LLM per esempio nella OWASP TOP 10 LLM, ma se non riuscissimo a trovarne di efficaci potremmo chiedere a Chatbot dedicati (che interverrebbero solo nel lato AI Security, non nella programmazione)

#-Dubbi emersi rimasti:
Ollama risponde vagamente, è dura decretare Vulnerabile - Non vulnerabile e si ricade in Incerto troppe volte
Se modello non risponde o va in timeout serve un try/except in Client per ricevere EsitoIncerto invece che un crash?
Da decidere la divisione e quanti commit fare ogni quanto

#-Fasi: Non abbiamo ancora una scansione specifica io e il mio collega Enrico, affineremo la programmazione dopo l'approvazione del progetto. 
La direzione potrebbe essere= partiamo costruendo il modello locale e la classe Client, testando il canale di comunicazione. Poi in ordine implementiamo la classe base Probe, un attacco per vedere se la catena payload-client-esito-stampa funziona, poi verso metà progetto avere i 4 attacchi, e infine creare il Runner e i pytest.

Restiamo in attesa di conferme o modifiche. 

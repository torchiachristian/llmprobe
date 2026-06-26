
-Client si occupa di ogni operazione di rete perchè i Probe siano semplici da comporre e ricevano testo pulito. Cambiare modello diventa semplice e meno dispendioso perchè una volta compreso il formato json che vuole in invio/risposta dobbiamo solo modificare Client.py

-invia() restituisce solo il testo che ci occorre e non una risposta grezza totale

-stream viene trattato come un booleno perchè è  true/false, restanti parametri sono stringhe

-nel try-except da aggiungere si crea un parametro None utile da restituire quando il modello è irraggiungibile, altrimenti si rischia che POST crashi o che ci siano Esiti errati.

-messages[] è una lista perchè una sequenza ordinata di messaggi e conta l'ordine, dev'essere inviato PRIMA system POI user . Lista tiene elementi in ordine, dizionario non riesce ad avere questa sequenza

-DENTRO messages[] ci sono dizionari (per i due tipi di messaggi). Questo perchè a sua volta il messaggio ha due campi role e content. Conveniva questo e ha funzionato subito

-Le etichette del PACCO ESTERNO di nome "dati" sono model, stream, messages, role, content perchè sono nomi fissi che Ollama richiede. le mie "tasche" interne come self.model posso chiamarle come voglio ma non verranno accettate.

-self.system_prompt è scritto con self. perchè salvato da inizio classe, payload scritto senza niente perchè arriva da fuori in ogni chiamata

-Ho dovuto salvare dentro 'risposta' response.json() prima di scavare all'interno di response.json() per trovare il content.

-risposta["message"]["content"] e non direttamente risposta["content"] perchè il parametro content è annidato dentro message. non al primo livello

-request.post basta ed è L'UNICA FUNZIONE che richiediamo alla libreria requests. Insieme a json() che converte la risposta in un dizionario Python su cui possiamo operare, hanno fatto tutto il lavoro. Non esiste GET come ritorno di dati da POST, anche se inizialmente pensavamo questo. Risposta torna nella stessa chiamata.
---------------------------------------------------

#Schematizzazione di Client.py:

1. init salva i dati fissi della sessione(endpoint, stream, system_prompt,model)

2. viene chiamata funzione invia() che impacchetta in un formato accettato da Ollama i dati che servono ad esso per interazioni:
 model+stream+ i 2 messaggi (system con istruzioni , user con payload)

3. request.post spedisce il pacco completo di ogni dato che serve al modello tramite una POST

4. response.json() converte la risposta in un dizionario Python su cui possiamo operare

5. Viene salvato tutto in parametro ' risposta ' 

6. Scaviamo in ' risposta ' e otteniamo ["message"]["content"] , restituiti poi al chiamante.

7. try - except
## Scelte operative 

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

- request.post basta ed è L'UNICA FUNZIONE che richiediamo alla libreria requests. Insieme a json() che converte la risposta in un dizionario Python su cui possiamo operare, hanno fatto tutto il lavoro. Non esiste GET come ritorno di dati da POST, anche se inizialmente pensavamo questo. Risposta torna nella stessa chiamata.

- Il payload lo abbiamo passato come attributo standard della classe, non nell'init perchè la lista è uguale per ogni probe di quel tipo non va passata da fuori ad ogni oggetto

- Severità è un attributo che abbiamo messo fuori dall' init in Esito per lo stesso motivo della scelta precedente. è un etichetta fissa, es. EsitoVulnerabile è sempre Severità=VULNERABILE . 

- In metodo esegui() prima si controlla il None e poi il marcatore e non viceversa. se controllo prima il marcatore e la risposta per caso è None, python crasha.

---------------------------------------------------

# Schematizzazione di Client.py:

1. init salva i dati fissi della sessione(endpoint, stream, system_prompt,model)

2. viene chiamata funzione invia() che impacchetta in un formato accettato da Ollama i dati che servono ad esso per interazioni:
 model+stream+ i 2 messaggi (system con istruzioni , user con payload)

3. request.post spedisce il pacco completo di ogni dato che serve al modello tramite una POST

4. response.json() converte la risposta in un dizionario Python su cui possiamo operare

5. Viene salvato tutto in parametro ' risposta ' 

6. Scaviamo in ' risposta ' e otteniamo ["message"]["content"] , restituiti poi al chiamante.

7. try - except per gestire modelli irraggiungibili

# Schematizzazione di Probe:
1. la classe base astratta fa da contratto e stabilisce che ogni attacco deve avere un metodo esegui() e deve per forza compilarlo

2. init salva due dati comuni ad ogni probe ossia client e nome

3. esegui() è un abstract method, Probe base non lo scrive ma obbliga ogni sottoclasse a scriverlo

# Schematizzazione di Esito.py:
1. la classe base ha una severità N/D come attributo standard, è default e le altre classi lo sovrascriveranno

2. metodo init salva probe_nome (chi l'ha prodotto) e dettaglio (cosa è successo)

3. descrivi() restituisce una frase con severità + nome + dettaglio 




Logica ciclo For nei Probe:
per ogni payload nella lista
    risposta = self.client.invia(payload)
    se risposta è None → return EsitoIncerto (modello giù)
    se il marcatore è dentro la risposta → return EsitoVulnerabile (ha bucato, mi fermo)
se il for finisce senza aver bucato → return EsitoSicuro (ha retto a tutti)
# Devlog

> Richiesta: Diario di bordo del gruppo. **Una entry a settimana** (minimo tre nel corso del progetto),
> 15-30 righe l'una, in prima persona plurale, **scritte da voi** (non dall'IA).


## Come si scrive

Tecnico e onesto: cosa avete fatto (fatti, non aspirazioni), cosa vi ha fatto perdere tempo,
cosa avete imparato, quali decisioni avete preso e perché, come vi siete divisi il lavoro.
Se una settimana non avete combinato niente, scrivetelo. Se vi siete bloccati tre giorni su
un bug, raccontate il bug. Le date delle entry vengono confrontate con il `git log`.

Ogni entry dovrebbe toccare almeno tre di questi punti:

- cosa abbiamo fatto questa settimana;
- cosa ci ha fatto perdere tempo e perché;
- cosa abbiamo imparato di nuovo (tecnicamente o organizzativamente);
- decisioni prese: cosa abbiamo scelto, perché, cosa abbiamo scartato;
- cosa pianifichiamo per la settimana prossima;
- divisione del lavoro: chi sta facendo cosa.

---

## Entry

### Settimana 1 — [date]

_Scrivete qui._
-CODICE SVILUPPATO, SCAFFOLDING ANCORA NON SVILUPPATO A PIENO --> SEZIONE Devlog NON IMPORTATA SU VScode, SEZIONE Devlog IGNORATA-->ENTRY INESISTENTE

-Entry postuma: 

### Settimana 2 — [date]

_Scrivete qui._
-CODICE SVILUPPATO, SCAFFOLDING ANCORA NON SVILUPPATO A PIENO --> SEZIONE Devlog NON IMPORTATA SU VScode, SEZIONE Devlog IGNORATA-->ENTRY INESISTENTE

-Entry postuma:

### Settimana 3 — [date]

_Scrivete qui._
- Entry: Nonostante ci troviamo alla terza settimana di progetto, e che per via dello Scaffolding tardivo non sia stato possibile rendicontare le prime settimane, tramite note e elementi condivisi tra noi (Enrico e Christian), è possibile avere ogni entry/fatto da raccontare in ordine.

Nella prima settimana la proposta è stata scritta e approvata dal professore con estrema convinzione. La nostra idea originale, semplice e piena di use cases è risultata ottima. Installato Ollama llama 3.2:1b e fatti primi test manuali con curl e payload è stato impressionante vedere il modello rispondere in modi diversi ogni volta, ciò rende possibile creare un programma pieno di risultati vari e originali. I payload però fallivano davvero troppe volte e risultavano banali inviati da soli, quindi li abbiamo accoppiati ad un marcatore come una parola specifica che il modello non doveva dire per giudicare in modo deterministico se l'attacco è riuscito. Nonoostante alcune conoscenze fossero ottime per via di unità formative scolastiche propedeutiche mancavano ad entrambi nozioni vere per la parte di security e networking legata alla gerarchia. Come 'parlare' con un endpoint di un'AI, come gestire il traffico HTTP (anche se si è rivelato banale), e come imbastire le classi che svolgono le operazioni più insidiose. Per colmare queste lacune prima di progettare e per una profonda supervisione dell'esecuzione è venuto in aiuto un chatbot efficiente. 
Verso la seconda settimana abbiamo rapidamente costruito un Client. La principale difficoltà è stata per Christian comprendere in che formato preciso JSON Ollama vuole i dati e come scrivere una formattazione simile in python. A classe ultimata, il chatbot ha suggerito un try/except molto utile e spiegato in scelte.md . 
Con una rapida spiegazione della classe Client al collega, e una decisione finale della gerarchia insieme, che è risultata semplice da implementare ma non banale, si è passati subito ad una divisione di compiti.
-Christian ha implementato le fondamenta principalmente: come la classe Probe, le prime due Probe per dare uno standard, la classe Esito.
-Enrico ha implementato i Probe restanti allacciandosi rapidamente alle basi create dal collega e le classi Esito con un'ottima visione dei cases.
Avendo già i payload malevoli da risorse online/chatbot, e avendo faticato soltanto a creare le classi base da zero come Esito e Probe, creare il resto è diventato un lavoro semplice e di compilazione dato che pochissimi dati variavano (solo nomi e la lista di payloads).
Nella terza settimana sono state completate tutte le sottoclassi (Probe soprattutto), scritto un Runner complesso che ha richiesto la logica di entrambi e frammenti di codice a cui non avevamo minimamente pensato implementati dall'AI, dato che era una tipologia di runner simile a quello visto didatticamente ma molto più complesso. Sviluppata la CLI minimale con Argparse, libreria conosciuta da entrambi ma di cui non avevamo mai visto un'implementazione e abbiamo dovuto studiare teoricamente e tecnicamente l'uso (soprattutto non conoscendo le caratteristiche di un PARSER ). Dopo questo step, il progetto è pronto alla fase di testing, a cui penseremo nei giorni rimanenti prima della consegna, senza confrontarci ma proponendo test individualmente così da creare implicitamente più possibilità di trovare falle casuali. I primi test svolti su un unico device da Christian evidenziano un programma sano e in cui numerosi payload bucano LLAMA3.2.1B, evento che ha generato molta soddisfazione.
Nonostante le difficoltà nell'approcciare un progetto così esteso, le risorse messe a disposizione e soprattutto la disponibilità di avere un compagno su cui fare affidamento ha reso molto più leggero il lavoro. Inoltre, la semplicità ma robustezza di ogni classe, senza necessità di strutture annidate, e senza implementare funzionalità inutili al fine, hanno trasformato la consegna in un processo automatico. La pipeline descritta in uso-ia.md ha consentito un'esperienza scorrevole e soprattutto di imparare insieme concetti nuovi e fruibili da qui in poi.


---

## Bilancio finale

Alla consegna, una entry di bilancio (30-50 righe). Spunti: di cosa siete più soddisfatti,
cosa avete capito di nuovo, cosa avete sottovalutato all'inizio, cosa rifareste diversamente,
se la divisione del lavoro è stata equa, cosa avreste aggiunto con un'altra settimana, e —
onestamente — che voto dareste al vostro progetto e perché.

-Entry di bilancio: 

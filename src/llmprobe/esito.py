#La classe Esito rappresenta il risultato di un attacco eseguito da un Probe e
#non si usa mai da sola poiché è la base comune per le 3 sottoclassi,
#così ogni Probe.esegui() stampa sempre "un Esito", senza che il runner
#debba sapere quale delle tre sottoclassi stia utilizzando

#Proprio per questo motivo, ossia la dipendenza delle sottoclassi probe
#rispetto alla classe esito, che quest'ultima viene definita per prima

class Esito:

#severita è un attributo di classe (fuori da __init__) perché è un'etichetta
#fissa uguale per ogni istanza di quel tipo di esito, non cambia da un
#EsitoVulnerabile all'altro. Qui vale "N/D" solo come valore di default,
#le sottoclassi la sovrascrivono subito con il proprio valore

    severita = "N/D"

#init salva solo le due cose che ogni esito ha in comune:
#probe_nome dice chi ha generato l'esito, dettaglio spiega cosa è successo
#nella risposta del modello. Le sottoclassi non aggiungono altri dati,
#quindi bastano questi due parametri per tutte e tre

    def __init__(self, probe_nome, dettaglio):
        self.probe_nome = probe_nome
        self.dettaglio = dettaglio

#descrivi() è il metodo polimorfico: il runner lo chiama su un Esito
#qualsiasi senza controllare il tipo con if/else. Qui nella base è una
#versione generica che usa severita; le sottoclassi la ridefiniscono
#per dire qualcosa di più specifico (es. "ha ceduto" invece di un generico messaggio)

    def descrivi(self):
        return f"[{self.severita}] {self.probe_nome}: {self.dettaglio}"

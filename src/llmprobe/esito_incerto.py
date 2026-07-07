from .esito import Esito

#EsitoIncerto: copre i casi ambigui, es. modello irraggiungibile (il Client
#ritorna "None") o risposta che non contiene né conferma né smentita chiara.
#serve per non forzare un Probe a scegliere tra vulnerabile e sicuro quando
#non ha abbastanza informazioni per giudicare

class EsitoIncerto(Esito):

    severita = "INCERTO"

    def __init__(self, probe_nome, dettaglio):
        super().__init__(probe_nome, dettaglio)

#override di descrivi(): segnala l'ambiguità, così il
#runner (o chi legge il report) sa che quella riga andrebbe rivista a mano

    def descrivi(self):
        return f"[{self.severita}] {self.probe_nome} esito ambiguo: {self.dettaglio}"

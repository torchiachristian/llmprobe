from .esito import Esito

#EsitoIncerto, il modello probabilmente è irraggiungibile.
#implementato esattamente sulla base di esito_sicuro.py
class EsitoIncerto(Esito):

    severita = "INCERTO"

    def __init__(self, probe_nome, dettaglio):
        super().__init__(probe_nome, dettaglio)


    def descrivi(self):
        return f"[{self.severita}] {self.probe_nome} esito ambiguo o modello irraggiungibile: {self.dettaglio}"

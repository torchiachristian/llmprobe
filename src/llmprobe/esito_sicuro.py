from .esito import Esito

#EsitoSicuro: l'attacco è fallito, il modello ha retto.
#è l'esito "buono", la severità è da considerare bassa perché non segnala nessun problema

class EsitoSicuro(Esito):

    severita = "SICURO"

    def __init__(self, probe_nome, dettaglio):
        super().__init__(probe_nome, dettaglio)

#Override di descrivi(): conferma la tenuta invece di segnalare un cedimento,
#così chi legge il report distingue a colpo d'occhio le righe positive

    def descrivi(self):
        return f"[{self.severita}] {self.probe_nome} ha retto: {self.dettaglio}"

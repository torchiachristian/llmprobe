from .esito import Esito

#EsitoVulnerabile: l'attacco è riuscito, è la sottoclasse più critica perché segnala un problema
#reale di sicurezza, quindi la severità è la più elevata

class EsitoVulnerabile(Esito):

    severita = "VULNERABILE"

#super().__init__() richiama l'init della classe genitore importata sopra, per
#salvare probe_nome e dettaglio senza doverli riscrive. Se in futuro servirà
#un campo in più (es. "evidenza" con la porzione di risposta incriminata)
#questo è il punto in cui sarà possibile aggiungerlo

    def __init__(self, probe_nome, dettaglio):
        super().__init__(probe_nome, dettaglio)

#override di descrivi(): stessa firma del genitore ma messaggio diverso,
#per far capire subito a chi legge il report che qui il modello ha fallito

    def descrivi(self):
        return f"[{self.severita}] {self.probe_nome} ha CEDUTO: {self.dettaglio}"

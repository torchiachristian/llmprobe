from llmprobe.system_prompt_leak_probe import SystemPromptLeakProbe
from llmprobe.esito_vulnerabile import EsitoVulnerabile
from llmprobe.esito_sicuro import EsitoSicuro
from llmprobe.esito_incerto import EsitoIncerto

# probe funziona quando produce un esito. idea di testare che dia l'esito corretto anche senza marcatore di mezzo (nel caso più complicato in assoluto)
#obiettivo : generare errori da fixare 

class ClientRisposta:
    def __init__(self, risposta):
        self.risposta = risposta
    def invia(self, payload):
        return self.risposta
#questo client fittizio restituisce la risposta che gli dico io alla creazione

def test_probe_vulnerabile():
        client = ClientRisposta("BASILISK")
        probe = SystemPromptLeakProbe(client, "leak")
        esito = probe.esegui()
        assert isinstance(esito, EsitoVulnerabile)
        #questo test controlla che la risposta contenga BASILISK , il leak probe lo trova e dà EsitoVulnerabile se ha successo 

def test_probe_sicuro():
        client = ClientRisposta("risposta innocua senza segreti")
        probe = SystemPromptLeakProbe(client, "leak")
        esito = probe.esegui()
        assert isinstance(esito, EsitoSicuro)
        #stessa logica del test precedente ma con una risposta innocua che non contiene BASILISK , quindi il probe restituisce EsitoSicuro
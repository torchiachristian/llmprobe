from llmprobe.esito import Esito
from llmprobe.system_prompt_leak_probe import SystemPromptLeakProbe
from llmprobe.prompt_injection_probe import PromptInjectionProbe
from mock_client import TestClient

#prendiamo il client fittizio da test_client 

def test_polimorfismo():
        client = TestClient()
        probes = [
            SystemPromptLeakProbe(client, "leak"),
            PromptInjectionProbe(client, "injection"),
        ]
    #nella lista di probes inseriamo due probe fittizi

        for probe in probes:
            esito = probe.esegui()
            assert isinstance(esito, Esito)
            #ogni probe in probe viene eseguito e dà un esito
            #istance(esito Esito) verifica che tutti quanti abbiano restituito un esito 
            #dato che il ciclo for non sa quale probe ha in mano perchè glieli abbiamo passati come Probe senza specificare il tipo, SI TRATTA DI POLIMORFISMO


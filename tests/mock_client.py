
from llmprobe.system_prompt_leak_probe import SystemPromptLeakProbe
from llmprobe.prompt_injection_probe import PromptInjectionProbe
from llmprobe.esito import Esito

class TestClient:
    def invia(self, payload):
        return "risposta con BASILISK e VIOLATO dentro "
    
#dopo aver creato questo client fittizio, lo passiamo in test polimorfismo
#che è in un altro file
    
    #questo file non è un test di per sè. serve per essere passato a test_polimorfismo
    #non nominata test_client ma mock_client perchè pytest davano errori , ogni cosa nominata TEST la testano
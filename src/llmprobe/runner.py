#importiamo innanzitutto i 4 attacchi 
from .system_prompt_leak_probe import SystemPromptLeakProbe
from .prompt_injection_probe import PromptInjectionProbe
from .jailbreak_probe import JailbreakProbe
from .policy_bypass_probe import PolicyBypassProbe

#la classe init salva self.client come client che arriva dalla CLI 
#crea inoltre una lista dei probe ben costruita

class Runner:
    
    def __init__(self, client):
        self.client = client
        self.probes = [
            SystemPromptLeakProbe(client, "System Prompt Leak Probe"),
            PromptInjectionProbe(client, "Prompt Injection Probe"),
            JailbreakProbe(client, "Jailbreak Probe"),
            PolicyBypassProbe(client, "Policy Bypass Probe"),
        ]

    # esegui_tutti() esegue tutti i probe in sequenza, stampando l'esito di ciascuno
    # metodo polimorfico perchè ogni probe ha il suo esegui() specifico, ma qui li chiamiamo tutti allo stesso modo
    def esegui_tutti(self):
        for probe in self.probes:
            esito = probe.esegui()
            print(esito.descrivi())
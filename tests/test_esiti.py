from llmprobe.esito_vulnerabile import EsitoVulnerabile
from llmprobe.esito_incerto import EsitoIncerto
from llmprobe.esito_sicuro import EsitoSicuro

def test_esito_vulnerabile():
    esito = EsitoVulnerabile("Test Probe", "Testo di esempio")
    risultato = esito.descrivi()
    assert "VULNERABILE" in risultato

#pytest per testare gli esiti.
#creo un test vulnerabile con due dati finti e chiamo descrivi() per vedere cosa torna
#se torna VULNERABILE nella stringa allora il test è passato 

#faccio la stessa identica cosa per gli altri due esiti cambiando i nomi

def test_esito_incerto():
    esito = EsitoIncerto("Test Probe", "Testo di esempio")
    risultato = esito.descrivi()
    assert "INCERTO" in risultato

def test_esito_sicuro():
    esito = EsitoSicuro("Test Probe", "Testo di esempio")
    risultato = esito.descrivi()
    assert "SICURO" in risultato
    
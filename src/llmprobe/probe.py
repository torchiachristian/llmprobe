
#abc è libreria python per creare classi astratte
from abc import ABC, abstractmethod

#classe Probe con parametri client e nome. agiscono come due tasche, una manda il payload e la seconda etichetta un esito
#ogni attacco ha un client, un nome, e un metodo esegui(). questa classe non fa niente da sola, obbliga solo le sottoclassi a esistere con quella forma precisa 
class Probe(ABC):
    def __init__(self, client, nome:
        self.client = client
        self.nome = nome

#metodo astratto che obbliga ogni sottoclasse a scrivere in questo metodo
    @abstractmethod
    def esegui(self):
        pass
        
#ogni sotto classe Probe poi erediterà questa struttura e dovrà riempire esegui(). suo specifico payload, client.py per la comunicazione , attinge da Esiti l'esito .
class AsientoImplementado(Asiento):
    def __init__(self,numero:int,avion:Avion,estado:str,vuelo:Vuelo,disponible:bool):
        super.__init__(numero,avion,estado)
        self.vuelo=vuelo
        self.disponible=disponible

from Vuelo import Vuelo
from Asiento import Asiento
class Pasaje:
    def __init__(self,cliente:Cliente,asiento:type[AsientoImplementado]):
        self.cliente=cliente
        self.asiento=asiento

from Cliente import Cliente
from AsientoImplementado import AsientoImplementado
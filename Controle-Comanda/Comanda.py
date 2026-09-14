from datetime import datetime


class Comanda:
    def __init__(self, numero:int, nome_cliente:str):
        self._numero = numero
        self._nome_cliente = nome_cliente
        self._data_hora_abertura = datetime.now()
        self._refeicoes_pedidas = []
        self._bebidas_pedidas = []

    def abrir_comanda(self, value):  
        pass

    def fechar_comanda(self, value):
        pass
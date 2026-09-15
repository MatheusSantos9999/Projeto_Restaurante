from datetime import datetime


class Comanda:
    def __init__(self):
        self._numero = None
        self._nome_cliente = None
        self._data_hora_abertura = datetime.now()
        self._refeicoes_pedidas = []
        self._bebidas_pedidas = []

    def abrir_comanda(self, nome_cliente:str, numero_comanda:int):
        
        self._nome_cliente = nome_cliente
        self._numero = numero_comanda


    def fechar_comanda(self):
        pass
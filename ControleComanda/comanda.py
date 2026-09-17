import re
from datetime import datetime


class Comanda:
    def __init__(self, numero, nome):
        self._numero = None
        self._nome_cliente = None
        self._data_hora_abertura = None
        self._refeicoes_pedidas = []
        self._bebidas_pedidas = []
        self._fechada = False
        self._aberta = False

        self.numero = numero
        self.nome_cliente = nome
        self.abrir_comanda()

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor:int):

        if isinstance(valor, int) and not isinstance(valor, bool) and valor > 0:
            self._numero = valor
        else:
            raise ValueError('número para comanda inválido')

    @property
    def nome_cliente(self):
        return self._nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, valor:str):

        padrao = re.compile(r'[A-Za-zÀ-ÖØ-öø-ÿ\s.]+')
        checar_padrao = padrao.fullmatch(valor)

        if isinstance(valor, str) and checar_padrao:
            self._nome_cliente = valor
        else:
            raise ValueError('Nome inválido')

    @property
    def refeicoes_pedidas(self):
        return self._refeicoes_pedidas

    @refeicoes_pedidas.setter
    def refeicoes_pedidas(self, valor:str):

        if self._fechada:
            raise ValueError('Não é possível adicionar itens a uma comanda já fechada')

        if isinstance(valor, str):
            valor_limpo = valor.replace(" ","")
            
            padrao= re.compile(r'([\w-]+)')
            
            checar_valor = padrao.fullmatch(valor_limpo)

            if checar_valor:
                self._refeicoes_pedidas.append(valor)
            else:
                raise ValueError('Refeição inválida')

    @property
    def bebidas_pedidas(self):
        return self._bebidas_pedidas

    @bebidas_pedidas.setter
    def bebidas_pedidas(self, valor:str):
        if self._fechada:
            raise ValueError('Não é possível adicionar itens a uma comanda já fechada')

        if isinstance(valor, str):
            valor_limpo = valor.replace(" ","")
                    
            padrao = re.compile(r'([\w-]+)')
                    
            checar_valor = padrao.fullmatch(valor_limpo)
        
            if checar_valor:
                self._bebidas_pedidas.append(valor)
            else:
                raise ValueError('Bebida inválida')
 
    def abrir_comanda(self):
        if self._aberta:
            raise ValueError('Você não pode abrir a mesma comanda duas vezes')

        self._aberta = True
        self._data_hora_abertura = datetime.now()

    def fechar_comanda(self):
        self._fechada = True

    @property
    def data_hora_abertura(self):
        return self._data_hora_abertura

    @property
    def fechada(self):
        return self._fechada




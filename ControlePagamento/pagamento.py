import re
from datetime import datetime


class Pagamento:
   

    def __init__(self, nome:str, numero_pagamento:int, forma_pagamento:str, valor_total:float):
        self._nome_pagador = None
        self._numero_comanda = None
        self._forma_pagamento = None
        self._valor_total_pago = 0
        self._data_hora_pagamento = None
        self._formas_validas = ['PIX', 'Cartão', 'Dinheiro']

        self.nome_pagador = nome
        self.numero_comanda = numero_pagamento
        self.forma_pagamento = forma_pagamento
        self.valor_total_pago = valor_total
        self._data_hora_pagamento = datetime.now()

    @property
    def nome_pagador(self):
        return self._nome_pagador

    @nome_pagador.setter
    def nome_pagador(self, valor:str):
        padrao = re.compile(r'[A-Za-zÀ-ÖØ-öø-ÿ\s.]+')

        if isinstance(valor, str) and padrao.fullmatch(valor):
            self._nome_pagador = valor
        else:
            raise ValueError('Nome inválido')

    @property
    def numero_comanda(self):
        return self._numero_comanda

    @numero_comanda.setter
    def numero_comanda(self, valor:int):

        if isinstance(valor, int) and not isinstance(valor, bool) and valor > 0:
            self._numero_comanda = valor
        else:
            raise ValueError('número para comanda inválido')

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, valor:str):
        if isinstance(valor, str) and valor in self.self._formas_validas:
            self._forma_pagamento = valor
        else:
            raise ValueError(f'Forma de pagamento inválida. Use uma de: {self.self._formas_validas}')

    @property
    def valor_total_pago(self):
        return self._valor_total_pago

    @valor_total_pago.setter
    def valor_total_pago(self, valor:float):
        if isinstance(valor, (float, int)) and not isinstance(valor, bool) and valor > 0:
            self._valor_total_pago = valor
        else:
            raise ValueError('Valor total pago inválido')

    @property
    def data_hora_pagamento(self):
        return self._data_hora_pagamento
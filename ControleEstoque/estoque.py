import re
from EstruturaDados import lista_encadeada
from datetime import datetime

class Estoque:
    def __init__(self):
        self.lista = lista_encadeada.ListaEncadeada()

    def repor_estoque(self, produto):
        nome_produto = produto.nome_produto
        self.lista.adicionar_dados((nome_produto, produto))

class Produto:
    def __init__(self):
        self._nome_produto = None
        self._preco_compra = 0
        self._preco_venda = 0
        self._data_compra = None
        self._data_vencimento = None
        self._quantidade_estoque = 0

    @property
    def nome_produto(self):
        return self._nome_produto

    @nome_produto.setter
    def nome_produto(self, valor:str):

        if isinstance(valor, str):
            valor_limpo = valor.replace(" ","")

            padrao= re.compile(r'([\w-]+)')

            checar_valor = padrao.fullmatch(valor_limpo)

            if checar_valor:
                self._nome_produto = valor
                    
            else:
                #print('\nNome inválido!!')
                #valor = input('\nPor favor digite um nome de produto válido: ')
                raise ValueError('Nome de Produto Inválido')
        else:
            raise ValueError('Tipo de Dado Inválido')

    @property
    def preco_compra(self):
        return self._preco_compra

    @preco_compra.setter
    def preco_compra(self, valor:float|int):
        if isinstance(valor, (float,int)) and not isinstance(valor, bool) and valor > 0:
            self._preco_compra = valor
        else:
            raise ValueError('preço de compra inválido')

    @property
    def preco_venda(self):
        return self._preco_venda
    
    @preco_venda.setter
    def preco_venda(self, valor:float|int):
        if isinstance(valor, (float,int)) and not isinstance(valor, bool) and valor > 0:
            self._preco_venda = valor
        else:
            raise ValueError('preço de venda inválido')

    @property
    def data_compra(self):
        return self._data_compra

    @data_compra.setter
    def data_compra(self, valor:str):
        try:
            datetime.strptime(valor, "%d/%m/%Y")
            self._data_compra = valor
        except ValueError:
            raise ValueError('Data de Compra Inválida')

    @property
    def data_vencimento(self):
        return self._data_vencimento
        
    @data_vencimento.setter
    def data_vencimento(self, valor:str):
        
        try:
            datetime.strptime(valor, "%d/%m/%Y")
            self._data_vencimento = valor
        except ValueError:
            raise ValueError('Data de Vencimento Inválida')

    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, valor:int):
        if isinstance(valor, int) and not isinstance(valor, bool) and valor > 0:
            self._quantidade_estoque = valor
        else:
            raise ValueError('Quantidade inválida')
    

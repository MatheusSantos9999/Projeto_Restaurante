import re
from EstruturaDados import lista_encadeada, fila
from datetime import datetime


class Estoque:
    def __init__(self):
        self._lista = lista_encadeada.ListaEncadeada()

    def repor_estoque(self, produto):
        resultado = self._lista.buscar_dados(lambda item: item[0] == produto.nome_produto)
        
        if resultado is not None:
            resultado[1].enfileirar(produto)

        else:
            fila_produto = fila.Fila()
            fila_produto.enfileirar(produto)
            self._lista.adicionar_dados((produto.nome_produto,fila_produto))

    def dar_baixa(self, nome_produto, quantidade_produto):
        resultado = self._lista.buscar_dados(lambda item: item[0] == nome_produto)

        if resultado is None:
            raise ValueError('O produto não existe no estoque')

        fila_do_produto = resultado[1]

        lote_atual = fila_do_produto.inicio.dado if fila_do_produto.inicio else None
        quantidade_restante = quantidade_produto

        while lote_atual and quantidade_restante > 0:
            if lote_atual.quantidade_estoque > quantidade_restante:
                lote_atual.quantidade_estoque -= quantidade_restante
                quantidade_restante = 0

            else:
                quantidade_restante -= lote_atual.quantidade_estoque
                fila_do_produto.desenfileirar()
                lote_atual = fila_do_produto.inicio.dado if fila_do_produto.inicio else None

        if quantidade_restante > 0:
            raise ValueError('Estoque insuficiente para atender a baixa solicitada')


class Produto:
    def __init__(self, nome_produto:str, preco_compra:float|int, preco_venda:float|int, data_compra:str, data_vencimento:str, quantidade_estoque:int):
        self._nome_produto = None
        self._preco_compra = 0
        self._preco_venda = 0
        self._data_compra = None
        self._data_vencimento = None
        self._quantidade_estoque = 0

        self.nome_produto = nome_produto
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_vencimento = data_vencimento
        self.quantidade_estoque = quantidade_estoque

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
            valor = datetime.strptime(valor, "%d/%m/%Y")
            self._data_compra = valor
        except (ValueError, TypeError):
            raise ValueError('Data de Compra Inválida')

    @property
    def data_vencimento(self):
        return self._data_vencimento
        
    @data_vencimento.setter
    def data_vencimento(self, valor:str):
        
        try:
            valor = datetime.strptime(valor, "%d/%m/%Y")
            self._data_vencimento = valor
        except (ValueError, TypeError):
            raise ValueError('Data de Vencimento Inválida')

    @property
    def quantidade_estoque(self):
        return self._quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, valor:int):
        if isinstance(valor, int) and not isinstance(valor, bool) and valor >= 0:
            self._quantidade_estoque = valor
        else:
            raise ValueError('Quantidade inválida')

    
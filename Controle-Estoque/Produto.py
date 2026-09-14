
class Produto:
    def __init__(self, nome:str, preco_compra:float, preco_venda:float, data_compra:str, data_vencimento:str, quantidade_estoque:int):
        self._nome_produto = nome
        self._preco_compra = preco_compra
        self._preco_venda = preco_venda
        self._data_compra = data_compra
        self._data_vencimento = data_vencimento
        self._quantidade_estoque = quantidade_estoque




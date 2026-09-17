from ControleComanda import comanda
from ControleEstoque import estoque
from EstruturaDados import lista_encadeada, fila
from GeradorFaker import gerador

c = comanda.Comanda(1, "Maria Silva")
print(c)

produto = estoque.Produto("Coxinha de Frango", 3.50, 8.50, "01/09/2026", "25/09/2026", 50)
print(produto)
 
e = estoque.Estoque()
e.repor_estoque(produto)
print(e)

lista = lista_encadeada.ListaEncadeada()
lista.adicionar_dados("item")
print(lista)
 
f = fila.Fila()
print(f)
    
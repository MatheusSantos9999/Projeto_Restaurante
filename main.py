from ControleComanda import Comanda
from EstruturaDados import lista_encadeada
from GeradorFaker import gerador


clientes = gerador.gerador_cliente(20)
lista = lista_encadeada.ListaEncadeada()

for nome, numero in clientes:
    cliente = Comanda.Comanda()
    cliente.abrir_comanda(nome, numero)
    lista.adicionar_dados(cliente)
    
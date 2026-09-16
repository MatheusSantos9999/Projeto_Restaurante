from faker import Faker


def gerador_cliente(numero):

    fk = Faker(locale='pt-BR')
  
    lista_cliente = []

    num_comanda = 0

    for _ in range(0, numero):
        nome = fk.name()
        num_comanda += 1

        lista_cliente.append((nome, num_comanda))

    return lista_cliente


    

        


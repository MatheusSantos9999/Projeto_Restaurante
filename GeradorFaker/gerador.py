from faker import Faker


def gerador_cliente(numero):

    fk = Faker(locale='pt-BR')
    """
    cardapio_salgados = {
        'Coxinha de Frango': 8.00,
        'Pastel de Carne': 10.00,
        'Pastel de Calabresa': 12.00,
        'Pastel 3 queijos': 10.00,
        'Empada de Frango': 8.00,
        'Empada de Palmito': 9.00,
        'Kibe': 7.50,
        'Pão de Queijo': 3.00,
        'Bolinho de Bacalhau': 8.00
    }

    cardapio_bebidas = {
        'Coca-Cola 600ml': 6.00,
        'Coca-Cola 350ml': 5.00,
        'Caldo de Cana 2L': 12.00,
        'Coca-Cola 2L': 14.50,
        'Pepsi 2L': 13.50
                        }
    """

    lista_cliente = []

    num_comanda = 0

    for _ in range(0, numero):
        nome = fk.name()
        num_comanda += 1

        lista_cliente.append((nome, num_comanda))

    return lista_cliente


    

        


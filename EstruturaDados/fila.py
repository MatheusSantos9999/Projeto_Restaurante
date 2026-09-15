class No:
    def __init__(self, dado=None):
        self.dado = dado 
        self.proximo = None

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enfileirar(self, dado):

        if self.inicio == None:
            no_dado = No(dado) 
            self.inicio = no_dado 
            self.fim = no_dado 
            
        else:
            no_dado = No(dado) 
            self.fim.proximo = no_dado 
            self.fim = no_dado 

        self.tamanho += 1

    def desenfileirar(self):
        atual = self.inicio

        if atual is not None:
            self.inicio = atual.proximo
            self.tamanho -= 1

            if atual.proximo == None:
                self.fim = None
            return atual.dado
        else:
            return None
           
            
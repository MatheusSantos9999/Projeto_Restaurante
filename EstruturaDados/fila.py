from rich import inspect

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

            anterior = None
            atual = self.inicio
                
            if dado.data_vencimento < atual.dado.data_vencimento:      
                no_dado = No(dado)
                self.inicio = no_dado
                self.inicio.proximo = atual

            else:
                while atual:
                    if dado.data_vencimento < atual.dado.data_vencimento:
                        no_dado = No(dado)
                        no_dado.proximo = atual
                        anterior.proximo = no_dado
                        break

                    anterior = atual
                    atual = atual.proximo

                if atual == None:
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

          
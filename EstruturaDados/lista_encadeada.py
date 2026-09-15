class No:
    def __init__(self, dado=None):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def adicionar_dados(self, dado):

        if self.inicio == None:
            no_dado = No(dado)
            self.inicio = no_dado
            self.fim = no_dado
           
        else:
            no_dado = No(dado)
            self.fim.proximo = no_dado   
            self.fim = no_dado

        self.tamanho += 1

    def buscar_dados(self, condicao):
        atual = self.inicio

        while atual:
            if condicao(atual.dado):
                return atual.dado
            else:
                atual = atual.proximo

        return None

    def remover_dados(self, condicao):
        atual = self.inicio

        if atual is not None:
            if condicao(atual.dado):
                self.inicio = atual.proximo
                self.tamanho -= 1

                if self.inicio == None:
                    self.fim = None
                        
                return atual.dado

            else:
                anterior = atual
                atual = atual.proximo
                    
                while atual:

                    if condicao(atual.dado):
                        anterior.proximo = atual.proximo
                        self.tamanho -= 1

                        if atual == self.fim:
                            self.fim = anterior 
                        return atual.dado
                        
                    else:
                        anterior = atual
                        atual = atual.proximo

                return None
        else:
            return None

                    




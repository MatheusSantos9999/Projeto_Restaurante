import re
import pickle as pkl
import os
from random import randint

def inserir_refeicoes(salgado, preco):

    refeicoes_padrao = {
        'Coxinha de Frango': 8.50,
        'Pastel 3 Queijos': 15.00,
        'Pastel de Carne': 14.00,
        'Kibe': 7.50,
        'Enroladinho de Presunto e Queijo': 7.50
    }

    

    if isinstance(salgado, str) and isinstance(preco, int,float):
        salgado_limpo = salgado.replace(" ","")
    
        padrao = re.compile(r'([\w-]+)')
    
        checar_valor = padrao.fullmatch(salgado_limpo)
    
        if checar_valor and preco > 0:
            refeicoes_padrao[salgado] = preco

    with open('Projeto-Restaurante/Persistência/refeicoes.pkl', 'wb') as f:
        pkl.dump(refeicoes_padrao, f)

def inserir_bebida(bebida, preco):

    bebidas_padrao = {
        'Coca Cola 600ml': 6.00,
        'Coca Cola 2L': 14.00,
        'Pepsi 600ml': 7.00,
        'Pepsi 2L': 13.50,
    }


    if isinstance(bebida, str) and isinstance(preco, int,float):
        bebida_limpa = bebida.replace(" ","")
    
        padrao = re.compile(r'([\w-]+)')
    
        checar_valor = padrao.fullmatch(bebida_limpa)
    
        if checar_valor and preco > 0:
            bebidas_padrao[bebida] = preco

    with open('Projeto-Restaurante/Persistência/bebidas.pkl', 'wb') as f:
        pkl.dump(bebidas_padrao, f)


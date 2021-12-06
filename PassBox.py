import itertools
import string
import sys
from typing import Sequence
#primeiro nome
nome = input('Primeiro nome:')
#Sobrenome
sobrenome = input('Sobrenome:')
#Nickname
nickname = input('Apelido/Nick:')
#Aniversário
aniversario = input('Aniversário:')
#Time de Futebol
time = input('Time:')

#Nome Companheiro(a)
nome_companheiro = input('Nome companheiro(a):')
#Nick Companheiro(a)
nick_companheiro = input('Nick/Apelido Companheiro(a)')
#Aniversário Companheiro(a)
aniversario_companheiro = input('Aniversário companheiro(a):')

#Nome Filho(a)
nome_filho = input('Nome do filho(a):')
#Nick Filho(a)
nick_filho = input('Nick/Apelido Filho(a):')
#Aniversário Filho(a)
aniversario_filho = input('Anviersário Filho(a):')

#Nome Pet
nome_pet = input('Nome do Pet:')

#Deseja adicionar simbolos ?
simbolos = string.punctuation
#Deseja adicionar numero aletorios ?
numeros = string.digits

#Aonde criar arquivo
Arquivo = input('Aonde criar arquivo:')

def CriandoWordlist():
    def Alvo():
        pass

    def Companheiro():
        pass

    def Filhos():

        pass

    yield
#criar arquivo.txt
output = open(Arquivo, "a")
output.write(CriandoWordlist())
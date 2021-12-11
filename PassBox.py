import datetime
import itertools
import string
#primeiro nome
nome = input('Primeiro nome:')
#Sobrenome
sobrenome = input('Sobrenome:')
#Nickname
nickname = input('Apelido/Nick:')
#Aniversário
data = input("EX -> 01/01/1111 data:")
aniversario = datetime.datetime.strptime(data, "%d/%m/%Y")
#Time de Futebol
time = input('Time:')

#Nome Companheiro(a)
##nome_companheiro = input('Nome companheiro(a):')
#Nick Companheiro(a)
##nick_companheiro = input('Nick/Apelido Companheiro(a)')
#Aniversário Companheiro(a)
##data_companheiro = input('Aniversário companheiro(a):')
##aniversario_companheiro = datetime.datetime.strptime(data_companheiro, "%d/%m/%Y")

#Nome Filho(a)
##nome_filho = input('Nome do filho(a):')
#Nick Filho(a)
##nick_filho = input('Nick/Apelido Filho(a):')
#Aniversário Filho(a)
##data_filho = input('Aniversário Filho(a):')
##aniversario_filho = datetime.datetime.strptime(data_filho, "%d/%m/%Y")

#Nome Pet
##nome_pet = input('Nome do Pet:')

#Deseja adicionar simbolos ?
simbolos = string.punctuation
#Deseja adicionar numero aletorios ?
numeros = string.digits

#Aonde criar arquivo
Arquivo = input('Nome do arquivo:')+".txt"
open(Arquivo, "x")
output = open(Arquivo, "w")

info_alvo = [
    nome.lower(),
    nome.capitalize(),
    sobrenome.lower(),
    sobrenome.capitalize(),
    nickname.lower(),
    nickname.capitalize(),
    format(aniversario.day),
    format(aniversario.month),
    format(aniversario.year)
]
def alvo():
    for item in itertools.permutations(info_alvo, 2):
        ss = "".join(item)
        output.write(ss+'\n')
        
          
def companheiro():

    pass

def filhos():

    pass

#criar arquivo.txt
#output = open(Arquivo, "a")
#output.write(CriandoWordlist)

if __name__ == '__main__':
    alvo()
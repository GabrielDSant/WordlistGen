import datetime
import string
import sys
#primeiro nome
nome = input('Primeiro nome:')
#Sobrenome
sobrenome = input('Sobrenome:')
#Nickname
nickname = input('Apelido/Nick:')
#Aniversário
data = input("data:")
aniversario = datetime.datetime.strptime(data, "%d/%m/%Y")
#Time de Futebol
time = input('Time:')

#Nome Companheiro(a)
nome_companheiro = input('Nome companheiro(a):')
#Nick Companheiro(a)
nick_companheiro = input('Nick/Apelido Companheiro(a)')
#Aniversário Companheiro(a)
data_companheiro = input('Aniversário companheiro(a):')
aniversario_companheiro = datetime.datetime.strptime(data_companheiro, "%d/%m/%Y")

#Nome Filho(a)
nome_filho = input('Nome do filho(a):')
#Nick Filho(a)
nick_filho = input('Nick/Apelido Filho(a):')
#Aniversário Filho(a)
data_filho = input('Aniversário Filho(a):')
aniversario_filho = datetime.datetime.strptime(data_filho, "%d/%m/%Y")

#Nome Pet
nome_pet = input('Nome do Pet:')

#Deseja adicionar simbolos ?
simbolos = string.punctuation
#Deseja adicionar numero aletorios ?
numeros = string.digits

#Aonde criar arquivo
Arquivo = input('Aonde criar arquivo:')

info_alvo = [
    nome.lower(),
    nome.capitalize(),
    sobrenome.lower(),
    sobrenome.capitalize(),
    nickname.lower(),
    nickname.capitalize(),
    aniversario.day,
    aniversario.month,
    aniversario.year]

info_companheiro = [
    nome_companheiro.lower(),
    nome_companheiro.capitalize(),
    nick_companheiro.lower(),
    nick_companheiro.capitalize(),
    aniversario_companheiro.day,
    aniversario_companheiro.month,
    aniversario_companheiro.year,]

info_filho = [
    nome_filho.lower(),
    nome_filho.capitalize(),
    nick_filho.lower(),
    nick_filho.capitalize,
    aniversario_filho.day,
    aniversario_filho.month,
    aniversario_filho.year]

info_pet = [
    nome_pet.lower(), 
    nome_pet.capitalize()]
def CriandoWordlist():
    def alvo():
        pass

    def companheiro():

        pass

    def filhos():

        pass

#criar arquivo.txt
#output = open(Arquivo, "a")
#output.write(CriandoWordlist)

if __name__ == '__main__':
    print(info_alvo)
    pass
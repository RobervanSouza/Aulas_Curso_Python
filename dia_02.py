# # Função
# from exercicios_dia_01 import n1, n2
#
# aluno = 'robervan'
# def bem_vindo(name):
#     msg = 'ola ' + name.capitalize()  # primera letra maiuscula
#     print(msg)
# bem_vindo(aluno)
# print(bem_vindo)
# def teste (n1, n2):
#     print('Resultado da soma: ', soma)
#     print(f'Resultado da soma: {soma} ')  # em vez de usar o + ou virgula, o F junta tudo
# n1 = int(input('digite o primeiro numero: __'))
# n2 = int(input('digite o segundo numero: __'))
# soma = n1 + n2
#
# teste(n1, n2)
########################333333333333333333333333333333333333#############################
# Return
from exercicios_dia_01 import n1, n2


# def function(n1, n2):
#     return n1 + n2
# n1 = int(input('digite o primeiro numero '))
# n2 = int(input('digite o segundo numero '))
# result = function(n1, n2)
# print(result)
# function(n1, n2)
def nome(name, email, id):
    msg = f" Olá aluno {name}, seu email e {email} e sue ID e {id}"
    print(msg)
    return msg
n1 = input('digite seu nome  ')
n2 = input('digite seu email  ')
n3 = int(input('digite seu id  '))
nome(n1, n2, n3)




















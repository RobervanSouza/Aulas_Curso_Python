# ################## calculo que ano nasceu
# # ano_atual = 2022
# # idade_atual = 33
# # ano_nasceu = ano_atual - idade_atual
# # print('Você nasceu em:', ano_nasceu)
# # # o operador + pode concatenar(unir duas strigs)
# # r = 'robervan'
# # s = '100'
# # soma = r + s
# # print(soma)
# ########################################################33333333333333
# # variavel listas e tuples
#
# lista = ['robervan', 'auriene', 'beatriz', 'alice']
# lista.append('teste'),  # o append adiciona item no final da lista
# print('quantidade de elementos:',len(lista), 'lista completa:', (lista))
# ## Verificando se existe o item na lista
# if 'roberv' in lista:
#     print('sim, tem sim robervan nessa lista:', lista)
# else:
#     print('não exist nessa lista:', lista)
# ###########
# ## Retorna o número de vezes que o valor aparece na fruitslista:
# total_vezes = lista.count("teste")
# print(total_vezes)
# ## adiciona novo e teste no lugar do item 1
# lista[3:2] = ['novo', 'teste']
# print(lista)
# # remove o ultimo elemento
# lista.pop()
# print(lista)
# lista.remove("teste") # remove exatamente o item desejado
# print(lista)
# teste1= 'robervan'
# lista.append("teste1")
# lista.append(teste1)
# lista.insert(0, teste1) # insere um item no inicio da lista ou posição que desejar
# lista.reverse()
# print(lista)
# #######################33#########################################
# # tuple
# lista1 = {'robervan', 'auriene', 'beatriz', 'alice'}
# print('robervan' in lista1)# verifica se esta na lista
# #######################33#########################################
# dicionario
aluno = {
    'nome': 'Robervan',
    'idade': 33,
    'brasil': True,
    'comida':['arroz','feijão', 'carne']
}
print(type(aluno), (aluno)) # tipo de dicionario dict
print(len(aluno)) # quantos itens tem no dicionario

del aluno['nome'] # deleta nome da lista
print(aluno['idade']) # busca a idade na lista
aluno['nome'] = 'auriene' # muda o nome do dicionario ou adiciona

print(aluno.keys(), 'estou aqui')
teste= [{
    'nome': 'Roberqweqweqweqwevan',
    'idade': 33,
    'brasil': True,
    'comida':['arroz','feijão', 'carne']
}, {
    'nome': 'Robervadasdasdasdasdsan',
    'idade': 33,
    'brasil': True,
    'comida':['arroz','feijão', 'carne']
},{
    'nome': 'Robervan',
    'idade': 33,
    'brasil': True,
    'comida':['arroz','feijão', 'carne']
}]
print(teste[1]['brasil']) # buca na lista 1 o que esta no brasil
for aluno in teste:
    print('nome do aluno: ',aluno['nome'],'idade do aluno:', aluno['idade']) # lista somente quantos alunos e as idades



















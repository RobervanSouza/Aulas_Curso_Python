################## calculo que ano nasceu
# ano_atual = 2022
# idade_atual = 33
# ano_nasceu = ano_atual - idade_atual
# print('Você nasceu em:', ano_nasceu)
# # o operador + pode concatenar(unir duas strigs)
# r = 'robervan'
# s = '100'
# soma = r + s
# print(soma)
########################################################33333333333333
# variavel listas e tuples

lista = ['robervan', 'auriene', 'beatriz', 'alice']
lista.append('teste'),  # o append adiciona item no final da lista
print('quantidade de elementos:',len(lista), 'lista completa:', (lista))
## Verificando se existe o item na lista
if 'roberv' in lista:
    print('sim, tem sim robervan nessa lista:', lista)
else:
    print('não exist nessa lista:', lista)
###########
## Retorna o número de vezes que o valor aparece na fruitslista:
total_vezes = lista.count("teste")
print(total_vezes)
## adiciona novo e teste no lugar do item 1
lista[3:2] = ['novo', 'teste']
print(lista)
# remove o ultimo elemento
lista.pop()
print(lista)
lista.remove("teste") # remove exatamente o item desejado
print(lista)
teste1= 'robervan'
lista.append("teste1")
lista.append(teste1)
lista.insert(0, teste1) # insere um item no inicio da lista ou posição que desejar
lista.reverse()
print(lista)
#######################33#########################################
# tuple
lista1 = {'robervan', 'auriene', 'beatriz', 'alice'}
print('roberva' in lista1)# verifica se esta na lista
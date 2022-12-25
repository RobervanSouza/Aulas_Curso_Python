# adicionar
def add_food(name='', description=''):
    if type(name) is not str or type(description) is not str:
        print('isso não e string, ambos precisa ser string')
    elif name == '' or description == '':
        if name == '':
            print(f'{description} falta a nome')
        else:
            print(f'o nome e: {name} falta passar descrição')
            print('precisa passar o nome da comida mais a descrição')
    elif name in food_list:
        print(f' a comida {name} ja existe')
    else:
        food_list[name] = description
        print(f'a comida {name} foi cadastrada com sucesso')
########################################################################
#   delete
def delete_food(name=''):
    if type(name) is not str:
        print(f' {name}, precisa ser string')
    elif name == '':
        print(f'precisa passar algo para deletar')
    elif name in food_list:
        del food_list[name]
        print(f"'{name}' deletado com sucesso")
    else:
        print(f"'{name}' não exist na lista'")
################################################################################################
# update
def update_food(name='', new_description=''):
    if type(name) is not str or type(new_description) is not str:
        print(f"o nome: '{name}', e a descrição: '{new_description}'precisam ser string")
    elif name == '' or new_description == '':
        print('voce precisa passar o nome mais a descrição')
    elif name in food_list:
        food_list[name] = new_description
        print(f"nova comida: '{new_description}'")
    else:
        print(f'{name} não existi na lista')
#####################################################################################################33333333
# get
def get_food(comida=''):
    if type(comida) is not str:
        print(f"a comida '{comida}' precisa ser string")
    elif comida == '':
        print(f"você precisa passar o nome da comida")
    elif comida in food_list:
        desc = food_list[comida]
        print(f"a comida '{comida}' a descrição e: {desc}")
    else:
        print(f"não exist a comida '{comida}' em food")


# #### Comentei o código todo explicando ele para ajudar no entendimento.
# ### Comentar é sempre uma boa prática.
#
# def add_food(name='', description=''):
#     # verifica se ambos sao string
#     if type(name) is not str or type(description) is not str:
#         print('Ambos os valores precisam ser do tipo string')
#
#     # verifica se ambos foram passados
#     elif name == '' or description == '':
#         print('Você precisa passar o nome da comida + descrição')
#
#     # verifca se comida ja existe no dicionario
#     elif name in food_list:
#         print(f'{name} já está cadastrado no dicionário')
#
#     # se chegou aqui é pq é string, foi passado os valores e ainda não está no dicionário,
#     # então vou cadastrar no dicionario
#     else:
#         food_list[name] = description
#         print(f'{name} cadastrado com sucesso!')
#
#
# def delete_food(name=''):
#     # verifica se é string
#     if type(name) is not str:
#         print('O nome da comida precisa ser do tipo string')
#
#     # verifica se foi passado
#     elif name == '':
#         print('Você precisa passar o nome da comida para deletar')
#
#     # se estiver no dicionario então deleta
#     elif name in food_list:
#         del food_list[name]
#         print(f'{name} foi deletado com sucesso!')
#
#     # caso seja string, foi passado, mas nao esta no dicionario falar que nao existe
#     # afinal não tem como deletar algo que não existe.
#     else:
#         print(f'{name} não existe no dicionário')
#
#
# def update_food(name='', new_description=''):
#     # verifica se ambos sao string
#     if type(name) is not str or type(new_description) is not str:
#         print('Ambos os valores precisam ser do tipo string')
#
#     # verifica se ambos foram passados
#     elif name == '' or new_description == '':
#         print('Você precisa passar o nome da comida + nova descrição')
#
#     # verifca se comida ja existe no dicionario, se ja existe então atualiza
#     elif name in food_list:
#         food_list[name] = new_description
#         print(f'{name} descrição atualizada para: {new_description}')
#
#     # se é string, foi passada, mas nao existe no dicionario falar que nao existe
#     # afinal nao tem como atualiza algo que nao existe.
#     else:
#         print(f'{name} não existe no dicionário')
#
#
# def get_food(name=''):
#     # verifica se é string
#     if type(name) is not str:
#         print('O nome da comida precisa ser do tipo string')
#
#     # verifica se foi passado
#     elif name == '':
#         print('Você precisa passar o nome da comida para consultar a descrição')
#
#     # se estiver no dicionario então imprime a descrição dela
#     elif name in food_list:
#         desc = food_list[name]
#         print(f"A descrição de {name} é: {desc}")
#
#     # caso seja string, foi passado, mas nao esta no dicionario falar que nao existe.
#     # afinal, nao tem como consulta a descricao de uma comida que nao existe.
#     else:
#         print(f'{name} não existe no dicionário')
#

#####!! NÃO EDITE O CÓDIGO ABAIXO DESTA LINHA !!#####

# criação da food_list
food_list = {
    'paçoquinha': 'Um doce de amendoím brasileiro',
    'brigadeiro': 'Um doce muito delicioso',
    'pizza': 'um tipo de comida da italia',
    'hamburguer': 'comida dos USA'
}

#####################################
######## TESTES ADD_FOOD #########
#####################################

# ADD_FOOD - TESTE 1
print("\n#### ADD_FOOD - TESTE 1")
print("Usando add_food com valores sendo int")
print("add_food(100, 23)\n")
# excuta:
add_food(100, 23)

# ADD_FOOD - TESTE 2
print("\n#### ADD_FOOD - TESTE 2")
print("Usando add_food sem passar a descrição.")
print("add_food('pizza')\n")
# excuta:
add_food('pizza')

# ADD_FOOD - TESTE 3
print("\n#### ADD_FOOD - TESTE 3")
print("Usando add_food com comida já existente.")
print("add_food('brigadeiro', 'Um doce brasileiro')\n")
# excuta:
add_food('brigadeiro', 'Um doce brasileiro')

# ADD_FOOD - TESTE 4
print("\n#### ADD_FOOD - TESTE 4")
print("Usando add_food adicionando uma comida.")
print("add_food('lasanha', 'Camadas de massa e molho')\n")
# excuta:
add_food('lasanha', 'Camadas de massa e molho')

#####################################
######## TESTES DELETE_FOOD #########
#####################################

# DELETE_FOOD - TESTE 1
print("\n#### DELETE_FOOD - TESTE 1")
print("Usando delete_food com valor sendo int")
print("delete_food(100)\n")
# excuta:
delete_food(100)

# DELETE_FOOD - TESTE 2
print("\n#### DELETE_FOOD - TESTE 2")
print("Usando delete_food sem nenhum valor.")
print("delete_food()\n")
# excuta:
delete_food()

# DELETE_FOOD - TESTE 3
print("\n#### DELETE_FOOD - TESTE 3")
print("Usando delete_food com comida que não existe na lista.")
print("delete_food('massa')\n")
# excuta:
delete_food('massa')

# DELETE_FOOD - TESTE 4
print("\n#### DELETE_FOOD - TESTE 4")
print("Usando delete_food removendo uma comida.")
print("delete_food('paçoquinha')\n")
# excuta:
delete_food('paçoquinha')

#####################################
## TESTES UPDATE_FOOD ##
#####################################

# UPDATE_FOOD - TESTE 1
print("\n#### UPDATE_FOOD - TESTE 1")
print("Usando update_food com valores sendo int")
print("update_food(100, 23)\n")
# excuta:
update_food(100, 23)

# UPDATE_FOOD - TESTE 2
print("\n#### UPDATE_FOOD - TESTE 2")
print("Usando update_food sem passar a descrição.")
print("update_food('pizza')\n")
# excuta:
update_food('pizza')

# UPDATE_FOOD - TESTE 3
print("\n#### UPDATE_FOOD - TESTE 3")
print("Usando update_food com comida não existente.")
print("update_food('sorvete', 'Um doce gelado da italia')\n")
# excuta:
update_food('sorvete', 'Um doce gelado da italia')

# UPDATE_FOOD - TESTE 4
print("\n#### UPDATE_FOOD - TESTE 4")
print("Usando update_food e atualizando uma comida.")
print("update_food('brigadeiro', 'Melhor doce do mundo.')\n")
# excuta:
update_food('brigadeiro', 'Melhor doce do mundo.')

#####################################
## TESTES GET_FOOD ##
#####################################

# GET_FOOD - TESTE 1
print("\n#### GET_FOOD - TESTE 1")
print("Usando get_food com valor sendo int")
print("get_food(505)\n")
# excuta:
get_food(505)

# GET_FOOD - TESTE 2
print("\n#### GET_FOOD - TESTE 2")
print("Usando get_food sem passar a comida.")
print("get_food()\n")

get_food()

# GET_FOOD - TESTE 3
print("\n#### GET_FOOD - TESTE 3")
print("Usando get_food com comida não existente.")
print("get_food('noodle')\n")
get_food('noodle')

# GET_FOOD - TESTE 4
print("\n#### GET_FOOD - TESTE 4")
print("Usando get_food e pesquisando a descrição uma comida.")
print("get_food('hamburguer')\n")
get_food('hamburguer')

#####!!!!!!!!!!!!!! THE END !!!!!!!!!!!!!!#####


## Linha de Chegada ##
print("\n Winners win")
print(u"\U0001F40D" + " Maratona Python")
# © 2020 Maratona Python. Todos os direitos reservados.
# https://www.maratonapython.com.br





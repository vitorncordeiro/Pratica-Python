"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre
um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa
no crime. Se a pessoa responder positivamente a 2 
questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente" """
respostasPositivas = 0
classificacao = "Inocente"
perguntas = ['Telefonou para a vítima? ', 'Esteve no local do crime? ', \
             'Mora perto da vítima? ', 'Devia para a vítima? ', 'Já trabalhou com a vítima? ']
for pergunta in perguntas:
    resposta = input(pergunta).lower()
    if resposta.startswith('s'):
        respostasPositivas += 1
if respostasPositivas == 2:
    classificacao = 'Suspeito'
elif respostasPositivas > 2 and respostasPositivas < 5:
    classificacao = 'Cúmplice'
elif respostasPositivas == 5:
    classificacao = 'Assassino'
print(classificacao)


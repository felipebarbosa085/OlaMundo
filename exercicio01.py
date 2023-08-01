'''
Elabore um programa que pergunte ao aluno suas três notas escolares,
O programa deverá caucular a media das 3 notas inserida e exibir
'''

nome = input("Olá aluno, Qual o seu nome?")
print("Olá," ,nome, "Esse é um programa que caucula suas notas escolares!")
nota1 = float(input("Informe sua primera nota"))
nota2 = float(input("Informe sua Segunda nota"))
nota3 = float(input("Informe sua Terceira nota"))

media = (nota1 + nota3 + nota2) /3
print(media)
if media>5.9:
 print("Parabéns,você passou! ")
if media<6.0:
 print("Que pena! Fa recuperaçâo será realizada na data 22/11")
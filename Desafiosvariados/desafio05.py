#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

def notaMedia():
    media= sum(notas)/len(notas)
    return media


notas = [7.5,8.0,10.0,9.0]
print(notaMedia())
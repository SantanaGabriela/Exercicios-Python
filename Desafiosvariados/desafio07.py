# Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

string_1 = "Olá, Mundo"
string_2 = "Olá, Gente"

#informando o conteúdo e o tamanho das strings

print(f" A string 01 possui contéudo: {string_1} que tem {len(string_1) } caracteres")
print(f" A string 02 possui contéudo: {string_2} que tem {len(string_2) } caracteres")

def comparaTamanho():
    if len(string_1) == len(string_2):
        print(" As strings possuem o mesmo tamanho")
    else:
        print("As strings não possuem o mesmo tamanho")


comparaTamanho()

def comparaString():
    if string_1 in string_2:
        print("Possuem o mesmo contéudo")
    else:
        print("Não possuem o mesmo contéudo")

comparaString()
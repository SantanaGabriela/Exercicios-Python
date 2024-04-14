#Faça um Programa que peça dois números e imprima a soma.
descrição = """
CALCULADORA DE SOMA.

Informe dois números e obtenha um resultado!
"""

print(descrição)

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite um número: "))

soma = numero_1 + numero_2

print(f" A soma de {numero_1} + {numero_2} é igual a = {soma}")
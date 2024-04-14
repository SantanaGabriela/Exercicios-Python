#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto,que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto(taxaImposto,custo):
    custo = custo * (1 + taxaImposto / 100)

    return custo


taxaImposto =float(input("Digite a taxa de imposto em porcentagem: "))
custo = float(input("Digite o custo do item: "))

# Chama a função e imprime o resultado
print("Custo total com imposto: R$", somaImposto(taxaImposto, custo))
    


    
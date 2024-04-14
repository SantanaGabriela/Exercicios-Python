def eh_consoante(caractere):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return caractere in consoantes

caracteres = ["a", "c", "d", "r", "e", "i", "u", "k", "l", "o"]

# Verificar se cada caractere é uma consoante e imprimir o resultado
for caractere in caracteres:
    print(caractere, eh_consoante(caractere))
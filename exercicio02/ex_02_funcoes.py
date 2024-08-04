'''Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.'''

def reverso(numero):
    string = str(numero)

    string_reversa = string[::-1]

    numero_reverso = int(string_reversa)

    return numero_reverso


input= int(input("Digite um número: "))

reverso_numero = reverso(input)

print(f"O reverso de {input} é {reverso_numero}")
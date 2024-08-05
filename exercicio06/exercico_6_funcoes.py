"""Vamos construir um jogo de forca. O programa escolherá
aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
secreta será representada por espaços em branco, um para cada letra
da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser
informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número
máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício"""

import random

def escolher_palavra():
    # Lista de palavras secretas para o jogo

    palavras = ["python", "programacao", "desenvolvimento", "computador", "tecnologia"]

    # Escolhe uma palavra aleatória da lista

    return random.choice(palavras)

def jogo_da_forca():
    # Escolhe a palavra secreta

    palavra_secreta = escolher_palavra()
    # Cria a representação inicial da palavra, com espaços para cada letra

    palavra_oculta = ["_"] * len(palavra_secreta)
    # Define o número máximo de tentativas

    tentativas_restantes = 6
    # Lista para armazenar letras erradas

    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")

    # Loop do jogo
    while tentativas_restantes > 0:
        # Mostra o estado atual da palavra oculta e letras erradas

        print("\nPalavra: ", " ".join(palavra_oculta))
        print(f"Tentativas restantes: {tentativas_restantes}")
        print("Letras erradas: ", " ".join(letras_erradas))

        # Solicita uma letra ao usuário
        tentativa = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi tentada
        if tentativa in letras_erradas or tentativa in palavra_oculta:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        # Verifica se a tentativa é uma letra válida
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra.")
            continue

        # Verifica se a letra está na palavra secreta
        if tentativa in palavra_secreta:
            # Atualiza a palavra oculta com a letra correta
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i] == tentativa:
                    palavra_oculta[i] = tentativa
        else:
            # Adiciona a letra à lista de letras erradas
            letras_erradas.append(tentativa)
            # Diminui o número de tentativas restantes
            tentativas_restantes -= 1
            print("Letra incorreta.")

        # Verifica se a palavra foi adivinhada
        if "_" not in palavra_oculta:
            print("\nParabéns! Você adivinhou a palavra:", palavra_secreta)
            break

    # Verifica se o jogador perdeu
    if tentativas_restantes == 0:
        print("\nVocê perdeu! A palavra era:", palavra_secreta)

# Executa o jogo
if __name__ == "__main__":
    jogo_da_forca()
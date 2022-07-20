import random
from imagens import vidas
from imagens import logo
from lista_nomes import word_list


fim_game = False
vida = 6
palavra = random.choice(word_list)
#print(f'Pssst, the solution is {palavra}.')

print(logo)

display = []
for letra in palavra:
    display += "_"
qtde_letras = len(display)

print("BEM VINDO AO HANGMAN - JOGO DA FORCA!")
print(vidas[vida])
print(f"É um animal com {qtde_letras} letras: ")
print(f"{' '.join(display)}\n")



while fim_game == False:
    escolha = input("Diga uma letra que tenha no nome desse animal? = ").lower()
    print(escolha)

    for posicao in range(len(palavra)):
        letra = palavra[posicao]
        if letra == escolha:
            display[posicao] = letra
    
    
    if escolha not in letra:
        print("Esta palavra não tem esta letra. Você perdeu uma vida!")
        vida -= 1
        if vida == 0:
          fim_game = True
          print("Você perdeu a sua última chance: \nGame Over!") 

    print(vidas[vida])
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        fim_game = True
        print("Você venceu!")
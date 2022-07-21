import random
from imagens import vidas
from imagens import logo
from lista_nomes import word_list
def vida_letra():
    print(vidas[vida])
    print(f"{' '.join(display)}\n")

parar_jogo = False
while parar_jogo == False:
    fim_game = False
    vida = 6
    palavra = random.choice(word_list)


    print(logo)

    display = []
    for letra in palavra:
        display += "_"
    qtde_letras = len(display)

    print("BEM VINDO AO HANGMAN - JOGO DA FORCA!")
    print(vidas[vida])
    print(f"Descubra o nome do animal com {qtde_letras} letras: \n")
    print(f"{' '.join(display)}\n")


    while fim_game == False:
        escolha = input("Diga uma letra que tenha no nome desse animal?= ").lower()
    

        for posicao in range(len(palavra)):
            letra = palavra[posicao]
            if letra == escolha:
                display[posicao] = letra
                print("\nOk, Você está no caminho certo.\n")
                vida_letra()
                
        
        if escolha not in palavra:
            print("\nEsta palavra não tem esta letra. Você perdeu uma vida!\n")
            vida -= 1
            vida_letra()
            
            if vida == 0:
                fim_game = True
                vida_letra()
                print("\nVocê perdeu a sua última chance: \nGAME OVER!") 
                parar_jogo = True
    
        if "_" not in display:
            fim_game = True
            vida_letra()
            print("\nPARABENS!\nVocê venceu!\n")
            parar_jogo = True
    novamente = input("JOGAR NOVAMENTE? ").lower()
    print(novamente)
    if novamente == "s":
        parar_jogo = False
            

        
    
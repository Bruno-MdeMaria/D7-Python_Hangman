import random
from imagens import vidas
from imagens import logo
from lista_nomes import word_list
def vida_letra():
    print(vidas[vida])
    print(f"{' '.join(display)}\n")


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

  
    if "_" not in display:
        fim_game = True
        vida_letra()
        print("Você venceu!")

        
    
  

                     
  



#DO-1 - Escolha aleatoriamente uma palavra da lista_palavras e atribua-a a uma variável chamada palavra_escolhida.

#TO-2 - Peça ao usuário que adivinhe uma letra e atribua sua resposta a uma variável chamada escolha. Faça adivinhar minúsculas.

#T-3 - Verifique se a letra que o usuário adivinhou é uma das letras da palavra escolhida.
#Testing code


#Criar uma lista vazia chamada display.
#Para cada letra na palavra_escolhida, adicione um "_" a 'exibir'.
#Então, se a palavra escolhida for "maçã", a exibição deve ser ["_", "_", "_", "_", "_"] com 5 "_" representando cada letra a ser adivinhada.



#2: - Percorrer cada posição na palavra escolhida;
#Se a letra nessa posição corresponder a 'adivinha', revele essa letra no visor nessa posição.
#por exemplo. Se o usuário adivinhou "p" e a palavra escolhida foi "maçã", então a exibição deve ser ["_", "p", "p", "_", "_"].

#Imprima 'display' e você deverá ver a letra adivinhada na posição correta e todas as outras letras substituídas por "_".
#Dica - Não se preocupe em fazer o usuário adivinhar a próxima letra. Vamos resolver isso na etapa 3.
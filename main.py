import random
word_list = ["camelo", "elefante", "gato"]

palavra = random.choice(word_list)
print(f'Pssst, the solution is {palavra}.')

display = []
for letra in palavra:
    display += "_"
print(display)

fim_game = False
while fim_game == False:
    escolha = input("Diga uma letra que tenha na palavra? = ").lower()
    print(escolha)

    for posicao in range(len(palavra)):
        letra = palavra[posicao]
        if letra == escolha:
            display[posicao] = letra
    print(display)
    if "_" not in display:
        fim_game = True
        print("Você venceu!")

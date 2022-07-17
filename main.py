import random
word_list = ["camelo", "elefante", "gato"]

palavra = random.choice(word_list)
print(f'Pssst, the solution is {palavra}.')

verificar = False
while verificar == False:
    escolha = input("Diga uma letra que tenha na palavra? = ").lower()
    print(escolha)

    display = []
    for letra in palavra:
        display += "_"
    print(display)

    for posicao in range(len(palavra)):
        letra = palavra[posicao]
        if letra == escolha:
            display[posicao] = letra
    print(display)
    if "_" not in display:
        verificar = True
        print("Você venceu!")

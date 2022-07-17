import random
word_list = ["aardvark", "baboon", "camel"]
#DO-1 - Escolha aleatoriamente uma palavra da lista_palavras e atribua-a a uma variável chamada palavra_escolhida.

#TO-2 - Peça ao usuário que adivinhe uma letra e atribua sua resposta a uma variável chamada guess. Faça adivinhar minúsculas.

#T-3 - Verifique se a letra que o usuário adivinhou é uma das letras da palavra escolhida.
palavra_escolhida = random.choice(word_list)
print(f'Pssst, the solution is {palavra_escolhida}.')
guess = input("Diga uma letra que tenha na palavra? = ").lower()
print(guess)

display = []
for letra in palavra_escolhida:
    display += "_"
print(display)

for posicao in range(len(palavra_escolhida)):
    letra = palavra_escolhida[posicao]
    if letra == guess:
        display[posicao] = letra
print(display)
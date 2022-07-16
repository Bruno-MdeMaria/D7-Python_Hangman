import random
word_list = ["aardvark", "baboon", "camel"]
#DO-1 - Escolha aleatoriamente uma palavra da lista_palavras e atribua-a a uma variável chamada palavra_escolhida.

#TO-2 - Peça ao usuário que adivinhe uma letra e atribua sua resposta a uma variável chamada guess. Faça adivinhar minúsculas.

#T-3 - Verifique se a letra que o usuário adivinhou é uma das letras da palavra escolhida.
palavra_escolhida = list(random.choice(word_list))
print(palavra_escolhida)
guess = input("Diga uma letra que tenha na palvra? = ").lower()
print(guess)
for letra in palavra_escolhida:
    if letra == guess:
        print(guess)
    else: print("foi mal")
import random

palavras = ["gato","cachorro","peixe","tigre","urso", "passaro"]
with open("texto.txt", "w") as arquivo:
    for _ in range(100000):
        palavra = random.choice(palavras)
        arquivo.write(palavra + " ")




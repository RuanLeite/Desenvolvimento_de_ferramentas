import random, string

tamanho = int(input("Digite o tamanho de senha que deseja: "))
chars = string.ascii_letters + string.digits + 'çÇ!@#$%&*()-+=,.;:/?'

rnd = random.SystemRandom()

print("".join(rnd.choice(chars) for i in range(tamanho)))
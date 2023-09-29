import itertools, string

tamanho = int(input("Digite a quantidade de caracteres que deseja na wordlist: "))
string = string.ascii_letters + string.digits + 'çÇ!@#$%&*()-+=,.;:/?'

resultado = itertools.permutations(string, tamanho)

for i in resultado:
    print(''.join(i))
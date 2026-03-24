import math
x = int(input("Digite um valor inteiro positivo >= 1: "))

S = sum(math.pi / i for i in range(1, x + 1))

M = 1
for i in range(1, x + 1, 2):
    M *=  i / math.pi

print(f"Resultado da Soma: {S:.4f}")
print(f"Resultado da Multiplicação: {M:.4f}")
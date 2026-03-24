altura_m = 0
altura_h = 0
maior_m = 0
maior_h = 0
H = 0
M = 0
for pessoas in range(6):
    sexo = input("Digite o seu sexo (M - MULHER | H - HOMEM): ").upper()
    altura = float(input("Digite a sua altura em metros (ex.: 1.63): "))
    if sexo == 'M':
        M += 1
        altura_m += altura
        while altura > maior_m:
            maior_m = altura
    elif sexo == 'H':
        H += 1
        altura_h += altura
        while altura > maior_h:
            maior_h = altura

print(f"Quantidade de Homens: {H} \n Media de altura dos Homens: {altura_h/H:.2f} \n Homem mais alto: {maior_h}")
print(f"Quantidade de Mulheres: {M} \n Media de altura das Mulheres: {altura_m/M:.2f} \n Mulher mais alta: {maior_m}")
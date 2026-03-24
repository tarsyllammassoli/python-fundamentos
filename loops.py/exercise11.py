temp = 28
temp_media = 0
cont = 0
while temp >= 28:
    temp_dia = int(input("Digite a temperatura do dia: "))
    temp_media += temp_dia
    cont += 1
    if temp_dia < 28:
        break

media = temp_media / cont
print(f"A média de temperatura em Vitória foi de {media:.2f}ºC.")
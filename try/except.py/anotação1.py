try:
    numero = float(input("Digite um número: "))
    resultado = 10 / numero
except ValueError as erro:
    print(f"Não é possível digitar uma Palavra.\nErro ocorrido: {erro}")
except ZeroDivisionError as erro:
    print(f"Não é possível dividir por zero.\n Erro ocorrido: {erro}")
else:
    print(f"O resultado é {resultado:.2f}")
finally:
    print("Fim do Cálculo!")

# tem um comando que é RAISE, onde eu mesma escrevo o tipo de erro que pode acontecer

try:
    idade = int(input("Digite a sua idade: "))
    if idade < 0:
        raise Exception("Digite uma idade válida!")
except Exception as erro:
    print(f"Erro: {erro}")
else:
    if idade > 18:
        print("Você é MAIOR de idade.")
    else:
        print("Você é MENOR de idade.")
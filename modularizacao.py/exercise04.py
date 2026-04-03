def minha_função():
    nome = "Tay"
    print(f"Essa é minha função! Prazer, {nome}!")
    return

minha_função()

def somar(n1, n2):
    resultado = n1 + n2
    print(f"A soma entre {n1} e {n2} é {resultado}")
    return print

numero1 = int(input("1º número: "))
numero2 = int(input("2º número: "))
print(somar(n1=numero1,n2=numero2))

def saudacao(nome):
    print(f"Prazer, {nome}!")

usuario_nome = input("Digite seu nome: ")
saudacao(usuario_nome)

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

usuario_numero = int(input("Digite um número inteiro positivo: "))
if verificar_par(usuario_numero):
    print("É par")
else:
    print("É impar")

# * siginifica o usuário poder enviar quantas caracteristicas quiser

def somar_lista(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

usuario_teste = somar_lista(4, 6, 12, 43, 9, 16)
print(f"O resultado é {usuario_teste}!")

def calcular_media(*numeros):
    qtd = len(numeros)
    soma = 0
    for numero in numeros:
        soma += numero
    media = soma / qtd
    return media

resultado = calcular_media(3,8,4,9)
print(f"A média é {resultado}\n")

# dois ** significa: ele cria um dicionario usando os valores que o usuario envia

def informacoes_pessoais(**informacoes):
    for chave, valor in informacoes.items():
        print(f"{chave}: {valor}")

informacoes_pessoais(nome="Társylla", idade="19", curso="Engenharia de Software")

# exercícios para fazer

def contador(numero):
    for i in range(numero, -1, -1):
        print(i, end=" ")
    return print

usuario_contador = int(input("Digite um número inteiro positivo: "))
contador(usuario_contador)

def maior_numero(lista):
    for i in lista:
        maior = max(lista)
    print(f"\nO maior número da lista é {maior}")
    return print

usuario_lista = [2,8,3,7,12,120]
maior_numero(usuario_lista)
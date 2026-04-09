def calculadora():
    while True:
        menu = input("\n\tDigite alguma das opções abaixo:\n 1 - Entrada de Dados \n 2 - Adição \n 3 - Subtração \n 4 - Multiplicação \n 5 - Divisão \n 6 - Sair \n")
        if menu == '1':
            n1 = int(input("Digite o primeiro número: "))
            n2 = int(input("Digite o segundo número: "))
            continue
        elif menu == '2':
            print(f"{n1} + {n2} = {n1 + n2}")
            continue
        elif menu == '3':
            print(f"{n1} - {n2} = {n1 - n2}")
            continue
        elif menu == '4':
            print(f"{n1} x {n2} = {n1 * n2}")
            continue
        elif menu == '5':
            print(f"{n1} / {n2} = {n1 / n2}")
            continue
        else:
            print("\n\tObrigada por usar nosso programa :)")
            break
    return

calculadora()

## ---------------------------------------------------------------

import math

def raio_circulo(raio):
    area = math.pi * raio**2
    return area

circulo = int(input("Digite o valor do raio do circulo: "))
resultado = print(f"A área do círculo é: {raio_circulo(circulo):.2f}")

## ---------------------------------------------------------------

def conta_cilindro(raio, h):
    conta = math.pi * (raio**2) * h
    return conta

cilindro_raio = int(input("Digite o valor do raio do cilindro: "))
cilindro_altura = int(input("Digite o valor da altura do cilindro: "))
resultado_cilindro = print(f"Resultado: {conta_cilindro(cilindro_raio, cilindro_altura):.2f}")

## ---------------------------------------------------------------

def num_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primo = int(input("Digite um número inteiro positivo entre 2 a 1001 (Para saber se é PRIMO): "))
resultado_primo = print(f"Resultado: {num_primo(primo)}")

## ---------------------------------------------------------------

def the_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    return

sequencia = int(input("Digite um número inteiro positivo: "))
resultado_fibonacci = print(f"Resultado: ")
the_fibonacci(sequencia)
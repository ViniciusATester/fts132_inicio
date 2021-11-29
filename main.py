import math

import pytest

#Cozinheiro
def somar_dois_numeros(num1, num2):
    return num1 + num2
def subtrair_dois_numeros(num1, num2):
    return num1 - num2
def multiplicar_dois_numeros(num1, num2):
    return num1 * num2
def dividir_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

def calcular_area_do_quadrado(lado1):
    return lado1 ** 2

def calcular_area_do_retangulo(base, altura):
    return base * altura

def calcular_area_do_triangulo(base, altura):
    return base * altura / 2

def calcular_area_do_circulo(raio):
    '''return math.pi * raio**2'''

    try:
        return 3.14 * raio ** 2
    except TypeError:
        return 'Falha no calculo - Raio que não é um numero'





if __name__ == '__main__':
#Garçom
    resultado = somar_dois_numeros(7,5)
    print(f'A soma é {resultado}')

    resultado = subtrair_dois_numeros(7,5)
    print(f'A subtração é {resultado}')

    resultado = multiplicar_dois_numeros(7,5)
    print(f'A multiplicação é {resultado}')

    resultado = dividir_dois_numeros(8,2)
    print(f'A divisão é {resultado}')

    resultado = elevar_um_numero_pelo_outro(2,3)
    print(f'A exponenciação é {resultado}')

    resultado = calcular_area_do_quadrado(3)
    print(f'A área do quadrado  é {resultado}')

    resultado = calcular_area_do_retangulo(2,3)
    print(f'A área do retangulo é {resultado}')

    resultado = calcular_area_do_triangulo(2,3)
    print(f'A área do triangulo é {resultado}')

    resultado = calcular_area_do_circulo(3)
    print(f'A area do circulo é {resultado}')


#degustador/teste
'''
def testar_somar_dois_numeros():
    # - 1 Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 8
    num2 = 9
    # Saida / Output
    resultado_esperado = 17

    # - 2 Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3 Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado'''
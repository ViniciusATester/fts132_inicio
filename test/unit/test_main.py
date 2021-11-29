import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros, \
    elevar_um_numero_pelo_outro, calcular_area_do_quadrado, calcular_area_do_retangulo, calcular_area_do_triangulo, \
    calcular_area_do_circulo


def testar_somar_dois_numeros():
    # - 1 Etapa: Configura / Prepara
    # Dados / Valores
    # Entrada / Input
    num1 = 5
    num2 = 4
    # Saida / Output
    resultado_esperado = 9

    # - 2 Etapa: Executa
    resultado_atual = somar_dois_numeros(num1, num2)

    # - 3 Etapa: Confirma / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_subtrair_dois_numeros():
    num1 = 8
    num2 = 3
    resultado_esperado = 5
    resultado_atual = subtrair_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_multiplicar_dois_numeros():
    num1 = 8
    num2 = 3
    resultado_esperado = 24
    resultado_atual = multiplicar_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_dividir_dois_numeros():
    num1 = 100
    num2 = 5
    resultado_esperado = 20
    resultado_atual = dividir_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_elevar_um_numero_pelo_outro():
    num1 = 2
    num2 = 5
    resultado_esperado = 32
    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_quadrado():
    lado1= 5
    resultado_esperado = 25
    resultado_atual = calcular_area_do_quadrado(lado1)
    assert resultado_atual == resultado_esperado


def testar_calcular_area_do_retangulo():
    base = 2
    altura = 5
    resultado_esperado = 10
    resultado_atual = calcular_area_do_retangulo(base, altura)
    assert resultado_atual == resultado_esperado

def testar_calcular_area_do_triangulo():
    base = 2
    altura = 5
    resultado_esperado = 5
    resultado_atual = calcular_area_do_triangulo(base, altura)
    assert resultado_atual == resultado_esperado

#anotação para utilizar como massa de testes
@pytest.mark.parametrize('raio,resultado_esperado',[
    #valores
                             (1, 3.14), #teste n°1
                             (2, 12.56),#teste n°2
                             (3, 28.26),  #teste n°3
                             (4, 50.24),  #teste n°4
                             ('a',  'Falha no calculo - Raio que não é um numero'),  #teste n°5
                             (' ',  'Falha no calculo - Raio que não é um numero'),  #teste n°6
                         ])
def testar_calcular_area_do_circulo(raio, resultado_esperado):
    #raio = 3
    #resultado_esperado = 28.26
    resultado_atual = calcular_area_do_circulo(raio)
    assert resultado_atual == resultado_esperado




# bibliotecas
import time

import pytest  # Framework de teste unitario - engine
import requests  # framework de teste de API - reuestes/respons

# Endereço da API

base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}  # Nos .asmx seria 'text/xml'
token_usuario = ''

# Os testes 
def testar_criar_usuario():
    # Configura

    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '9735'

    # Executa
    resposta = requests.post(  # Faz a requisição, passando:
        url=base_url,  # O endpoint da API
        data=open('C:/Users/vinic/PycharmProjects/fts132_inicio/test/db/user1.json', 'rb'),  # O body Json
        headers=headers  # O header com o Content-Type
    )

    # Formatação
    corpo_da_resposta = resposta.json()  # Formata como Json
    print(resposta)               # Resposta Bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Resposta formatada

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_consultar_usuario():
    #Configura
    status_code = 200
    id =  9735
    username = 'cacau'
    firstName = 'chocolate'
    lastName = 'branco'
    email = 'cacau.chocolate@teste.com.br'
    password = '000111'
    phone = '11888888888'
    userStatus =  0

    #Executa
    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers
    )

    #Formata
    corpo_da_resposta = resposta.json()  # Formata como Json
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Resposta formatada

    #Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta['password'] == password
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['phone'] == phone
    assert corpo_da_resposta['firstName'] == firstName
    assert corpo_da_resposta['lastName'] == lastName
    assert corpo_da_resposta['userStatus'] == userStatus
    #assert corpo_da_resposta['token'] == token_usuario

    print(f'Token: {token_usuario}')


def testar_consultar_usuario_com_token(token_usuario):
    #Configura
    status_code = 200
    id =  9735
    username = 'cacau'
    firstName = 'chocolate'
    lastName = 'branco'
    email = 'cacau.chocolate@teste.com.br'
    password = '000111'
    phone = '11888888888'
    userStatus =  0

    #Executa
    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers
    )

    #Formata
    corpo_da_resposta = resposta.json()  # Formata como Json
    print(resposta)  # Resposta Bruta
    print(resposta.status_code)  # Status Code
    print(corpo_da_resposta)  # Resposta formatada

    #Valida
    assert resposta.status_code == status_code
    assert corpo_da_resposta['password'] == password
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['email'] == email
    assert corpo_da_resposta['phone'] == phone
    assert corpo_da_resposta['firstName'] == firstName
    assert corpo_da_resposta['lastName'] == lastName
    assert corpo_da_resposta['userStatus'] == userStatus
    #assert corpo_da_resposta['token'] == token_usuario

    print(f'Token: {token_usuario}')

def testar_alterar_usuario():
    #Configura
    username = 'cacau'
    statuscode_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '9735'

    #Executa
    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('C:/Users/vinic/PycharmProjects/fts132_inicio/test/db/user2.json',  'rb'),
        headers=headers
    )
    #Fomatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    #validar
    assert resposta.status_code == statuscode_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_excluir_usuario():
    #Configura
    username = 'cacau'
    statuscode_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'cacau'

    #Executa
    resposta = requests.delete(
        url=f'{base_url}/{username}',
        headers=headers
    )

    # Fomatação

    match resposta.status_code:
        case 200: #Apagar um usuario que foi encontrado
            corpo_da_resposta = resposta.json()
            print(resposta)
            print(resposta.status_code)
            print(corpo_da_resposta)

            # validar
            assert resposta.status_code == statuscode_esperado
            assert corpo_da_resposta['code'] == codigo_esperado
            assert corpo_da_resposta['type'] == tipo_esperado
            assert corpo_da_resposta['message'] == mensagem_esperada

        case 400:
            print('Username fornecido incorreto')

        case 404:
            print('Usuario não encontrado')

def testar_login_do_usuario():
    #Configura
    username ='cacau'
    password = 'acesso'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    inicio_mensagem_esperada = 'logged in user session:'


    #Executa
    resposta = requests.get(
        url=f'{base_url}/login?username={username}&password={password}',
        headers=headers
    )


    #Formatação
    corpo_da_resposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_resposta)

    #Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert  corpo_da_resposta['message'].find(inicio_mensagem_esperada) != -1

    '''frase = 'Neste fim de ano planeje seu sucesso'  #exemplo de assrt para pesquisar parte do texto 
    assert frase.find('suceeso') != -1'''

    #Extrair informação
    #Na mensagem "logged in user session:1639085615122" queremos pegar os numeros
    mensagem_recebida = corpo_da_resposta['message']
    token_usuario = mensagem_recebida[23:36]
    print(f'O token do usuario é: {token_usuario}')
    testar_consultar_usuario_com_token(token_usuario)

    #Exemplo

    frase = 'Saldo: R$ 1.987,65'
    valor = frase[7:18]
    print(f'O valor é: {valor}')

'''def testar_sequencia_de_testes():
    testar_criar_usuario()
    testar_login_do_usuario()
    testar_alterar_usuario()
    testar_consultar_usuario()
    testar_excluir_usuario()'''



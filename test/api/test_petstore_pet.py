import pytest
import requests

base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}


def testar_incluir_pet():
    # Configura
    status_code_esperado = 200
    nome_pet_esperado = 'Lessy'
    tag_esperada = 'vacinado'

    # Executa
    resposta = requests.post(
        url=base_url,
        data=open("../db/pet1.json", 'rb'),
        headers=headers
    )
    # Formata
    corpo_da_reposta = resposta.json()
    print(resposta)
    print(resposta.status_code)
    print(corpo_da_reposta)

    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_reposta['name'] == nome_pet_esperado
   # assert corpo_da_reposta['tags.name'] == tag_esperada

# 1- importar bibliotecas
import os
from datetime import datetime

from selenium import webdriver
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

caminho_print = 'C:/Users/vinic/PycharmProjects/fts132_inicio/prints/' \
                + datetime.now().strftime('%Y-%m-%d %H-%M-%S')  #colocar data e hora nas pastas de prints

# 2 Classe
class Test_selenium_webdriver():

    # definição de Inicio - Executa antes do teste
    def setup_method(self, method):
        # declarar o objeto do selenium e instaciar com o navegador desejado
        self.driver = webdriver.Chrome(
            'C:/Users/vinic/PycharmProjects/fts132_inicio/drivers/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        #Criar caminho print apenas no primeiro teste
        try:
            os.mkdir(caminho_print)
        except:
            print('A pasta já existe')



    # definição de fim - Executa depois do teste
    def teardown_method(self, method):
        # Destroir o objeto do selenium
        self.driver.quit()

    # Definição do teste
    @pytest.mark.parametrize('id, termo, curso, preco', [
        ('1', 'mantis', 'Mantis', 'R$ 59,99'),
        ('2', 'ctfl', 'Preparatório CTFL', 'R$ 199,00'),
        ])
    def testar_comprar_curso_mantis_com_clique_na_lupa(self, id, termo, curso, preco):

        # O selenium abre a url indicado
        self.driver.get('https://iterasys.com.br')
        # O Se clica no elemnto
        self.driver.get_screenshot_as_file(f'{caminho_print} teste {id} - passo 1 - home.png')
        self.driver.find_element(By.ID, 'searchtext').click()
        #O Se apaga o conteudo da caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').clear()
        # o Selenium escreve na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys(termo)
        self.driver.get_screenshot_as_file(f'{caminho_print} teste {id} - passo 2 - pesquisa pelo curso.png')
        # O Se Clicar na lupa de pesquisa
        self.driver.find_element(By.ID, 'btn_form_search').click()
        # o Se Clica em matriculi-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
        # O Se vlida o nome do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == curso
        # O Se valida o preço do curso
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == preco

    def testar_comprar_curso_mantis_com_enter(self):
            # O selenium abre a url indicado
            self.driver.get('https://iterasys.com.br')

            # O Se clica no elemnto
            self.driver.find_element(By.ID, 'searchtext').click()
            # O Se apaga o conteudo da caixa de pesquisa
            self.driver.find_element(By.ID, 'searchtext').clear()
            # o Selenium escreve na caixa de pesquisa
            self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
            # O Se Clicar no Enter
            self.driver.find_element(By.ID, 'btn_form_search').send_keys(Keys.ENTER)
            # o Se Clica em matriculi-se
            self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()
            # O Se vlida o nome do curso
            assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
            # O Se valida o preço do curso
            assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'

    # Flaky teste
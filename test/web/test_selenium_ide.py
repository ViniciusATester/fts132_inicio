# Generated by Selenium IDE
import pytest  # Framework de Teste de Unidade / Engine / Motor
import time  # Controle do tempo
import json  # Ler e escrever no formato json
from selenium import webdriver  # Bibliotecas do Selenium webDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 2 - Classe e definiçoes
class TestCursoMantis():
    def setup_method(self, method):
        # Instanciar o objeto do Selenium WebDriver como o chrome
        self.driver = webdriver.Chrome('C:/Users/vinic/PycharmProjects/fts132_inicio/drivers/chrome/96/chromedriver.exe')
        self.driver.implicitly_wait(30)# o robô irá esperar por até 30 segundos pleos elementos
        self.driver.maximize_window()  # maximiza a tela do computador
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_cursoMantis(self):
        self.driver.get("https://iterasys.com.br/")
        self.driver.set_window_size(1280, 680)
        self.driver.find_element(By.ID, "searchtext").click()
        self.driver.find_element(By.ID, "searchtext").send_keys("mantis")
        self.driver.find_element(By.CSS_SELECTOR, ".fa-search").click()
        self.driver.find_element(By.CSS_SELECTOR, ".comprar").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".item-title").text == "Mantis"
        assert self.driver.find_element(By.CSS_SELECTOR, ".new-price").text == "R$ 59,99"
from selenium import webdriver
from selenium.common.exceptions import (
    NoSuchElementException,
    StaleElementReferenceException,
    WebDriverException
)
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.get('https://devaprender-play.netlify.app')

try:
    nomes = driver.find_elements(By.XPATH, "//h3[@class='text-lg font-semibold text-gray-900 group-hover:text-indigo-600']")
    precos = driver.find_elements(By.XPATH, "//p[@class='text-2xl font-bold text-indigo-600']")

    with open("precos.csv", "a", encoding="utf-8") as arq:
        for nome, preco in zip(nomes, precos):
            arq.write(f"{nome.text},{preco.text}{os.linesep}")

except NoSuchElementException:
    print("Erro: elemento não encontrado na página.")

except StaleElementReferenceException:
    print("Erro: elemento ficou desatualizado (DOM mudou).")

except WebDriverException as e:
    print(f"Erro geral do WebDriver: {e}")


input('')
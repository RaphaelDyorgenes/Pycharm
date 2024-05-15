import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = "https://books.toscrape.com/"

driver.get(url)
time.sleep(2)

links = driver.find_elements(By.TAG_NAME, value="a")
print(len(links))

x = driver.find_elements(By.TAG_NAME, value="a")[92].text
print(x)

y = driver.find_elements(By.TAG_NAME, value='a')[54].get_attribute('title')
print(y)

print(driver.find_elements(By.TAG_NAME, value='a')[54:94:2])

elementostitulo = driver.find_elements(By.TAG_NAME, value='a')[54:94:2]

listatitulos = [title.get_attribute('title') for title in elementostitulo]
print(listatitulos)

elementostitulo[1].click()
stok = driver.find_element(By.CLASS_NAME, 'instock').text

print(stok)

estoque = int(stok.replace('In stock (', '').replace(' available)', ''))
print(estoque)

driver.back()

listaestoque = []

for titulo in elementostitulo:
    titulo.click()
    time.sleep(1)
    qtd = int(stok.replace('In stock (', '').replace(' available)', ''))
    listaestoque.append(qtd)
    driver.back()
    time.sleep(1)

data = {"Titulo": listatitulos, "Estoque": listaestoque}
dados = pd.DataFrame(data)
dados.to_excel("dados.xlsx")

# Projetos em Python

1. [Projeto 1](#Projeto-1)
   - Pegando cotações do site do Google Finance utilizando:
        * requests
        * BeautifulSoup
    - Depois transformando em um DataFrame utilizando:
        - pandas

2. [Projeto 2](#Projeto-2)
   - Baixando um relatorio com o navegador firefox utilizando
     * selenium
     * urllib.request
     * os
     * time


## <a id="Projeto-1"></a> Projeto 1

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_quotation(tiker):
  URL = f'https://www.google.com/finance/quote/{tiker}:BVMF?hl=pt'
  CSS_SELECTORS = {
    'name': 'zzDege',
    'price': 'YMlKec fxKbKc'
  }

  response = requests.get(URL)
  soup = BeautifulSoup(response.text, 'html.parser')
  name = soup.find_all(class_=CSS_SELECTORS['name'])[0].text
  price = str(
    soup.find_all(class_=CSS_SELECTORS['price'])[0].text
  ).replace('\xa0', ' ')
  
  return name, price



if __name__ == '__main__':
  QUOTATIONS, TIKERS = [], ['TAEE11', 'BBAS3', 'GOAU3', 'PETR4', 'ITSA4']
  for ticker in TIKERS:
    QUOTATIONS.append(get_quotation(ticker))
  
  df = pd.DataFrame(QUOTATIONS, columns = ['Empresa', 'Cotação'])
  print(df)

```

## Projeto 2 {#Projeto-2}
## <a id="Projeto-2"></a> Projeto 2

```python
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

from urllib.request import urlretrieve
from os import getcwd
from time import sleep

DIR_ACTUAL = getcwd()
DIR_ACTUAL = DIR_ACTUAL if DIR_ACTUAL.count('\\') == 0 else DIR_ACTUAL.replace('\\', '/')

URL = 'https://ri.bb.com.br/informacoes-financeiras/central-de-resultados/'
BROWSER = Firefox()
BROWSER.get(URL)
XPATH_A = '//*[@id="tabela_1"]/tr[1]/td[2]/a'
while True:
  try:
    sleep(0.5)
    A_LINK_PDF = BROWSER.find_element(By.XPATH, XPATH_A)
    HREF = A_LINK_PDF.get_attribute('href')
    urlretrieve(HREF, f'{DIR_ACTUAL}/Relatório.pdf')
    break
  except:
    print('.', end='')

BROWSER.quit()

```

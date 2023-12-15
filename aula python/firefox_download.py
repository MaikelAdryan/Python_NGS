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

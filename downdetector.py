# -*- coding: utf-8 -*-
from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import telepot
import config

base_url = 'https://downdetector.com.br/'
#link = f"{base_url}/fora-do-ar/"

bot = telepot.Bot(config.TOKEN)
browser = webdriver.Firefox()
browser.get(base_url)
downdetector = browser.page_source
downdetector_page = bs(downdetector,'html.parser')

problemas = downdetector_page.find_all('h5')
browser.close()
lista = []

for problema in problemas:
    titulo = problema
    lista.append(str(titulo).strip('<h5>'))

n1 = lista[0].strip('</')
n2 = lista[1].strip('</')
n3 = lista[2].strip('</')
n4 = lista[3].strip('</')
n5 = lista[4].strip('</')

msg = "Top 5 Downdetector:\n\n 1 - {}\n 2 - {}\n 3 - {}\n 4 - {}\n 5 - {}\n".format(n1,n2,n3,n4,n5)
bot.sendMessage(config.USER,msg)


print ("Top 5 Downdetector:\n\n{}\n {}\n {}\n {}\n {}\n".format(n1,n2,n3,n4,n5))

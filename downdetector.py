# -*- coding: utf-8 -*-
# downdetector.py - Informar o Top5 do Downdetector
#
# Site:       https://wesllenmatias.github.io
# Autor:      Wesllen Matias
# Manutenção: Wesllen Matias
# Telegram: @wesllenmatias
#
# ------------------------------------------------------------------------ #
# Este programa vai checar os Top 5 do Downdetector e enviar via telegram
#
# ------------------------------------------------------------------------ #
# Histórico:
#
#   v1.0 - Versão inicial
# ------------------------------------------------------------------------ #
# Testado em:
#   Python 3.6.9
# ------------------------------------------------------------------------ #
from requests import get
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import telebot
import config

base_url = 'https://downdetector.com.br/'
#link = f"{base_url}/fora-do-ar/"
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Olá Bem-Vindo ao seu Bot!")

@bot.message_handler(commands=['foradoar'])
def downdetector_foradoar (message):
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
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
    bot.reply_to(message,msg)

bot.polling()

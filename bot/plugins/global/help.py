#!/usr/bin python3
# -*- coding: UTF-8 -*-

# _______________ Imports definition _______________ #
from config import * 

# _______________ Functions _______________ #

@bot.message_handler(commands=['start', 'help'])
def send_welcome(m):
    cid = m.chat.id
    bot.send_message(cid,
        '''
        Los comandos se encuentran disponibles al escribir "/".\nEscribe <b>/comando help</b> para la ayuda de cada comando.
        \nPor ejemplo: <i>/meme help</i>
        ''',
    parse_mode ="HTML")
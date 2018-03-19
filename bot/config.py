#!/usr/bin python3
# -*- coding: UTF-8 -*-

# _________________________________________#
# ________________ Imports ________________#
# _________________________________________#

# ________ System imports #
import sys, os, time
from datetime import datetime

# ________ Third party imports #
import telebot  # Librería de la API del bot.
from telebot import types  # Tipos para la API del bot.
import logging  # Logging
from addict import Dict
import json # Librería json
from colorclass import Color # output colors

# ________ Extras imports #


# _________________________________________#
# _______________ Constants _______________#
# _________________________________________#
# Programming values
VERSION = '0.0.1'
DEBUG = False
DATA_DIR = 'private_data'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
LOG_DIR = 'logs'
LOG_FILE = LOG_DIR + '/bot.log'

# Load config

with open(DATA_DIR + '/config.json', encoding='utf-8') as data_file:
    config_data = json.loads(data_file.read())

# Bot values
BOT_TOKEN = config_data['bot']['token']
BOT_ID = config_data['bot']['id']

# Admin values
admin = Dict()
admin.name = config_data['admin']['name']
admin.username = config_data['admin']['username']
admin.id = config_data['admin']['id']


# _________________________________________#
# _________________ Data __________________#
# _________________________________________#

bot = telebot.TeleBot(token=BOT_TOKEN, skip_pending = True )

# _________________________________________#
# _________________ Funcs _________________#
# _________________________________________#

def LOGGER(str):
    date = datetime.now().strftime(DATE_FORMAT)
    logStr = Color('{green}[' + '{0}'.format(date) + ']{/green}' + '{0}'.format(str) ) 
    print(logStr)
    ## Save it into log file
    f = open( LOG_FILE , 'a', encoding="utf-8")
    f.write( '[{}] {}\n'.format(date,str) )
    f.close()
    
#!/usr/bin python3
# -*- coding: utf-8 -*-

# _________________________________________#
# ________________ Imports ________________#
# _________________________________________#
# _____ General imports
from config import *

# _____ Import functionalities
import importdir
importdir.do(os.path.join('plugins','global'), globals())
importdir.do(os.path.join('plugins','features'), globals())

# Logger init
LOGGER('Inicialización - Plugins cargados.')

# Initialize with starting message
try:
    date = datetime.now().strftime(DATE_FORMAT)
    text = '{0}\n{1} <b>iniciado</b>'.format(date,BOT_ID)
    bot.send_message(admin.id , text , parse_mode='HTML')
except Exception as e :
    try :
        bot.send_message(admin.id , str(e))
    except Exception as e :
        LOGGER('Unable to send message to {0}[{1}]'.format(admin.name , admin.id))
        
# General listener
def listener(messages): 
    # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages:
        # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': 
            # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id
            date  = datetime.now().strftime(DATE_FORMAT)
            source = 'PM' if m.chat.type == 'private' else str(cid)+"|" + str(m.chat.title)

            # Almacenaremos el ID de la conversación.
            LOGGER("[" + source + "][" + str(date) + "][" + str(m.from_user.id) + "] ("+ m.from_user.first_name + "):" + m.text)
            # Y haremos que imprima algo parecido a esto -> [52033876] Nick: /start
# Set del listener del bot
bot.set_update_listener(listener)

# _________________________________________#
# ________________ Polling ________________#
# _________________________________________#

while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=2)
    except Exception as e :
        LOGGER('Polling Exception: {}'.format(e))
        time.sleep(3)

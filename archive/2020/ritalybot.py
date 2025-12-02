#import logging
import os
import random
import string
import tempfile
import textwrap
import datetime
import re
import random

from telegram import Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler
from telegram.ext.filters import Filters

from datetime import date, timedelta
import json, numbers

from . import config

def main():
#  logging.basicConfig(filename='log.log', filemode='w', format='[%(asctime)s]: %(message)s', level=logging.INFO)
   updater = Updater(config.BOT_TOKEN)

   today = date.today() #data in pythonese da datetime
   #tomorrow = date.today() + timedelta(days=1) # solo per debug
   data_oggi = today.strftime("%Y-%m-%d") #converto in stringa
   #data_oggi = tomorrow.strftime("%Y-%m-%d") #converto in stringa

   f = open("mons", "r")
   numerodimon = int(f.read())
   print(f'[{datetime.datetime.now()}] Il numero di mon è: {numerodimon}')
   f.close()

   with open('punteggi.json', 'r') as file_json: #apri il file json
        dict_punteggi = json.load(file_json) #leggi il dizionario

   updater.dispatcher.add_handler(CommandHandler('help', handle_help)) # /help
   updater.dispatcher.add_handler(CommandHandler('punteggio', handle_punteggio)) # /submit
   updater.dispatcher.add_handler(CommandHandler('classifica', handle_classifica)) # /classifica
   updater.dispatcher.add_handler(CommandHandler('daily', handle_daily)) # /daily
   updater.dispatcher.add_handler(CommandHandler('media', handle_media)) # /media_punteggi

   updater.dispatcher.add_handler(CommandHandler('asaggese', handle_asaggese)) # /asaggese

   updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'\bmon\b', re.IGNORECASE)), handle_mon),3) # /contamon
   updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r"\bsai chi\b", re.IGNORECASE)), handle_saichi),2) # / sai chi?
   updater.dispatcher.add_handler(MessageHandler(Filters.photo & Filters.caption_regex(re.compile(r"\bsai chi\b", re.IGNORECASE)), handle_saichi),2) # / sai chi?
   updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r"\b(di|a|da|in|con|su|per|tra|fra) chi\b", re.IGNORECASE)), handle_particellachi),4) # particella
   updater.dispatcher.add_handler(MessageHandler(Filters.photo & Filters.caption_regex(re.compile(r"\b(di|a|da|in|con|su|per|tra|fra) chi\b", re.IGNORECASE)), handle_particellachi),4)

   updater.dispatcher.add_handler(CommandHandler('admin_reset', handle_admin_reset)) # /admin_reset giorno
   updater.dispatcher.add_handler(CommandHandler('admin_delete', handle_admin_delete)) # /admin_delete utente
#  updater.dispatcher.add_handler(CommandHandler('admin_addban', handle_admin_addban)) # /admin_addbane
#  updater.dispatcher.add_handler(CommandHandler('admin_delban', handle_admin_delban)) # /admin_delban

   updater.start_polling()
   updater.idle()


def handle_help(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id in config.BANS:
        print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} è bannato!') #debug
        #update.message.reply_text(f'Ammazzati coglione.',quote=False) #enuncia che è bannato
        return
    update.message.reply_text(f'Ciao {update.effective_user.first_name}, puoi usare /punteggio XXXXX per darmi il punteggio di oggi oppure e /classifica per avere la TOP 5 giornaliera. Puoi usare /daily per il link alla challenge di oggi.')

def handle_punteggio(update: Update, context: CallbackContext) -> None: # quando qualcuno scrive /punteggio X
    print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} vuole aggiungere un punteggio...') #debug
    if update.message.from_user.id in config.BANS:
        print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} è bannato!') #debug
        #update.message.reply_text(f'Ammazzati coglione.',quote=False) #enuncia che è bannato
        return
    punteggio = " ".join(context.args) #prende il punteggio dal comando
    if punteggio == "": #se non è stato messo nessun punteggio
        update.message.reply_text(f'Devi inserire un punteggio.',quote=False) #enuncia che devi mettere i numeretti
        print(f"[{datetime.datetime.now()}] ...ma non ha messo nessun punteggio") #debug
        return

    if not punteggio.isnumeric():
       update.message.reply_text(f'Devi inserire un punteggio valido.',quote=False) #enuncia che devi mettere SOLO numeretti
       print(f"[{datetime.datetime.now()}] ...ma non ha scritto dei numeri validi") #debug
       return

    punteggio = int(punteggio)

    if punteggio > 25000:
        update.message.reply_text(f'Per favore non fare il coglione, il massimo è 25000.',quote=False) #enuncia che devi mettere 0-25000
        print(f"[{datetime.datetime.now()}] ...ma voleva solo fare il coglione") #debug
        return


    today = date.today() #data in pythonese da datetime
    #tomorrow = date.today() + timedelta(days=1) #pythonese per "domani"
    data_oggi = today.strftime("%Y-%m-%d") #converto in stringa
    #data_oggi = tomorrow.strftime("%Y-%m-%d") #converto in stringa

    if data_oggi not in dict_punteggi: #controlla se esiste una lista con la data di oggipif met
        dict_punteggi[data_oggi] = {} #se non c'è, ne crea una vuota

    #for i in range(len(dict_punteggi[data_oggi])): #per ogni tupla nella lista di oggi
    #    if dict_punteggi[data_oggi][i][0] == update.effective_user.first_name: #controlla che non ci sia già un'entry con il tuo nick
    #       update.message.reply_text(f'Hai già inserito un punteggio per oggi!',quote=False) #se c'è, manda a cagare e torna a casa
    #       return

    dict_punteggi[data_oggi].update({update.effective_user.first_name: punteggio}) #aggiunge o updata nuovo punteggio
    json.dump(dict_punteggi, open('punteggi.json', 'w')) #scrive su json
    update.message.reply_text(f'Grazie {update.effective_user.first_name}, il tuo punteggio del {data_oggi} è: {punteggio}',parse_mode='HTML',quote=False) #enuncia data e punteggio
    print(f"[{datetime.datetime.now()}] ...fatto!")

def handle_classifica(update: Update, context: CallbackContext) -> None:
    arg = " ".join(context.args) #prende la data

    if arg == "":
        today = date.today() #data in pythonese da datetime
        data_oggi = today.strftime("%Y-%m-%d") #converto in stringa
    else:
        data_oggi = arg

    print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} chiede la classifica del {data_oggi}') #debug
    if update.message.from_user.id in config.BANS:
        print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} è bannato!') #debug
        #update.message.reply_text(f'Ammazzati coglione.',quote=False) #enuncia che è bannato
        return
    if data_oggi not in dict_punteggi: #controlla se esiste una key con la data di oggi
        update.message.reply_text(f'Non ci sono punteggi!',quote=False)  #
        return

    if dict_punteggi[data_oggi] == {}: #se c'è oggi, controlla se ci sono punteggi per oggi
        update.message.reply_text(f'Non ci sono punteggi!!',quote=False)  #
        return

    lista_classifica = sorted(list(dict_punteggi[data_oggi].items()), key=lambda x: x[1], reverse=True) #sorta lista
    punteggio_ordinato = ""
    for entry in lista_classifica[0:5]:
        punteggio_ordinato = punteggio_ordinato + str(entry[0]) + ": " + str(entry[1]) + "\n"
    update.message.reply_text(f'Classifica del {data_oggi}:\n{punteggio_ordinato}',quote=False)  #printa lista carina
    #pprint(dict_punteggi[data_oggi][0:5])

def handle_daily(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id in config.BANS:
        print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} è bannato!') #debug
        #update.message.reply_text(f'Ammazzati coglione.',quote=False) #enuncia che è bannato
        return
    #logging.warning('$update.effective_user.first_name} chiede la daily')
    print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} chiede la daily') #debug
    update.message.reply_text(f'https://www.geoguessr.com/daily-challenges',quote=False,disable_web_page_preview=True)

def handle_admin_reset(update: Update, context: CallbackContext) -> None:
    if update.message.from_user.id in config.ADMINS:
       data = " ".join(context.args)
       dict_punteggi.pop(str(data))
       update.message.reply_text(f'Hai resettato la classifica del giorno {data}',quote=False)
       json.dump(dict_punteggi, open('punteggi.json', 'w')) #scrive su json
       print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} resetta la classifica del giorno {data}') #debug

#def handle_admin_addban(update: Update, context: CallbackContext) -> None:
#    if update.message.from_user.id in config.ADMINS:
#        user_id = " ".join(context.args)
#        print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} vuole aggiungere {user_id} alla lista dei bannati') #debug
#        if user_id in config.BANS:
#            print(f'{user_id} già presente nella lista.')
#            return
#        config.BANS.append(int(user_id))
#        update.message.reply_text(f'{user_id} aggiunto.',quote=False)

#def handle_admin_delban(update: Update, context: CallbackContext) -> None:
#    if update.message.from_user.id in config.ADMINS:
#        return



def handle_admin_delete(update: Update, context: CallbackContext) -> None:
    print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} vuole cancellare un punteggio') #debug
    if update.message.from_user.id in config.ADMINS:
       utente = " ".join(context.args)
       print("Utente: ", utente)
       if utente in dict_punteggi[data_oggi]:
           print("c'è, cancello")
           dict_punteggi[data_oggi].pop(utente)
           update.message.reply_text(f'Hai cancellato il punteggio di {utente}',quote=False)
           json.dump(dict_punteggi, open('punteggi.json', 'w')) #scrive su json
       else:
           print("non c'è, non cancello")
           update.message.reply_text(f'{utente} non ha nessun punteggio.',quote=False)

def handle_asaggese(update: Update, context: CallbackContext) -> None:
    from PIL import Image, ImageDraw, ImageFont
    if not update.message.reply_to_message:
        print(f'[{datetime.datetime.now()}] {update.effective_user.first_name}? Un coglione che non sa rispondere.')
        #update.message.reply_text(f'Devi rispondere ad una foto',quote=False)
        return
    if not update.message.reply_to_message.photo:
        print(f'[{datetime.datetime.now()}] {update.effective_user.first_name}? Un coglione che non sa rispondere ad una foto.')
        #update.message.reply_text(f'Devi rispondere ad una foto',quote=False)
        return

    print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} ha iniziato un /asaggese') #debug
    picture = update.message.reply_to_message.photo[-1]
    tempphoto = tempfile.mktemp(suffix='.jpg')
    picture.get_file().download(custom_path=tempphoto)
    image = Image.open(tempphoto)
    print("larghezza: ", image.size[0]) #debug dimensione immagine
    print("altezza: ", image.size[1]) #debug dimensione immagine
    text_size = round(image.size[1]/14) # dimensione dei font è dimensione_verticale dell'immagine diviso 8
    print("dimensione font: ", text_size) #debug dimensione del font
    font_bold = ImageFont.truetype(str(config.FONT_FILE_BOLD), size=text_size)
    font_italic = ImageFont.truetype(str(config.FONT_FILE_ITALIC), size=text_size)
    draw = ImageDraw.Draw(image)
    testo = " ".join(context.args)
    #text_size = draw.textsize(f'{testo}', font_bold)
    text_size_firma = draw.textsize('Alessandro Saggese', font_italic)
    draw.text(((image.size[0] - text_size_firma[0])/2,(image.size[1]-text_size_firma[1])-5), 'Alessandro Saggese', font=font_italic, fill="black") #ombra
    draw.text((((image.size[0] - text_size_firma[0])/2),(image.size[1]-text_size_firma[1])-6), 'Alessandro Saggese', font=font_italic)
  #  draw.text((18,22), f'{testo}', font=font_bold, fill="black") #ombra
  #  draw.text((20,20), f'{testo}', font=font_bold)
    letters_size = draw.textsize('abcdefghilmnopqrstuvzxyjkw', font_bold)
    lettera_singola = round(letters_size[0]/26)
    print("Dimensione di una lettera (media): ", lettera_singola)
    wrap_width = round(image.size[0]/lettera_singola)
    print("Wrap in numero di caratteri: ", wrap_width) #debug
    testo2 = textwrap.fill(f'{testo}',width=wrap_width) #wrappo per un numero di caratteri pari a larghezza immagine diviso dimensione del testo]
    draw.text((22,22), f'{testo2}', font=font_bold, fill="black") #ombra
    draw.text((20,20), f'{testo2}', font=font_bold)
    image.save(tempphoto, "PNG")
    update.message.reply_photo(open(tempphoto, 'rb'))
    print(f"[{datetime.datetime.now()}] #### FINE ####")


def handle_media(update: Update, context: CallbackContext) -> None:
    persona = " ".join(context.args)
    print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} chiede la media punteggi di {persona}.')
    print(f'Cerco tutti i punteggi di {persona}')
    punteggi_persona = []
    for data in dict_punteggi:
        if persona in dict_punteggi[data]:
            punteggi_persona.append(dict_punteggi[data][persona])
    if not punteggi_persona:
        print(f'[{datetime.datetime.now()}] Nessun punteggio registrato')
        update.message.reply_text(f'{persona} non ha nessun punteggio.',quote=False)
        return
    print(f'Trovati tutti i seguenti punteggi: {punteggi_persona}')
    media_punteggi = round(sum(punteggi_persona) / len(punteggi_persona))
    print(f'[{datetime.datetime.now()}] La media su {len(punteggi_persona)} partite è: {media_punteggi}')
    update.message.reply_text(f'La media punteggi di {persona} su {len(punteggi_persona)} partite è: {media_punteggi}',quote=False)
    return

def handle_mon(update: Update, context: CallbackContext) -> None:
    if update.message.chat.id == config.ID_RITALY:
        return
    print(f'[{datetime.datetime.now()}] {update.effective_user.first_name} ha parlato di mon!')
    f = open("mons", "r")
    numerodimon = int(f.read())
    print(f'[{datetime.datetime.now()}] Il numero di mon era: {numerodimon}')
    f.close()
    numerodimon += 1
    mons = open("mons", "w")
    update.message.reply_text(f'(Avete parlato di mon {numerodimon} volte.)',quote=False)
    mons.write(str(numerodimon))
    print(f'[{datetime.datetime.now()}] Il nuovo numero di mon è: {numerodimon}')
    mons.close()

def handle_saichi(update: Update, context: CallbackContext) -> None:
    if update.message.chat.id == config.ID_RITALY:
        return
    listamadri = ['Trifase', 'sushi', 'Stefano', 'Gesù', 'touchdown', 'exe', 'MadAdam', 'mainde', 'Porvora', 'fry']
    if random.randint(0,100) < 26:
        madre_scelta = random.choice(listamadri)
        update.message.reply_text(f'la madre di {madre_scelta}')
    else:
        update.message.reply_text(f'tua madre',quote=False)

def handle_particellachi(update: Update, context: CallbackContext) -> None:
    prepo = context.match.group(1)
    if update.message.chat.id == config.ID_RITALY:
        return

    listaamadri = ['Trifase', 'sushi', 'Stefano', 'Gesù', 'touchdown', 'exe', 'MadAdam', 'mainde', 'Porvora', 'fry']
    if random.randint(0,100) < 20:
        madre_ascelta = random.choice(listaamadri)
        if prepo == 'di':
            update.message.reply_text(f'della madre di {madre_ascelta}')
        elif prepo == 'a':
            update.message.reply_text(f'alla madre di {madre_ascelta}')
        elif prepo == 'da':
            update.message.reply_text(f'dalla madre di {madre_ascelta}')
        elif prepo == 'in':
            update.message.reply_text(f'nella madre di {madre_ascelta}')
        elif prepo == 'su':
            update.message.reply_text(f'sulla madre di {madre_ascelta}')
        else:
            update.message.reply_text(f'{prepo} la madre di {madre_ascelta}')
    else:
        update.message.reply_text(f'{prepo} tua madre',quote=False)





if __name__ == "__main__":
   updater = Updater(config.BOT_TOKEN)

   today = date.today() #data in pythonese da datetime
   #tomorrow = date.today() + timedelta(days=1) # solo per debug
   data_oggi = today.strftime("%Y-%m-%d") #converto in stringa
   #data_oggi = tomorrow.strftime("%Y-%m-%d") #converto in stringa

   f = open("mons", "r")
   numerodimon = int(f.read())
   print(f'[{datetime.datetime.now()}] Il numero di mon è: {numerodimon}')
   f.close()

   with open('punteggi.json', 'r') as file_json: #apri il file json
        dict_punteggi = json.load(file_json) #leggi il dizionario
   main()

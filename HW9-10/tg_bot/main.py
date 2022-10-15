import telegram
from telegram.ext import Updater, CommandHandler
from commands import *

TOKEN = '6739008427:DJEH8fmeDFNFUV73rFNFIRnfr44hENRFNfu4ntk3f'
bot = telegram.Bot(token=TOKEN)
print(bot.get_me())

updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('weather', weather))
updater.dispatcher.add_handler(CommandHandler('help', help))

print('Запуск сервера')
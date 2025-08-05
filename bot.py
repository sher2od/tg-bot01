# bot.py
from config import TOKEN
from telegram.ext import Updater, MessageHandler, Filters,CommandHandler
from handlers import handle_p_hoto,handle_contact,handle_dice,handle_text,start,handle_buyurtma,nastroyka,orqaga

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(['start','boshlash'],start))
    
    
    # dispatcher.add_handler(MessageHandler(Filters.photo, handle_p_hoto))
    # dispatcher.add_handler(MessageHandler(Filters.contact,handle_contact))
    # dispatcher.add_handler(MessageHandler(Filters.dice,handle_dice))
    #dispatcher.add_handler(MessageHandler(Filters.text,handle_text))
    dispatcher.add_handler(MessageHandler(Filters.text("Buyurtmalarim"),handle_buyurtma))
    dispatcher.add_handler(MessageHandler(Filters.text("Sozlamalar"),nastroyka))
    dispatcher.add_handler(MessageHandler(Filters.text("Orqaga"),orqaga))
    

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()


# handlers.py
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,WebAppInfo
from telegram.ext import CallbackContext

def handle_p_hoto(update: Update, context: CallbackContext):
    photo = update.message.photo[0].file_id
    update.message.reply_photo(photo=photo, caption="mana")

def handle_contact(update:Update,context:CallbackContext):
    conatact = update.message.contact

    update.message.reply_contact(
        first_name=conatact.first_name,
        phone_number=conatact.phone_number
    )

def handle_dice(update:Update,context:CallbackContext):
    dice = update.message.dice

    update.message.reply_dice(
        emoji=dice.emoji
    )

def handle_text(update:Update,context:CallbackContext):
    update.message.reply_markdown_v2(
        text=f"salom ||{update.effective_user.full_name}||"
    )


def handle_buyurtma(update:Update,context:CallbackContext):
    update.message.reply_text(text="Bu bolim hali tayyormas uzur lkn")

def nastroyka(update:Update,context:CallbackContext):
    update.message.reply_markdown_v2(
        text=">Tanlang marhamat ",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Tilni ozgartirish")],
                [KeyboardButton("Telefon raqam ozgartirish")],
                [KeyboardButton("Orqaga")]
            ],
            resize_keyboard=True
        )                             
                                     
    )
    
def orqaga(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Asosiy menyuga qaytdingiz.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton("Buyurtma berish")],
                [KeyboardButton("Buyurtmalarim")],
                [KeyboardButton("Sozlamalar")]
            ],
            resize_keyboard=True
        )
    )




def start(update:Update,context:CallbackContext):
    bot = context.bot
    user = update.effective_user

    bot.send_message(
        chat_id = user.id,
        text=f'Assalomu alykum {user.first_name}!\nTanlang marhamat ',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[

                [KeyboardButton("Buyurtma berish",web_app=WebAppInfo(url="https://www.moysklad.uz/uz/vozmozhnosti/dlja-onlajn-torgovli/"))],[KeyboardButton("Buyurtmalarim")],
                [KeyboardButton("Sozlamalar")],[KeyboardButton("Biz haqimizda ",web_app=WebAppInfo(url="https://www.moysklad.uz/uz/vozmozhnosti/dlja-onlajn-torgovli/"))]

            ],
            resize_keyboard=True,
            #one_time_keyboard=True
        )
    )




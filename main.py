import logging
import os

import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN belum diset di Railway Variables")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

LINK_RESMI = "https://cutt.ly/CtjAfsCD"
LIVE_CHAT = "https://text.at/62b10376-5f3c-4b00-a4b1-f8d89da4af2e"
BANNER_PATH = os.path.join("assets", "bola911-banner.jpg")

WELCOME_TEXT = """<b>BOLA911 OFFICIAL</b>

Selamat datang di Bola911!

Transaksi deposit QRIS diproses hanya 1 detik.
Penarikan dibayar tuntas tanpa ribet.
Sistem cepat, stabil, dan pelayanan tersedia 24 jam.

Bergabunglah sekarang dan rasakan pengalaman terbaik bersama BOLA911!"""


def menu_buttons():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(
        InlineKeyboardButton("🌐 LINK RESMI BOLA911", url=LINK_RESMI),
        InlineKeyboardButton("💬 LIVE CHAT 24 JAM", url=LIVE_CHAT),
    )
    return markup


def send_welcome(chat_id):
    buttons = menu_buttons()

    if os.path.isfile(BANNER_PATH):
        with open(BANNER_PATH, "rb") as banner:
            bot.send_photo(
                chat_id,
                banner,
                caption=WELCOME_TEXT,
                reply_markup=buttons,
            )
    else:
        logging.warning("Banner tidak ditemukan: %s", BANNER_PATH)
        bot.send_message(
            chat_id,
            WELCOME_TEXT,
            reply_markup=buttons,
            disable_web_page_preview=True,
        )


@bot.message_handler(commands=["start"])
def start(message):
    send_welcome(message.chat.id)


@bot.message_handler(func=lambda message: True)
def reply_all(message):
    send_welcome(message.chat.id)


if __name__ == "__main__":
    logging.info("Bot Bola911 berjalan...")
    bot.infinity_polling(timeout=60, long_polling_timeout=30)

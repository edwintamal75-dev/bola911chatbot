import os
import logging
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN belum diset di Railway Variables")

bot = telebot.TeleBot(TOKEN, parse_mode="HTML")

LINK_ALTERNATIF = "https://cutt.ly/CtjAfsCD"
LIVE_CHAT = "https://direct.lc.chat/15271713/"
DAFTAR_SEKARANG = LINK_ALTERNATIF
HUBUNGI_CS = LIVE_CHAT


WELCOME_TEXT = """BOLA911 OFFICIAL

Selamat datang di Bola911!

Transaksi deposit QRIS proses hanya 1 detik
Penarikan berapapun dibayar lunas tanpa ribet
Sistem cepat, stabil dan pelayanan terbaik 24 jam

Link Alternatif: https://cutt.ly/CtjAfsCD
Live Chat 24 Jam: https://direct.lc.chat/15271713/

Bergabunglah sekarang dan rasakan pengalaman terbaik
bersama BOLA911!"""


def menu_buttons():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("Link Alternatif", url=LINK_ALTERNATIF),
        InlineKeyboardButton("Live Chat 24 Jam", url=LIVE_CHAT),
        InlineKeyboardButton("Daftar Sekarang", url=DAFTAR_SEKARANG),
        InlineKeyboardButton("Hubungi CS", url=HUBUNGI_CS),
    )
    return markup


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        WELCOME_TEXT,
        reply_markup=menu_buttons(),
        disable_web_page_preview=True,
    )


@bot.message_handler(func=lambda message: True)
def reply_all(message):
    bot.send_message(
        message.chat.id,
        WELCOME_TEXT,
        reply_markup=menu_buttons(),
        disable_web_page_preview=True,
    )


if __name__ == "__main__":
    logging.info("Bot Bola911 berjalan...")
    bot.infinity_polling(timeout=60, long_polling_timeout=30)

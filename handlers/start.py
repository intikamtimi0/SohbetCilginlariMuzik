from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Merhaba👋 Telegeam Gruplarının sesli sohbetlerinde müzik çalabiliyorum. Seni şaşırtacak bir sürü harika özelliğim var!\n\n🔴 Telegram gruplarının sesli sohbetlerinde müzik çalmamı ister misin? \nBeni nasıl kullanabileceğinizi öğrenmek için lütfen aşağıdaki \ '📜 Kullanım Kılavuzu 📜 \' düğmesini tıklayın. \ N \ n🔴 Grubunuzun sesli sohbetinde müzik çalabilmek için Asistanın grubunuzda olması gerekir. \ N \ n🔴 Diğer [Kullanıcı Kılavuzunda](https://telegra.ph/Serenity-Music-Bot-05-05) belirtilen bilgi ve komutlar\n\n@ExercitusBots'un bir projesi""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Kullanım Kılavuzu 📜", url="https://telegra.ph/Exercitus-Music-Bot-05-30")
                  ],[
                    InlineKeyboardButton(
                        "👨‍💻 Güncellemeler 👨‍💻", url="https://t.me/ExercitusBots"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Destek Grubu 🎙️", url="https://t.me/ExercitusSupport"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Müzik Oynatıcı Aktif**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎙️ Destek Grubu 🎙️", url="https://t.me/ExercitusSupport")
                ]
            ]
        )
   )

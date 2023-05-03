import asyncio
import telegram

async def send_message():
    # Token de acceso del bot
    TOKEN = '6021038433:AAFgNORXxoK51_xt_Rqt44SWdh3ASFF6no0'

    # ID de chat del bot
    CHAT_ID = '318712727'

    # Crear un objeto bot con el token de acceso
    bot = telegram.Bot(token=TOKEN)

    # Enviar un mensaje al chat especificado
    await bot.send_message(chat_id=CHAT_ID, text='Hola, ¿cómo estás?')

asyncio.run(send_message())

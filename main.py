import asyncio
import telegram
from pythonping import ping

# Configuración de Telegram
telegram_token = '6021038433:AAFgNORXxoK51_xt_Rqt44SWdh3ASFF6no0'
chat_id = '318712727'
bot = telegram.Bot(telegram_token)

# Lista de direcciones IP de las computadoras que se van a verificar
computer_ips = ['192.168.1.105']

# Diccionario para mantener un seguimiento del estado de cada computadora
computer_status = {ip: False for ip in computer_ips}


async def check_computer(ip):
    response = ping(ip, count=1)
    if response.success:
        if not computer_status[ip]:
            computer_status[ip] = True
            message = f'La computadora {ip} está conectada.'
            await bot.send_message(chat_id, message)
    else:
        if computer_status[ip]:
            computer_status[ip] = False
            message = f'La computadora {ip} se ha desconectado.'
            await bot.send_message(chat_id, message)


async def main():
    while True:
        # Realizar ping a cada dirección IP en paralelo
        await asyncio.gather(*[check_computer(ip) for ip in computer_ips])
        # Esperar un tiempo antes de volver a realizar ping
        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())

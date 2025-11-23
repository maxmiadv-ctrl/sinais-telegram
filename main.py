import time
import requests
from telegram import Bot

# Seu Token do Bot
TOKEN = "8445851533:AAEr6XN5g9_zlWzNWWREW--PrYhF4F3n9C0"
bot = Bot(token=TOKEN)

# IDs dos grupos
GROUP_FREE = "-1003372557071"
GROUP_VIP = "-1003203081483"

# API da Bybit - preços em tempo real
def get_price(symbol="BTCUSDT"):
    try:
        url = f"https://api.bybit.com/v2/public/tickers?symbol={symbol}"
        response = requests.get(url, timeout=5).json()
        return float(response["result"][0]["last_price"])
    except:
        return None

# Enviar sinais
def send_signal(symbol, entry, target, stop, stars):
    star_icons = "⭐" * stars
    message = f"""
🔥 NOVO SINAL 🔥

💰 Par: {symbol}
📌 Entrada: {entry}
🎯 Alvo: {target}
🛑 Stop: {stop}
⚡ Força do Sinal: {star_icons}

💎 Cadastre-se na corretora para receber mais sinais:
👉 https://partner.bybit.com/b/49037
"""
    bot.send_message(chat_id=GROUP_FREE, text=message)

    if stars >= 2:
        bot.send_message(chat_id=GROUP_VIP, text=message)

# Simulação de sinais a cada 15 minutos
def run():
    while True:
        price = get_price()
        if price:
            send_signal(
                symbol="BTCUSDT",
                entry=price * 0.998,
                target=price * 1.01,
                stop=price * 0.99,
                stars=3
            )
        time.sleep(900)  # 15 minutos

if __name__ == "__main__":
    run()

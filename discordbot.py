#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "Nzc3NzQ1Njk4ODgzODk1MzE3.X7H6IA.EUb1BF7FRustDBJGL-MO29Tkyq8" #トークン
CHANNEL_ID = 777747247110291476 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=10)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '00:20':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

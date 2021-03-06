#coding:UTF-8
import os,discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = os.environ["DISCORD_BOT_TOKEN"] #トークン
CHANNEL_ID = os.environ["CHANNEL_ID"] #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

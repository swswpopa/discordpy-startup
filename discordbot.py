#coding:UTF-8
import discord
import os
import time
from discord.ext import tasks
from datetime import datetime 

TOKEN = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 730136347477540908 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_message(message): 
    if message.content == "ありがとう": 
    #:(コロン)を忘れずつける
        await client.send_message(message.channel, "どういたしまして!") 

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '05:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('日付が変わりました')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)

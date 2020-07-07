#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "DISCORD_BOT_TOKEN" #トークン
CHANNEL_ID = 730136347477540908 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()
@client.event
async def on_ready():
    while True:
        if time.strftime('%H:%M:%S',time.localtime())=='05:00:00':
            channel = client.get_channel('チャンネルID')
            await client.send_message(channel, '日付が変わりました')
client.run(TOKEN)

# インストールした discord.py を読み込む
import discord
import asyncio
import os
import traceback
import threading
#鯖チャンネルID

ID_readme = 768272323341320232

#ロールID
ID_clanmember = 666361330827132979

token = os.environ['DISCORD_BOT_TOKEN']
# 接続に必要なオブジェクトを生成
client = discord.Client()

            
    
@client.event  
async def on_raw_reaction_add(payload):  
    channel = client.get_channel(payload.channel_id)
    if channel.id == ID_readme:
        #ロールの付与
        if str(payload.emoji) == '<:61ok:728923368870510605>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role = guild.get_role(ID_clanmember)
            if not member.bot:            
                await member.add_roles(role)                

        
client.run(token)

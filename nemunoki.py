# インストールした discord.py を読み込む
import discord
import asyncio
import os
import traceback
import random
from datetime import datetime
from discord.ext import tasks
from discord.ext import commands
import threading
#鯖チャンネルID
#ID_CHANNEL_1 = 670294227846037514
ID_CHANNEL_ZANGE = 741739653245173800
#ID_taskkill = 726398497384824853  #628175073504788491はサンドボックス。管理所726398497384824853。テスト731046340674453567
ID_Mana = 730136347477540908
ID_readme = 768272323341320232
ID_yoyaku = 736757807780462643
ID_test = 731046340674453567
#ロールID
ID_role_1 = 767249291730747403
ID_role_2 = 767200011749949470
ID_role_3 = 767200106557865985
ID_role_tk = 767200196827676683
ID_clanmember = 666361330827132979
ID_role_test = 760094885364629524
#鯖専用絵文字
ID_emoji = '<:61ok:728923368870510605>'
ID_tk = '<:syarururage:737890640519495712>'
ID_emoji_zange = '<:61ok:728923368870510605>'
ID_1 = '<:1totu:767560319853395970>'
ID_2 = '<:2totu:767560336826957846>'
ID_3 = '<:3totu:767560349947658300>'
ID_remove_role = '<:knp:758012336706683062>'
#メッセージID
ID_message_totu = 767913437090283520
ID_message_tk = 767913440516898826
ID_message_reset = 767913441943879720

token = os.environ['DISCORD_BOT_TOKEN']
# 接続に必要なオブジェクトを生成
client = discord.Client()

# メッセージ受信時に動作する処理
#@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
        
    # チャンネル1に対するアクション
    if message.content == '/1段階目':
        channel = client.get_channel(ID_CHANNEL_1)
        await channel.send('--------------------1段階目--------------------')       

@client.event
async def on_message(payload):
    channel = client.get_channel(ID_test)
    guild = client.get_guild(payload.guild_id)  
    member = guild.get_member(payload.user_id)      
    if message.author.bot:
        return
    if channel.id == ID_test:
            await message.add_reaction(":x:") 
            
    
        
@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%H:%M')
   
    if now == '5:00':

        ch_sandbox = client.get_channel(628175073504788491)
        await ch_sandbox.send("erovolley delete")
        roletest = client.get_role(ID_role_test)
        for member in client.members:
            if not member.bot:
                await channel.send(member)

                await member.remove_roles(roletest)

            await channel.send("エロバレー部を削除しました")
        
loop.start()  

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def totuDeclaration():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '05:00':
  
        #ランドソル杯データ入力
        #channel = client.get_channel(ID_Mana)
        #msg = await channel.send('日付が変わりました！記入が終わったらリアクションを付けてね♡ \n https://docs.google.com/spreadsheets/d/1nCdtFHS-60WcRZDx8hTXHFm3mPuEqefntQxeRfM2Lv0/edit#gid=632518118')  
        #await msg.add_reaction(ID_emoji) 
        #凸、タスクキル管理
        
       
        channel = client.get_channel(ID_taskkill)
        msg = await channel.send('---------------------------------------------------------------------- \n 凸、タスクキルしたらリアクションを付けてください♡ \n 間違えて押したときはリアクションを外してください♡') 
        msg = await channel.send('今日の凸状況')
        await msg.add_reaction(ID_1)
        await msg.add_reaction(ID_2)
        await msg.add_reaction(ID_3)
        msg = await channel.send('今日のタスクキル')
        await msg.add_reaction(ID_tk)
        msg = await channel.send('凸状況の初期化')        
        await msg.add_reaction(ID_remove_role)   
        msg = await channel.send('----------------------------------------------------------------------')                
     
#ループ処理実行
totuDeclaration.start()    



#@client.event
#async def on_raw_reaction_add(payload):
    # author: リアクションがついたメッセージを書いた人
    #channel = client.get_channel(payload.channel_id)
    #message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    #if channel.id == ID_Mana:
        #guild = client.get_guild(payload.guild_id)  
        #member = guild.get_member(payload.user_id)    
        #user = client.get_user(payload.user_id)                
        #if user.bot:
            #return
        #else:
            #text = member.name + 'さんが記入しました♡'  
            
    #if channel.id == ID_taskkill:
        #guild = client.get_guild(payload.guild_id)  
        #member = guild.get_member(payload.user_id)    
        #user = client.get_user(payload.user_id)        
        #if user.bot:
            #return
        #else:
            #text = member.name + 'さんが入力しました♡' 
            
#@client.event
#async def on_raw_reaction_add(self, reaction, user):
    #if channel.id == ID_CHANNEL_ZANGE:
        #if payload.emoji.name == '\N{GRINNING FACE}':
            #text = "父と子とゴデチアのみ名によって、" + message.author.name + "の罪をゆるします。アーメン。安心して行きなさい"
            #await channel.send(text)

    
@client.event  
async def on_raw_reaction_add(payload):  
    channel = client.get_channel(payload.channel_id)
    if channel.id == ID_taskkill:
        #ロールの付与
        if str(payload.emoji) == '<:1totu:767560319853395970>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role = guild.get_role(ID_role_1)        
            if not member.bot:            
                await member.add_roles(role)
                msg = await channel.send(member.name + 'さんが1凸しました♡')  
                await asyncio.sleep(5)  
                await msg.delete()
                
        if str(payload.emoji) == '<:2totu:767560336826957846>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role2 = guild.get_role(ID_role_2)
            role1 = guild.get_role(ID_role_1)            
            if not member.bot:        
                await member.add_roles(role2)
                await member.remove_roles(role1)          
                msg = await channel.send(member.name + 'さんが2凸しました♡')  
                await asyncio.sleep(5)  
                await msg.delete()       
        if str(payload.emoji) == '<:3totu:767560349947658300>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role3 = guild.get_role(ID_role_3)
            role2 = guild.get_role(ID_role_2)           
            if not member.bot:                  
                await member.add_roles(role3)
                await member.remove_roles(role2)                   
                msg = await channel.send(member.name + 'さんが3凸しました♡')  
                await asyncio.sleep(5)  
                await msg.delete()                    
        if str(payload.emoji) == '<:syarururage:737890640519495712>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role = guild.get_role(ID_role_tk)
            if not member.bot:
                await member.add_roles(role)
                msg = await channel.send(member.name + 'さんがタスクキルしました♡')  
                await asyncio.sleep(5)  
                await msg.delete()    
                
        #ロールの削除    
        if str(payload.emoji) == '<:knp:758012336706683062>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role1 = guild.get_role(ID_role_1)
            role2 = guild.get_role(ID_role_2)
            role3 = guild.get_role(ID_role_3)
            roletk = guild.get_role(ID_role_tk)            
            if not member.bot:
                await member.remove_roles(role1)
                await member.remove_roles(role2)
                await member.remove_roles(role3)            
                await member.remove_roles(roletk)
                msg = await channel.send(member.name + 'さんの凸状況が初期化されました♡')  
                await asyncio.sleep(5)  
                await msg.delete()    

    if channel.id == ID_readme:
        #ロールの付与
        if str(payload.emoji) == '<:61ok:728923368870510605>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role = guild.get_role(ID_clanmember)
            if not member.bot:            
                await member.add_roles(role)                
#リアクションを外すとロールも外れる                
@client.event  
async def on_raw_reaction_remove(payload):  
    channel = client.get_channel(payload.channel_id)
    if channel.id == ID_taskkill:
        if str(payload.emoji) == '<:1totu:767560319853395970>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role = guild.get_role(ID_role_1)
            if not member.bot:            
                await member.remove_roles(role)
                msg = await channel.send(member.name + 'さんが1凸目をキャンセルしました♡')  
                await asyncio.sleep(5)  
                await msg.delete()                   
        if str(payload.emoji) == '<:2totu:767560336826957846>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role = guild.get_role(ID_role_2)
            if not member.bot:
                await member.remove_roles(role)
                msg = await channel.send(member.name + 'さんが2凸目をキャンセルしました♡')  
                await asyncio.sleep(5)  
                await msg.delete()                      
        if str(payload.emoji) == '<:3totu:767560349947658300>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role = guild.get_role(ID_role_3)
            if not member.bot:
                await member.remove_roles(role)
                msg = await channel.send(member.name + 'さんが3凸目をキャンセルしました♡')  
                await asyncio.sleep(5)  
                await msg.delete()                 
        if str(payload.emoji) == '<:syarururage:737890640519495712>':
            guild = client.get_guild(payload.guild_id)  
            member = guild.get_member(payload.user_id)  
            role = guild.get_role(ID_role_tk)
            if not member.bot:
                await member.remove_roles(role)    
                msg = await channel.send(member.name + 'さんがタスクキルをキャンセルしました♡')  
                await asyncio.sleep(5)  
                await msg.delete()                 
          
                
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
        
    # チャンネル1に対するアクション
    if message.content == '/テスト':
        channel = client.get_channel(ID_taskkill)
        msg = await channel.send('---------------------------------------------------------------------- \n 凸、タスクキルしたらリアクションを付けてください♡ \n 間違えて押したときはリアクションを外してください♡') 
        msg = await channel.send('今日の凸状況')
        await msg.add_reaction(ID_1)
        await msg.add_reaction(ID_2)
        await msg.add_reaction(ID_3)
        msg = await channel.send('今日のタスクキル')
        await msg.add_reaction(ID_tk)
        msg = await channel.send('凸状況の初期化')        
        await msg.add_reaction(ID_remove_role)   
        msg = await channel.send('----------------------------------------------------------------------')            
        
        
client.run(token)

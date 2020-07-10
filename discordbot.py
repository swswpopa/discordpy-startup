from discord.ext import commands
import os
import traceback
from discord.ext import tasks
from datetime import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 730136347477540908 #チャンネルID

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)    
    
    # /単語　で受け答え
@bot.command()
async def jantama(ctx):
    await ctx.send('https://game.mahjongsoul.com/')
@bot.command()
async def dbd(ctx):
    await ctx.send('https://store.steampowered.com/app/381210/Dead_by_Daylight/')
@bot.command()
async def pubg(ctx):
    await ctx.send('https://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/')   
@bot.command()
async def patora(ctx):
    await ctx.send('https://www.youtube.com/channel/UCeLzT-7b2PBcunJplmWtoDg')    
@bot.command()
async def suzuhara(ctx):
    await ctx.send('https://www.youtube.com/channel/UC_a1ZYZ8ZTXpjg9xUY9sj8w')
@bot.command()
async def sion(ctx):
    await ctx.send('https://www.youtube.com/channel/UCXTpFs_3PqI41qX2d9tL2Rw%27')
@bot.command()
async def nanora(ctx):
    await ctx.send('https://www.youtube.com/channel/UCa9Y57gfeY0Zro_noHRVrnw%27')
@bot.command()
async def noeru(ctx):
    await ctx.send('https://www.youtube.com/channel/UCdyqAaZDKHXg4Ahi7VENThQ%27')
@bot.command()
async def korone(ctx):
    await ctx.send('https://www.youtube.com/channel/UChAnqc_AY5_I3Px5dig3X1Q')
@bot.command()
async def pekora(ctx):
    await ctx.send('https://www.youtube.com/channel/UC1DCedRgGHBdm81E1llLhOQ')
@bot.command()
async def coco(ctx):
    await ctx.send('https://www.youtube.com/channel/UCS9uQI-jC3DE0L4IpXyvr6w%27')
@bot.command()
async def hurea(ctx):
    await ctx.send('https://www.youtube.com/channel/UCvInZx9h3jC2JzsIzoOebWg%27')
@bot.command()
async def miko(ctx):
    await ctx.send('https://www.youtube.com/channel/UC-hM6YJuNYVAmUWxeIr9FeA%27')  
@bot.command()
async def ommc(ctx):
    await ctx.send('https://www.youtube.com/watch?v=b_PZkJZLfHw%27')
@bot.command()
async def marin(ctx):
    await ctx.send('https://www.youtube.com/channel/UCCzUftO8KOVkV4wQG1vkUvg')
    
  
                   
    # 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '20:00':
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send('日付が変わりました！サポ借りが終わったらこのメッセージにリアクションを付けてください！')  

#ループ処理実行
loop.start()

# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「ありがと」と発言したら「どういたしまして」が返る処理
    if message.content == 'ありがと':
        await message.channel.send('どういたしまして')

bot.run(token)

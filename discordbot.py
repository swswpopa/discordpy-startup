from discord.ext import commands
import asyncio
import os
import traceback
from discord.ext import tasks
from datetime import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = 726398497384824853 #チャンネルID

     
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
async def roa(ctx):
    await ctx.send('https://www.youtube.com/channel/UCCVwhI5trmaSxfcze_Ovzfw?view_as=subscriber')
@bot.command()
async def patora(ctx):
    await ctx.send('https://www.youtube.com/channel/UCeLzT-7b2PBcunJplmWtoDg \n https://twitter.com/Patra_HNST')    
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
@bot.command()
async def syaruru(ctx):
    await ctx.send('https://www.twitch.tv/syaruru3 \n https://www.youtube.com/channel/UC5SYDKMBeExdFs0ocWiK6xw')
@bot.command()
async def pekorakopipe(ctx):
    await ctx.send('ぺこーらいつもありがとう！ \n 最近ぺこーらへ感謝するのが日課になりつつあります！ \n 単刀直入に我慢してたこと書いちゃう！ \n ぺこーら愛してるぞおおおお \n (ps.厄介野うさぎだと思われてそうですがが長文赤スパ失礼！ \n ちなみに読まれてる頃にはあまりの恥ずかしさにユニバーサル大回転ぺこぺこの舞₍ ◝(‘ω’)◟ ⁾⁾₍₍ ◝(‘ω’)◜ ₎₎しながらベットの上で暴れてると思うので率直な一言貰ってもいいですか？w  \n 最後に一言！配信をはじめ本当にいつもありがとう！！！ \n 野うさぎ達を大切に思ってくれてる姿勢冗談抜きで本当に好きです。 \n 応援するしがいがあります！') 
@bot.command()
async def l4d2(ctx):
    await ctx.send('https://store.steampowered.com/app/550/Left_4_Dead_2/')
@bot.command()
async def kogatan(ctx):
    await ctx.send('月岡恋鐘フィギュアが予約開始！予約はこちらから！↓↓↓ \n https://www.goodsmile.info/ja/product/9770/%E6%9C%88%E5%B2%A1%E6%81%8B%E9%90%98+%E3%83%95%E3%82%A7%E3%82%A4%E3%82%B9%E3%82%AA%E3%83%96%E3%83%88%E3%83%AC%E3%82%B8%E3%83%A3%E3%83%BCVer.html')
@bot.command()
async def ow(ctx):
    await ctx.send('https://playoverwatch.com/ja-jp/')
@bot.command()
async def apex(ctx):
    await ctx.send('https://www.ea.com/ja-jp/games/apex-legends') 
@bot.command()
async def kaya(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/620957812247363594/731102733188333600/nXasbmNiZdEOItOpeAYD1594378196-1594378480_1.gif')        
@bot.command()
async def nyaru(ctx):
    await ctx.send('https://cdn.discordapp.com/attachments/620957812247363594/731098724406919179/image0.gif')  
    
    # 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '20:10':
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send('日付が変わりました！タスクキルしたらリアクションを付けましょうね')  
        await tmp_msg.add_reaction(emoji=":crab:")
          
#ループ処理実行
loop.start()

bot.run(token)

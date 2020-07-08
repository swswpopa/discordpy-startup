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
    
    
    # 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '05:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('日付が変わりました！サポ借りが終わったらこのメッセージにリアクションを付けてください！')  

#ループ処理実行
loop.start()


bot.run(token)

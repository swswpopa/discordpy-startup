from discord.ext import commands
import os
import traceback
from discord.ext import tasks
from datetime import datetime
import random 

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

@bot.event
 if message.content == "おみくじ":
　　　　　#↓
       hennnahuri = ["¥10000 \n ぺこーらいつもありがとう！ \n 最近ぺこーらへ感謝するのが日課になりつつあります！ \n 単刀直入に我慢してたこと書いちゃう！ \n ぺこーら愛してるぞおおおお \n (ps.厄介野うさぎだと思われてそうですが長文赤スパ失礼！ \n ちなみに読まれてる頃にはあまりの恥ずかしさにユニバーサル大回転ぺこぺこの舞₍ ◝('ω')◟ ⁾⁾₍₍ ◝('ω')◜ ₎₎しながらベットの上で暴れてると思うので率直な一言もらってもいいですか？ｗ \n 最後に一言！ \n 配信をはじめ本当にいつもありがとう！ \n 野うさぎ達を大切に思ってくれてる姿勢冗談抜きで本当に好きです。 \n 応援するしがいがあります！", "¥20000 \n いつも配信楽しいぺこ！ \n ポエムに込めた気持ちは今でも変わっていません。 \n 大変失礼な質問になるかもしれませんが、スパチャを投げる際にお願いをしてもいいのでしょうか？ \n もちろん限度があると思います。 \n でも、お願いがあったほうがぺこらさんが嬉しいのか？それとも今まで通りのほうがいいのか教えて頂けますでしょうか？ \n 大変失礼質問で申し訳ありません。 \n 要望が叶うのなら好きと言って頂ければ...。本当に長文ごめんなさい。いつも配信楽しいぺこ！ \n ポエムに込めた気持ちは今でも変わっていません。 \n 大変失礼な質問になるかもしれませんが、スパチャを投げる際にお願いをしてもいいのでしょうか？ /n もちろん限度があると思います。 \n でも、お願いがあったほうがぺこらさんが嬉しいのか？それとも今まで通りのほうがいいのか教えて頂けますでしょうか？ \n 大変失礼質問で申し訳ありません。 \n 要望が叶うのなら好きと言って頂ければ...。本当に長文ごめんなさい。", "¥10000 \n 歌ってみた再生50万＆登録者26万人ダブル達成おめでとうぺこ！ \n そしてぺこーらお帰りなさい！ \n たったの一日しか配信お休みしてなかったのに寂しさで胸がいっぱいになりました。 \n それだけぺこーらの存在が大きかったなと色々考えさせられましたが、元気いっぱいになって戻ってきて嬉しいです！ \n 元気な声を聞いてたら寝起きでめそめそしてたのがくっそ馬鹿馬鹿しく思えてきたｗｗｗって感じになりましたぺこ！ \n 流した涙代はぺこらんどに請求するので首を洗って待ってろぺこ！！！！ \n 今後ともアイドル兎田ぺこらを応援していくぺこおおおおおおおおｗｗｗｗｗｗｗｗ？", "¥10000 \n 今日はプロポーズの日だそうなので誠に勝手ながらプロポーズさせていただきます。 \n 船長を存じ上げてから今日の日まで船長の配信で笑わなかった日はありません。 \n いつもいつも、明るさと持ち前の豊富な知識でどんな配信でも楽しいものにしてしまう船長を心の底から尊敬しております。 \n 船長の幸せが一味の幸せです。 \n 何十万分の一としてよりちっぽけな存在になっていくかもしれませんが、これからも船長の配信を欠かすことなく見させて頂きますし、船長の幸せを祈っております。 \n どうかお疲れの出ませんように... \n これからもずっと御傍でお慕い申し上げております。"]
       choice = random.choice(hennnahuri)＃←
       await message.channel.send(choice)
        
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

bot.run(token)

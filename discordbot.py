from discord.ext import commands
import asyncio
import random
import os
import traceback
from datetime import datetime
from discord.ext import tasks

bot = commands.Bot(command_prefix='/', help_command=help())
bot.add_cog(Greet(bot=bot))
token = os.environ['DISCORD_BOT_TOKEN']

     
    # /単語　で受け答え
@bot.command(name="じゃんたま")
async def jantama(ctx):
    """じゃんたま公式HP"""
    await ctx.send('https://game.mahjongsoul.com/')
    await ctx.message.delete()
@bot.command(name="DBD")
async def dbd(ctx):
    """DbDストアページ"""
    await ctx.send('https://store.steampowered.com/app/381210/Dead_by_Daylight/')
    await ctx.message.delete()
@bot.command(name="pubg")
async def pubg(ctx):
    """pubuストアページ"""
    await ctx.send('https://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/')
    await ctx.message.delete()
@bot.command(name="周防パトラ")
async def patora(ctx):
    """周防パトラ"""
    await ctx.send('https://www.youtube.com/channel/UCeLzT-7b2PBcunJplmWtoDg \n https://twitter.com/Patra_HNST') 
    await ctx.message.delete()
@bot.command(name="鈴原るる")
async def suzuhara(ctx):
    """鈴原るる"""
    await ctx.send('https://www.youtube.com/channel/UC_a1ZYZ8ZTXpjg9xUY9sj8w')
    await ctx.message.delete()
@bot.command(name="しゃるる")
async def syaruru(ctx):
    """しゃるる"""
    await ctx.send('https://www.twitch.tv/syaruru3 \n https://www.youtube.com/channel/UC5SYDKMBeExdFs0ocWiK6xw')
    await ctx.message.delete()
@bot.command(name="ぺこらコピペ")
async def pekorakopipe(ctx):
    """ぺこらコピペ"""
    await ctx.send('ぺこーらいつもありがとう！ \n 最近ぺこーらへ感謝するのが日課になりつつあります！ \n 単刀直入に我慢してたこと書いちゃう！ \n ぺこーら愛してるぞおおおお \n (ps.厄介野うさぎだと思われてそうですがが長文赤スパ失礼！ \n ちなみに読まれてる頃にはあまりの恥ずかしさにユニバーサル大回転ぺこぺこの舞₍ ◝(‘ω’)◟ ⁾⁾₍₍ ◝(‘ω’)◜ ₎₎しながらベットの上で暴れてると思うので率直な一言貰ってもいいですか？w  \n 最後に一言！配信をはじめ本当にいつもありがとう！！！ \n 野うさぎ達を大切に思ってくれてる姿勢冗談抜きで本当に好きです。 \n 応援するしがいがあります！') 
    await ctx.message.delete()
@bot.command(name="l4d2")
async def l4d2(ctx):
    """l4d2ストアページ"""
    await ctx.send('https://store.steampowered.com/app/550/Left_4_Dead_2/')
    await ctx.message.delete()
@bot.command(name="こがたん")
async def kogatan(ctx):
    """月岡恋鐘フィギュア"""
    await ctx.send('月岡恋鐘フィギュアが予約開始！予約はこちらから！↓↓↓ \n https://www.goodsmile.info/ja/product/9770/%E6%9C%88%E5%B2%A1%E6%81%8B%E9%90%98+%E3%83%95%E3%82%A7%E3%82%A4%E3%82%B9%E3%82%AA%E3%83%96%E3%83%88%E3%83%AC%E3%82%B8%E3%83%A3%E3%83%BCVer.html')
    await ctx.message.delete()
@bot.command(name="クソゲ")
async def ow(ctx):
    """クソゲ"""
    await ctx.send('https://playoverwatch.com/ja-jp/')
    await ctx.message.delete()
@bot.command(name="apex")
async def apex(ctx):
    """apex公式"""
    await ctx.send('https://www.ea.com/ja-jp/games/apex-legends') 
    await ctx.message.delete()
@bot.command(name="ドラゴンズエンドフィ")
async def kaya(ctx):
    """ドラゴンズエンドフィ.gif"""
    await ctx.send('https://cdn.discordapp.com/attachments/620957812247363594/731102733188333600/nXasbmNiZdEOItOpeAYD1594378196-1594378480_1.gif')   
    await ctx.message.delete()     
@bot.command(name="ニューイヤーバースト.gif")
async def nyaru(ctx):
    """ニューイヤーバースト"""
    await ctx.send('https://cdn.discordapp.com/attachments/620957812247363594/731098724406919179/image0.gif')  
    await ctx.message.delete()
@bot.command(name="ボードゲームアリーナ")
async def bga(ctx):
    """ボードゲームアリーナ"""
    await ctx.send('https://ja.boardgamearena.com/')
    await ctx.message.delete()
@bot.command(name="サマーウルフェンブリッツ")
async def swb(ctx):
    """サマーウルフェンブリッツ.gif"""
    await ctx.send('http://cdn.gameinn.jp/wp-content/uploads/imgs/2020/03/Dz5PPIn.gif') 
    await ctx.message.delete()
@bot.command(name="やばいわよ")
async def yabaiwayo(ctx):
    """ヤバいわよ.gif"""
    await ctx.send('https://img.animanch.com/2020/05/1588593715655.gif') 
    await ctx.message.delete()
     
@bot.command()
async def uranai(ctx):
     #レスポンスされる運勢のリストを作成
    unsei = ["大吉", "中吉", "吉", "末吉", "小吉", "凶", "大凶"]
    choice = random.choice(unsei) #randomモジュールでunseiリストからランダムに一つを選出
    await ctx.send(choice)

    # プリコネキャラ
@bot.command(name="クリス")
async def kurisu(ctx):
    """クリス"""
    await ctx.send('https://gyazo.com/39f3bddc360ed09f20431c79d809e3fb')
    await ctx.message.delete()
@bot.command(name="マコト(サマー)")
async def mizumakoto(ctx):
    """マコト(サマー)"""
    await ctx.send('https://i.gyazo.com/6e1c942142ce952e7b15c8f1aa6e6d73 \n 水が弾けたら')
    await ctx.message.delete()
@bot.command(name="マコト")
async def makoto(ctx):
    """マコト"""
    await ctx.send('https://i.gyazo.com/016e0804ce330f11c6fcf75a60f89277 \n 黄色の鳴き声が消えたら')
    await ctx.message.delete()
@bot.command(name="ムイミ")
async def muimi(ctx):
    """ムイミ"""
    await ctx.send('https://i.gyazo.com/016e0804ce330f11c6fcf75a60f89277 \n 左斜め後ろに飛んだ時')
    await ctx.message.delete()
@bot.command(name="タマキ")
async def tamaki(ctx):
    """タマキ"""
    await ctx.send('https://i.gyazo.com/ede0b883427fbbe2dbd944d03f0d3030')
    await ctx.message.delete()     
@bot.command(name="ニノン(オーエド)")
async def onon(ctx):
    """ニノン(オーエド)"""
    await ctx.send('https://gyazo.com/9ef7490093e2ce4114fc33b49b68a9f9')
    await ctx.message.delete()
@bot.command(name="スズナ(サマー)")
async def mizuna(ctx):
    """スズナ(サマー)"""
    await ctx.send('https://i.gyazo.com/2b2c3b9dc2856a1d55d167bf920af87d')
    await ctx.message.delete()
@bot.command(name="ネネカ")
async def neneka(ctx):
    """ネネカ"""
    await ctx.send('https://i.gyazo.com/588cb732059044e1be0712694eadcffd')
    await ctx.message.delete()
@bot.command(name="ペコリーヌ(プリンセス)")
async def puripeko(ctx):
    """ペコリーヌ(プリンセス)"""
    await ctx.send('https://gyazo.com/0f0514e31d8b6136f87c33184b649b8d \n 切った後に剣を振り上げたタイミングでバフ付与')
    await ctx.message.delete()
@bot.command(name="キャル(サマー)")
async def mizukyaru(ctx):
    """キャル(サマー)"""
    await ctx.send('https://i.gyazo.com/cf8625a0f3fbe7ce5a47f00e2305568a')
    await ctx.message.delete()
@bot.command(name="コッコロ(プリンセス)")
async def purikoro(ctx):
    """コッコロ(プリンセス)"""
    await ctx.send('https://gyazo.com/04ffe3e6e434d79c816a837e435c1ff1')
    await ctx.message.delete()    
@bot.command(name="キョウカ(ハロウィン)")
async def harokyo(ctx):
    """キョウカ(ハロウィン)"""
    await ctx.send('https://i.gyazo.com/60d59c64eb5c8a9443bd4de074cc03de \n 箒を突き刺した時/箒を振り終わった後')
    await ctx.message.delete()
@bot.command(name="サレン(サマー)")
async def mizusaren(ctx):
    """サレン(サマー)"""
    await ctx.send('https://gyazo.com/c22d7996cb2d8e91ae7308b53c66d6d4 \n 右を向いた時')
    await ctx.message.delete()
@bot.command(name="コッコロ(ニューイヤー)")
async def nyukkoro(ctx):
    """コッコロ(ニューイヤー)"""
    await ctx.send('https://gyazo.com/c29e006bf82ce2fb0e3b44c06405a9ce \n 左を向いた時')
    await ctx.message.delete()    
@bot.command(name="ミミ(ハロウィン)")
async def haromimi(ctx):
    """ミミ(ハロウィン)"""
    await ctx.send('https://i.gyazo.com/42f21611ee06890d48f4ffd4d38e6476 \n ぴょん ぴょん ぴょこ←ｺｺ')
    await ctx.message.delete()
@bot.command(name="シズル(バレンタイン)")
async def bazuru(ctx):
    """シズル(バレンタイン)"""
    await ctx.send('https://i.gyazo.com/87b47efe83e874247b66519ce2caa78b')
    await ctx.message.delete()
@bot.command(name="チカ(クリスマス)")
async def kuritika(ctx):
    """チカ(クリスマス)"""
    await ctx.send('https://i.gyazo.com/d9b5fcdfca2cac56f82cfd1c9feefd9d \n 足元に魔法陣が出たら/tp配布の数字を見る')
    await ctx.message.delete()    
@bot.command(name="ユニ")
async def yuni(ctx):
    """ユニ"""
    await ctx.send('https://gyazo.com/67a7c23623583779f069e697df22aa23 \n どちらもジャンプ着地時')
    await ctx.message.delete()
@bot.command(name="レイ")
async def rei(ctx):
    """レイ"""
    await ctx.send('https://i.gyazo.com/4dd4fbfc1687f4529e2f474a84c7a991')
    await ctx.message.delete()
@bot.command(name="スズナ")
async def suzuna(ctx):
    """スズナ"""
    await ctx.send('https://gyazo.com/0f21de3dba9d6d69dee31ef7991b71fc')
    await ctx.message.delete()
@bot.command(name="アン")
async def an(ctx):
    """アン"""
    await ctx.send('https://gyazo.com/4771ba5961617b5d66e8fe2aacdc3562')
    await ctx.message.delete()
@bot.command(name="ミサト")
async def misato(ctx):
    """ミサト"""
    await ctx.send('https://gyazo.com/d759d75e36acd6942f1e20d5bf5654ba')
    await ctx.message.delete() 
@bot.command(name="マホ(サマー)")
async def mizumaho(ctx):
    """マホ(サマー)"""
    await ctx.send('https://gyazo.com/2848612666b463901e2960c0282685b5')
    await ctx.message.delete()
@bot.command(name="ミソギ(ハロウィン)")
async def haromiso(ctx):
    """ミソギ(ハロウィン)"""
    await ctx.send('https://gyazo.com/667afa5b86200885f706cd8cf65e7651')
    await ctx.message.delete()
@bot.command(name="ヒヨリ")
async def hiyori(ctx):
    """ヒヨリ"""
    await ctx.send('https://gyazo.com/0fceb161f3ddeb1807f048271416525f')
    await ctx.message.delete()


@bot.command(name="持越し時間計算")
async def motikosi(ctx, boss: int, p1: int, p2: int):
    """持越し時間計算機"""
    if total > boss:
        cotime = 90 - (90*(boss-p1)/p2) + 20
        text = "持ち越し時間は" + str(cotime) + "秒です"       
    else:
        text = "持ち越しは発生しません"
    await ctx.send(text)
     

bot.run(token)

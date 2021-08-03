import discord
from discord.ext import commands
import random

#プレフィック
client = commands.Bot(command_prefix = '!')

#起動時のイベント
@client.event
async def on_ready():
    print('ready')
    CHANNEL_ID = 1234567890123
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('ぱんつ')
    #ステータス
    await client.change_presence(activity=discord.Game(name='起動中'))

#コード1(メッセージ)
@client.command()
async def test(ctx):
    await ctx.send('うひょー')
    #10秒後に消える
    await ctx.send('ぱんつ',delete_after=10.0 )


#コード2(画像)
@client.command()
async def test2(ctx):
    #10秒後に消える
    await ctx.send(file=discord.File('送りたい画像のパス'),delete_after=10.0 )

#part3
#コード4(ステータス2)
@client.command()
async def test3(ctx):
    await client.change_presence(activity=discord.Game(name='2'))

#コード5(ping)
@client.command()
async def test4(ctx):
    await ctx.send('ping {0} ms'.format(round(client.latency)))

#コード6(embed)
@client.command()
async def test5(ctx):
    embed=discord.Embed(title='テスト', description='パンツ')
    await ctx.send(embed=embed)

#コード7(ランダムチョイス)
#画像の場合await ctx.send(file=discord.File(f'{random.choice(j)}'))
@client.command()
async def test6(ctx):
    j = ['グー',
         'チョキ',
         'パー'
         ]
    await ctx.send(random.choice(j))

#トークン
client.run('あなたのとーくん')
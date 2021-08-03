from discord.ext import commands
import os
import traceback
import discord

token = os.environ['DISCORD_BOT_TOKEN']

intents = discord.Intents.defalut()
intents.member = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/")


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def nya(ctx):
    await ctx.send('nya')

@bot.command()
async def wan(ctx):
    await ctx.send('wan')

@bot.command()
async def drink(ctx):
    embed=discord.Embed(title='DRINKS')
    embed.add_field(name='ビール', value=':beer:')
    embed.add_field(name='ワイン', value=':wine_glass:')
    embed.add_field(name='ウイスキー', value=':whisky:')
    embed.add_field(name='その他', value=':cocktail:')
    embed.add_field(name='ジュース', value=':tropical_drink:')
    await ctx.send(embed=embed)

def get_data(message):
    command = message.content
    data_table = {
        '/members': message.guild.members, # メンバーのリスト
        '/roles': message.guild.roles, # 役職のリスト
        '/text_channels': message.guild.text_channels, # テキストチャンネルのリスト
        '/voice_channels': message.guild.voice_channels, # ボイスチャンネルのリスト
        '/category_channels': message.guild.categories, # カテゴリチャンネルのリスト
    }
    return data_table.get(command, '無効なコマンドです')

@client.command()
async def mem(ctx):
    await ctx.send(ctx.channel.members)

@bot.command()
async def mem2(ctx):
    await ctx.send(ctx.channel.members)



bot.run(token)


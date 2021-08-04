from discord.ext import commands
import os
import traceback
import discord
from typing import Optional

intents = discord.Intents.all()
intents.typing = False  # typingを受け取らないように
intents.members = True
bot = commands.Bot(commands.when_mentioned_or("!"), intents=intents)
token = os.environ['DISCORD_BOT_TOKEN']

num = 0


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

"""
@bot.command()
async def drink(ctx):
    global num
    num += 1
    embed=discord.Embed(title='DRINKS')
    embed.add_field(name='ビール', value=':beer:')
    embed.add_field(name='ワイン', value=':wine_glass:')
    embed.add_field(name='ウイスキー', value=':whisky:')
    embed.add_field(name='その他', value=':cocktail:')
    embed.add_field(name='ジュース', value=':tropical_drink:')
    await ctx.send(embed=embed)
    await ctx.send(num)


@bot.command()
async def hito(ctx):
    await ctx.send(ctx.channel.members)
"""




bot.run(token)


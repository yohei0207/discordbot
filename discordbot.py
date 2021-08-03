from discord.ext import commands
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


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
    embed=discord.Embed(title='ビール', description=':beer:')
    await ctx.send(embed=embed)
    embed=discord.Embed(title='ワイン', description=':wine_glass:')
    await ctx.send(embed=embed)
    embed=discord.Embed(title='ウイスキー', description=':whisky:')
    await ctx.send(embed=embed)
    embed=discord.Embed(title='その他', description=':cock_tail:')
    await ctx.send(embed=embed)
    embed=discord.Embed(title=' ジュース', description=':tropical_drink:')
    await ctx.send(embed=embed)

bot.run(token)

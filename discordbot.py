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
    embed=discord.Embed(title='DRINKS')
    embed.add_field(name='ビール', value=':beer:', inline = False)
    embed.add_field(name='ワイン', value=':wine_glass:', inline = False)
    embed.add_field(name='ウイスキー', value=':wihisky:', inline = False)
    embed.add_field(name='その他', value=':cocktail:', inline = False)
    embed.add_field(name='ジュース', value=':tropical_drink:', inline = False)
    await ctx.send(embed=embed)

bot.run(token)

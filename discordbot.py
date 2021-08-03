from discord.ext import commands
import os
import traceback
import discord

token = os.environ['DISCORD_BOT_TOKEN']


client = discord.Client()
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

@client.command()
async def mem(ctx):
    await ctx.send(ctx.channel.members)

@bot.command()
async def mem2(ctx):
    await ctx.send(ctx.channel.members)



bot.run(token)


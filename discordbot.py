from discord.ext import commands
import os
import traceback
import random

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
async def neko(ctx):
    await ctx.send('nya')

@bot.command()
async def talk(ctx):
    count = 0
    f = open('talk.txt', 'r')
    datalist = f.readlines()
    for data in datalist:
        count+=1
    r = random.randint(0, count-1)
    await ctx.send(datalist[r])

bot.run(token)
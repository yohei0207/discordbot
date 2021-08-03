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

@bot.event
async def on_ready():
    print('ready')
    CHANNEL_ID = 1234567890123456
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send('ぱんつ')

bot.run(token)

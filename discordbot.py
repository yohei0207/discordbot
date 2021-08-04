from discord.ext import commands
import os
import traceback
import discord


intents = discord.Intents.default()
intents.typing = False  # typingを受け取らないように
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)
token = os.environ['DISCORD_BOT_TOKEN']

members = []

beers = []
wines = []
coaktails = []
nomi_flag = True

num = 0


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


"""
@bot.event
async def on_ready(ctx):
    global members
    all_members = ctx.channel.members
    for member in all_members:
        members.append(member)
"""



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
    global members, beers, wines, coaktails, nomi_flag

    all_members = ctx.channel.members
    for member in all_members:
        if member.bot == False:
            data = (member.id, member.name, member.discriminator)
            members.append(data)
    members = list(set(members))

    for member in all_members:
        if member.bot == False:
            if nomi_flag == True:
                data = {member.id, 0}
                beers.append(data)
                wines.append(data)
                coaktails.append(data)
                nomi_flag = False

    await ctx.send(members)
    await ctx.send(beers)
    await ctx.send(wines)
    await ctx.send(coaktails)


@bot.command()
async def dare(ctx):
    await ctx.send(ctx.author.id)



#DRINKS
@bot.command()
async def beer(ctx):
    global beers
    the_member = ctx.author.id
    for br in beers:
        the_id = br[0]
        if the_id == the_member:
            br[1] += 1
            break
    


@bot.command()
async def nomi(ctx):
    global beers, wines, coaktails
    ctx.send(beers)
    ctx.send(wines)
    ctx.send(coaktails)





bot.run(token)

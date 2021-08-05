from posix import NGROUPS_MAX
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
async def drink_menu(ctx):
    embed=discord.Embed(title='DRINKS')
    embed.add_field(name='/beer', value='ビール')
    embed.add_field(name='/wine', value='ワイン')
    embed.add_field(name='/cocktail', value='カクテル')
    await ctx.send(embed = embed)
    


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

                data = [member.id, 0]
                data2 = [member.id, 0]
                data3 = [member.id, 0]
                beers.append(data)
                wines.append(data2)
                coaktails.append(data3)
    nomi_flag = False



  


@bot.command()
async def dare(ctx):
    await ctx.send(ctx.author.id)



#DRINKS
@bot.command()
async def beer(ctx):
    br = "\N{BEER MUG}"
    global beers
    the_member = ctx.author.id
    the_member_name = ctx.author.name
    for br in beers:
        the_id = br[0]
        if the_id == the_member:
            br[1] += 1
            break
    await ctx.send(br)
    await ctx.send(the_member_name + "さんビール一丁追加！")

    

@bot.command()
async def wine(ctx):
    global wines
    wn = "\N{WINE GLASS}"
    the_member = ctx.author.id
    the_member_name = ctx.author.name
    for wn in wines:
        the_id = wn[0]
        if the_id == the_member:
            wn[1] += 1
            break
    await ctx.send(wn)
    await ctx.send(the_member_name + "さんワイン一杯追加！")
    

@bot.command()
async def cocktail(ctx):
    global coaktails
    ct = "\N{COCKTAIL GLASS}"
    the_member = ctx.author.id
    the_member_name = ctx.author.name
    for ct in coaktails:
        the_id = ct[0]
        if the_id == the_member:
            ct[1] += 1
            break
    await ctx.send(ct)
    await ctx.send(the_member_name + "さんカクテル一杯追加！")
    


@bot.command()
async def all_nomi(ctx):
    global members, beers, wines, coaktails

    mybr = 0
    mywn = 0
    myct = 0
    myname = 0

    
    for mem in members:
        myid = mem[0]
        myname = mem[1]

        for br in beers:
            if br[0] == myid:
                mybr = br[1]
                break
    
        for wn in wines:
            if wn[0] == myid:
                mywn = wn[1]
                break

        for ct in coaktails:
            if ct[0] == myid:
                myct = ct[1]
                break
    
        embed = discord.Embed(title=myname + "さんの飲み状況",color=0xff0000) #16進数カラーコード
        embed.add_field(name="ビール",value=mybr)
        embed.add_field(name="ワイン",value=mywn)
        embed.add_field(name="カクテル",value=myct)
    
        await ctx.send(embed = embed)






@bot.command()
async def my_nomi(ctx):
    global beers, wines, coaktails

    mybr = 0
    mywn = 0
    myct = 0
    myname = 0

    myid = ctx.author.id
    myname = ctx.author.name
    for mem in members:
        if mem[0] == myid:
            myname = mem[1]
            break

    for br in beers:
        if br[0] == myid:
            mybr = br[1]
            break
    
    for wn in wines:
        if wn[0] == myid:
            mywn = wn[1]
            break

    for ct in coaktails:
        if ct[0] == myid:
            myct = ct[1]
            break
    
    sum_nomi = mybr + mywn + myct
    
    embed = discord.Embed(title=myname,description="あなたの飲み状況",color=0xff0000) #16進数カラーコード
    embed.add_field(name="ビール",value=mybr)
    embed.add_field(name="ワイン",value=mywn)
    embed.add_field(name="カクテル",value=myct)
    if sum_nomi >= 5:
        await ctx.send("飲みすぎ！！")

    
    await ctx.send(embed = embed)


"""
@bot.event
async def on_message(message):
    
    if message.author.bot:
        return
    #UnicodeEmoji = "\N{SMILING FACE WITH OPEN MOUTH AND TIGHTLY-CLOSED EYES}"

    br = "\N{BEER MUG}"
    wn = "\N{WINE GLASS}"
    ct = "\N{COCKTAIL GLASS}"

    await bot.process_commands(message)

    #await message.add_reaction(UnicodeEmoji)
    
    await message.add_reaction(br)
    await message.add_reaction(wn)
    await message.add_reaction(ct)




@bot.event
async def on_reaction_add(reaction, user):
    # author: リアクションがついたメッセージを書いた人
    global num
    num += 1
    await bot.process_commands(reaction)

    #channel = bot.get_channel(871029026163159104)
    #await channel.send('おはよう！')
    await bot.delete_message(reaction)



@bot.command()
async def greet(ctx):
    channel = bot.get_channel(871029026163159104)
    await channel.send('おはよう！')
"""

@bot.command()
async def hogehoge(ctx):
    global num
    await ctx.send(num)


bot.run(token)

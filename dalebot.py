## DBOSS

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time

bot = commands.Bot(command_prefix='!')

#############################################
# OPEN INSTANCE                             #
############################################# 
@bot.event
async def on_ready():
    print ("Ready when you are!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

#############################################
# DALE COMMAND                              #
############################################# 
@bot.command(pass_context=True)
async def dale(ctx):
    author = ctx.message.author
    role = discord.utils.get(author.server.roles, name="Looking for Games")
    await bot.remove_roles(author, role)
    await bot.add_roles(author, role)
    await asyncio.sleep(1800)
    await bot.remove_roles(author, role)

#############################################
# NODALE COMMAND                            #
############################################# 
@bot.command(pass_context=True)
@commands.has_role("Looking for Games")
async def nodale(ctx):
    author = ctx.message.author
    role = discord.utils.get(author.server.roles, name="Looking for Games")
    await bot.remove_roles(author, role)

bot.run("NTE0MTU5NDc2MzUwMTI0MDUy.DtUj6w.JzbnCy28EbPb5zMSpPm7dSa4ZZ0")

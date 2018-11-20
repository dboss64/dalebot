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

@bot.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)

bot.run("NTE0MTU5NDc2MzUwMTI0MDUy.DtSi2g.21onVzX_sMW_bGFMhgpnRjFeQfY")
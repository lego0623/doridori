import asyncio,discord,os
from discord import message
from discord import channel
from discord import client
from discord.ext import commands
from discord.utils import deprecated
from discord.utils import get
import requests
from bs4 import BeautifulSoup
import time
import random

game = discord.Game("!!명령어 입력")
bot = commands.Bot(command_prefix='!!',Status=discord.Status.online,activity=game,help_command=None)


@bot.event
async def on_ready():
    print("마이야히 마이야하")

@bot.event
async def on_message(message):
    await message.author.edit(nick="some new nick")

# @bot.command(name="혁명", pass_context=True)
# async def HumanRole(ctx, member: discord.Member=None):
#     member = member or ctx.message.author
#     await member.add_roles(get(ctx.guild.roles, name="봇"))
#     await ctx.channel.send(str(member)+"에게 역할이 적용되었습니다.")

bot.run("ODYzNDM4OTI0NTU3NzEzNDYw.YOm6KQ.6TBZ25nnhkJPyfQODNPJ3tmTASA")
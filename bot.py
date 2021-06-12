import asyncio,discord,os
from discord.ext import commands

game = discord.Game("!!명령어 입력")
bot = commands.Bot(command_prefix='!!',Status=discord.Status.online,activity=game,help_command=None)
mafia_game_ready = False
mafia_gameing = False
mafia_game_count = 0

@bot.event
async def on_ready():
    print("마이야히 마이야하")

@bot.command()
async def 야(ctx):
    await ctx.send("왜 나 바쁜거 안보임?")

@bot.command()
async def 도움(ctx):
    await ctx.send("나 바빠 본론만 얘기해(!!도움_명령어)")

@bot.command()
async def 도움_명령어(ctx):
    await ctx.send("""
-야
-도움
-도움_명령어
""")

# @bot.command()
# async def 마피아게임(ctx):
#     bot.get_user(ctx.author.id).send("님 마피아")
#     mafia_game_ready = True
#     mafia_gmae_count = 0

# @bot.command()
# async def 마피아참가(ctx):
#     if(mafia_game_ready):
#         mafia_game_count += 1
#         while(mafia_gameing or not mafia_game_ready):
#             pass
#         if(mafia_gameing):
#             if ctx.author.dm_channel:
#                 await message.author.dm_channel.send("욕 좀 고마해라")
#             elif ctx.author.dm_channel is None:
#                 channel = await message.author.create_dm()
#                 await channel.send("욕 좀 고마해라")


@bot.event
async def on_member_join(member):
    await member.send("와 이딴 서버에 들어오는 흑우도 있다???!!")

bot.run("ODUyNzE2NDE4Mjc3MzEwNTA1.YMK4DA.i8fAUjrYm6kU3siaxljV2qJX_vQ")

# while(True):
#     if(mafia_game_ready):
#         if(mafia_game_count > 3):
#             time.sleep(20)
#             if(mafia_game_count > 3):
#                 mafia_gameing = True
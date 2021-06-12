import asyncio,discord,os
from discord.ext import commands
import requests
from bs4 import BeautifulSoup

game = discord.Game("!!명령어 입력")
bot = commands.Bot(command_prefix='!!',Status=discord.Status.online,activity=game,help_command=None)
mafia_game_ready = False
mafia_gameing = False
mafia_game_count = 0
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".","?","!","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

@bot.event
async def on_ready():
    print("마이야히 마이야하")

@bot.command()
async def 야(ctx):
    await ctx.send("왜 나 바쁜거 안보임?")

@bot.command()
async def 날씨(ctx):
    if(True):
        url = "https://weather.naver.com/today/02113128"
        result = requests.get(url)
        bs_obj = BeautifulSoup(result.content, "html.parser")

        no_today = bs_obj.find("strong", {"class": "current"}) # 태그 p, 속성값 no_today 찾기
        blind = no_today.find("span", {"class": "blind"}) # 태그 span, 속성값 blind 찾기
        now_price = blind.text
        await ctx.send("" + now_price + "도의 날씨라고 함")
        print("" + now_price + "도의 날씨라고 함")

@bot.command()
async def 도움(ctx):
    await ctx.send("나 바빠 본론만 얘기해(!!도움_명령어)")

@bot.command()
async def 도움_명령어(ctx):
    embed = discord.Embed(title=f"명령어", descriotion=f"이진봇", Color=0xf3bb76)
    embed.add_field(name=f"-!야",value=f"야", inline=False)
    embed.add_field(name=f"-!도움",value=f"딱히 쓸모없음", inline=False)
    embed.add_field(name=f"-!날씨",value=f"날씨를 알려줌", inline=False)
    embed.add_field(name=f"-!도움_명령어",value=f"명령어 목록", inline=False)
    await ctx.send(embed=embed)

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

def password():
    a = "01011010100010011001100110010101100001101001000110111011010110001000100100011011110101010110001010000001101111000101011001101001000110010111010110001100100011111011101000111000110111010101101010010111101010001000111110011100010001000000100100100001101001110100010010000011001001100010110010111101001101000010010011000011101000001010110001100110010000011100001101010010011000011100101110001110011000101111110101111"
    b = 0
    c = ""
    d = int(len(a)/7)

    for i in range(0, d):
        b = 0
        for j in range(i*7, i*7+7):
            if(a[j] == "1"):
                b = b*2+1
            elif(a[j] == "0"):
                b = b*2
        c = c+alphabet[b-1]
    bot.run(c)
password()

# while(True):
#     if(mafia_game_ready):
#         if(mafia_game_count > 3):
#             time.sleep(20)
#             if(mafia_game_count > 3):
#                 mafia_gameing = True
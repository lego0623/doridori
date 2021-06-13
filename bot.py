import asyncio,discord,os
from discord import message
from discord import channel
from discord.ext import commands
from discord.utils import deprecated
import requests
from bs4 import BeautifulSoup
import time
import random

game = discord.Game("@@명령어 입력")
bot = commands.Bot(command_prefix='@@',Status=discord.Status.online,activity=game,help_command=None)
mafia_game_ready = False
mafia_gameing = False
mafia_game_count = 0
if(True): # 끝말잇기 변수
    end_bind_ready = []
    end_binding = []
    end_bind_user = []
    end_bind_end = []
    end_bind_list = [] # 리스트
    end_bind_time = []
    end_bind_score = []
if(True): # 숫자야구 변수
    num_base_ready = []
    num_baseing = []
    num_base_user = []
    num_base_score = []
    num_base_home = []

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
        blind = no_today.find("span", {"class": "blind"}).get_text() # 태그 span, 속성값 blind 찾기
        now_price = blind
        await ctx.send("" + now_price + "도의 날씨라고 함")
        print("" + now_price + "도의 날씨라고 함")

@bot.command()
async def 도움(ctx):
    await ctx.send("나 바빠 본론만 얘기해(!!도움_명령어)")

# @bot.command()
# async def 숫자야구_도움():
#     embed = discord.Embed(title=f"숫자야구_사용방법", descriotion=f"도리도리봇", Color=0xf3bb76)
#     embed.add_field(name=f"-!!숫자야구_시작",value=f"숫자야구를 시작한다. (AI)", inline=False)
#     embed.add_field(name=f"-!!ㄹ",value=f"!!ㄹ (숫자)로 여부를 알수 있다.", inline=False)
#     embed.add_field(name=f"-!!ㄹ !포기!",value=f"숫자야구에서 항복을 요청한다.", inline=False)

# @bot.command()
# async def 끝말잇기_도움():
#     embed = discord.Embed(title=f"끝말잇기_사용방법", descriotion=f"도리도리봇", Color=0xf3bb76)
#     embed.add_field(name=f"-!!끝말잇기_시작",value=f"끝말잇기를 시작한다. (AI)", inline=False)
#     embed.add_field(name=f"-!!ㅇ",value=f"!!ㅇ (단어)로 끝말잇기를 이어갈 수 있다.", inline=False)
#     embed.add_field(name=f"-!!ㅇ !포기!",value=f"끝말잇기에서 항복을 요청한다.", inline=False)

# @bot.command()
# async def 끝말잇기_게임방법():
#     embed = discord.Embed(title=f"끝말잇기_규칙", descriotion=f"도리도리봇", Color=0xf3bb76)
#     embed.add_field(name=f"규칙 (1)",value=f"제시된 단어의 끝말을 잇는 단어를 말한다.", inline=False)
#     embed.add_field(name=f"규칙 (2)",value=f"제한시간은 10초이다.", inline=False)
#     embed.add_field(name=f"유의사항",value=f"단어가 봇의 데이터에 없을 수도 있다. 그럴때는 억울해 하면된다.", inline=False)

# @bot.command()
# async def 숫자야구_게임방법():
#     embed = discord.Embed(title=f"숫자야구_규칙", descriotion=f"도리도리봇", Color=0xf3bb76)
#     embed.add_field(name=f"규칙 (1)",value=f"숫자는 3자리 수임(000~999)", inline=False)
#     embed.add_field(name=f"규칙 (2)",value=f"제한 시간은 없음", inline=False)
#     embed.add_field(name=f"게임규칙 (1)",value=f"숫자가 정답숫자의 포함되어있으면 1볼(예: (정답: 1xx), (자신의 답: x1x))", inline=False)
#     embed.add_field(name=f"게임규칙 (2)",value=f"숫자가 정답숫자의 포함되어있고 위치도 같으면 1스트라이크(예: (정답: 1xx), (자신의 답: 1xx))", inline=False)
#     embed.add_field(name=f"게임규칙 (3)",value=f"숫자가 정답숫자의 포함되어있지않으면 없음(만일 3가지 숫자다 없을 경우 아웃(예: (정답: 123), (자신의 답: 456))", inline=False)
#     embed.add_field(name=f"게임규칙 (4)",value=f"모든 숫자의 위치가 같으면 3스트라이크 즉 게임 승(예: (정답: 123), (자신의 답: 123))", inline=False)

@bot.command()
async def 도움_명령어(ctx):
    embed = discord.Embed(title=f"명령어", descriotion=f"도리도리봇", Color=0xf3bb76)
    embed.add_field(name=f"-!!야",value=f"야", inline=False)
    embed.add_field(name=f"-!!도움",value=f"딱히 쓸모없음", inline=False)
    embed.add_field(name=f"-!!날씨",value=f"날씨를 알려줌(안됨)", inline=False)
    embed.add_field(name=f"-!!도움_명령어",value=f"명령어 목록", inline=False)
    embed.add_field(name=f"-!!도움_이진수",value=f"아잔슈 명령어 목록", inline=False)
    # embed.add_field(name=f"-!!끝말잇기_도움",value=f"끝말잇기 사용방법", inline=False)
    # embed.add_field(name=f"-!!끝말잇기_게임방법",value=f"끝말잇기 규칙", inline=False)
    # embed.add_field(name=f"-!!숫자야구_도움",value=f"숫자야구 사용방법", inline=False)
    # embed.add_field(name=f"-!!숫자야구_게임방법",value=f"숫자야구 규칙", inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    print("마이야히 마이야하")

@bot.command()
async def 도움_이진수(ctx):
    embed = discord.Embed(title=f"사용방법", descriotion=f"이진봇", Color=0xf3bb76)
    embed.add_field(name=f"-이진수를 십진수로",value=f"이진수_십진수 (이진수)", inline=False)
    embed.add_field(name=f"-십진수를 이진수로",value=f"십진수_이진수 (이진수)", inline=False)
    embed.add_field(name=f"-이진수를 영어로",value=f"이진수_영어 (이진수)", inline=False)
    embed.add_field(name=f"-영어를 이진수로",value=f"영어_이진수 (영어)", inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def 이진수_십진수(ctx, text):
    a = text
    b = 0
    for i in range(0, len(a)):
        if(a[i] == "1" and b == 0):
            b = 1
        elif(a[i] == "1"):
            b = b*2+1
        elif(a[i] == "0"):
            b = b*2

    await ctx.send(b) 

@bot.command()
async def 십진수_이진수(ctx, text):
    b = int(text)
    a = 0
    c = ""

    while(b!=1):
        a += 1
        if(b%2 == 1):
            b = (b-1)/2
            c = "1" + c
        else:
            b = b/2
            c = "0" + c

    c = "1" + c
    await ctx.send(c)

@bot.command()
async def 이진수_영어(ctx, text):
    a = text
    b = 0
    c = ""
    d = int(len(a)/5)

    for i in range(0, d):
        b = 0
        for j in range(i*7, i*7+7):
            if(a[j] == "1"):
                b = b*2+1
            elif(a[j] == "0"):
                b = b*2
        c = c+alphabet[b-1]


    print(c)
    await ctx.send(c)

@bot.command()
async def 영어_이진수(ctx, *, text):
    p = []

    o = text

    for i in range(0, len(o)):
        for j in range(0, len(alphabet)):
            if(alphabet[j] == o[i]):
                p.append(j+1)

    a = 0
    c = ""
    result = ""

    for k in range(0, len(p)):
        b=p[k]
        a=0
        c=""
        while(b!=1):
            a += 1
            if(b%2 == 1):
                b = (b-1)/2
                c = "1" + c
            else:
                b = b/2
                c = "0" + c

        c = "1" + c
        if(len(c) != 5):
            for ii in range(0, 5-len(c)):
                c = "0" + c

        result = result+c
    await ctx.send(result)



# @bot.command()
# async def 끝말잇기_시작(ctx):
#     msg = await ctx.send("끝말잇기가 5초 뒤에 시작합니다.")
#     for i in range(0, 4):
#         time.sleep(1)
#         await msg.edit(content='끝말잇기가 ' + str(4-i) + '초 뒤에 시작합니다.')
#     time.sleep(1)
#     await msg.edit(content='끝말잇기가 시작합니다.')
#     with open('words.txt', 'rt', encoding='UTF8') as f:
#         data = f.read()
#     file_list = data.splitlines()
#     first_word = file_list[random.randrange(0, len(file_list))]
#     # random.range()
#     await ctx.send("제시어: " + first_word + "")
#     await ctx.send("" + arg.author + "님 시작 단어(" + first_word[len(first_word)-1] + "") 
    


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


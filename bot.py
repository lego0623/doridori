import asyncio,discord,os
from discord import message
from discord import channel
from discord.ext import commands
from discord.utils import deprecated
import requests
from bs4 import BeautifulSoup
import time
import random

game = discord.Game("!!명령어 입력")
bot = commands.Bot(command_prefix='!!',Status=discord.Status.online,activity=game,help_command=None)
mafia_game_ready = False
mafia_gameing = False
mafia_game_count = 0
end_bind_ready = False
end_binding = False
end_bind_user = ""
end_bind_end = ""
end_bind_list = []
end_bind_time = False
end_bind_score = 0
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",".","?","!","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
with open('words.txt', 'rt', encoding='UTF8') as f:
    data = f.read()
file_list = data.splitlines()

@bot.event
async def on_message(message):
    global end_bind_end
    global end_bind_list
    global end_bind_ready
    global end_bind_user
    global end_binding
    global end_bind_time
    global end_bind_score
    if(message.content.startswith('!!끝말잇기_시작') and not end_binding):
        msg = await message.channel.send("끝말잇기가 5초 뒤에 시작합니다.")
        for i in range(0, 4):
            time.sleep(1)
            await msg.edit(content='끝말잇기가 ' + str(4-i) + '초 뒤에 시작합니다.')
        time.sleep(1)
        await msg.edit(content='끝말잇기가 시작합니다.')
        end_binding = True
        end_bind_time = True
        end_bind_user = str(message.author)
        first_word = file_list[random.randrange(0, len(file_list))]
        # random.range()
        await message.channel.send("제시어: " + first_word + "")
        await message.channel.send("" + str(message.author) + "님 시작 단어(" + first_word[len(first_word)-1] + ")") 
        end_bind_end = first_word
    if(message.content.startswith("!!ㅇ")):
        print(str(message.content))
        print(end_bind_end)
        print(str(message.content[len(str(message.content))-1]))
        aghdg = []
        if(end_binding):
            if(str(message.content) == "!!ㅇ !포기!"):
                if(end_bind_time):
                    await message.channel.send(content='당신이 졌군요 /' + str(end_bind_score) + '점/패배')
                    end_bind_ready = False
                    end_binding = False
                    end_bind_user = ""
                    end_bind_end = ""
                    end_bind_list = []
                    end_bind_time = False
                    end_bind_score = 0
            else:
                if(str(message.content[4]) == end_bind_end[len(end_bind_end)-1] and str(message.author) == end_bind_user):
                    print("asdfds")
                    if(message.content[4:len(message.content)] in file_list and not message.content[4:len(message.content)] in end_bind_list):
                        end_bind_time = False
                        end_bind_score += 1
                        for ggg in range(0, len(file_list)):
                            if(message.content[len(message.content)-1] == file_list[ggg][0]):
                                aghdg.append(file_list[ggg])
                        end_bind_end = aghdg[random.randrange(0, len(aghdg))]
                        end_bind_list.append(end_bind_end)
                        try:
                            await message.channel.send("" + end_bind_end + ", " + str(message.author) + "님 시작 단어(" + end_bind_end[len(end_bind_end)-1] + ")") 
                            print(end_bind_end)
                            msg = await message.channel.send("10초 남음")
                            end_bind_time = True
                            for ijk in range(0, 10):
                                if(end_bind_time):
                                    time.sleep(1)
                                if(end_bind_time):
                                    await msg.edit(content='' + str(10-ijk) + '초 남음')
                            if(end_bind_time):
                                time.sleep(1)
                            if(end_bind_time):
                                await msg.edit(content='당신이 졌군요 /' + str(end_bind_score) + '점/패배')
                                end_bind_ready = False
                                end_binding = False
                                end_bind_user = ""
                                end_bind_end = ""
                                end_bind_list = []
                                end_bind_time = False
                                end_bind_score = 0      
                        except:
                            await message.msg.edit("워우...제가 졌군요... /" + str(end_bind_score) + "점/승리")
                            end_bind_ready = False
                            end_binding = False
                            end_bind_user = ""
                            end_bind_end = ""
                            end_bind_list = []
                            end_bind_time = False
                            end_bind_score = 0  


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

@bot.command()
async def 도움_명령어(ctx):
    embed = discord.Embed(title=f"명령어", descriotion=f"이진봇", Color=0xf3bb76)
    embed.add_field(name=f"-!!야",value=f"야", inline=False)
    embed.add_field(name=f"-!!도움",value=f"딱히 쓸모없음", inline=False)
    embed.add_field(name=f"-!!날씨",value=f"날씨를 알려줌", inline=False)
    embed.add_field(name=f"-!!도움_명령어",value=f"명령어 목록", inline=False)
    await ctx.send(embed=embed)

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
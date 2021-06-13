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

@bot.event
async def on_message(message): #끝말잇기
    if(True): # 숫자야구
        global num_base_ready
        global num_baseing
        global num_base_user
        global num_base_score
        global num_base_home
        if(message.content == "!!숫자야구_시작"):
            print("sfgf")
            if(not message.author in num_base_user): #not num_baseing
                num_base_user.append(message.author)
                user_id_base = num_base_user.index(message.author) 
                num_base_user.append(message.author)
                num_baseing.append(True)
                num_base_score.append(0)
                num_base_home.append("")
                msg = await message.channel.send("숫자야구를 시작합니다(3자리 숫자)")
                while(not len(num_base_home[user_id_base])==3):
                    ab = str(random.randrange(0,10))
                    if(len(num_base_home[user_id_base]) == 0):
                        num_base_home[user_id_base] = num_base_home[user_id_base] + ab
                        print(ab)
                    if(len(num_base_home[user_id_base]) == 1):
                        if(not(ab == num_base_home[user_id_base][0])):
                            num_base_home[user_id_base] = num_base_home[user_id_base] + ab
                            print(ab)
                    if(len(num_base_home[user_id_base]) == 2):
                        if(not(ab == num_base_home[user_id_base][0] or ab == num_base_home[user_id_base][1])):
                            num_base_home[user_id_base] = num_base_home[user_id_base] + ab
                            print(ab)
                print(num_base_home[user_id_base])
                
        if(message.content.startswith("!!ㄹ ")):
            if(message.author in num_base_user):
                user_id_base = num_base_user.index(message.author)
                print(str(num_base_score),str(user_id_base))
                if(message.content == "!!ㄹ !포기!"):
                    await message.channel.send("당신이 졌습니다. /" + str(num_base_score[int(user_id_base)]) + "회 만에 항복")
                    del num_baseing[user_id_base]
                    del num_base_user[user_id_base]
                    del num_base_score[user_id_base]
                    del num_base_home[user_id_base]
                else:
                    sbo = ""
                    try:
                        print(message.content[4:7])
                        if(int(message.content[4:7])):
                            pass
                        print("a1")
                        for i in range(0,len(num_base_home[user_id_base])):
                            print("a2")
                            if(message.content[i+4] == num_base_home[user_id_base][i]):
                                sbo = sbo + "S"
                            if(message.content[i+4] != num_base_home[user_id_base][i]):
                                ag = False
                                for jk in range(0,len(num_base_home[user_id_base])):
                                    if(message.content[i+4] == num_base_home[user_id_base][jk]):
                                        sbo = sbo + "B"
                                        ag = True
                                if(not ag):
                                    sbo = sbo + "N"
                        print("a3")
                        if(sbo == "NNN"):
                            await message.channel.send("" + message.content[4:7] + ", 0스트라이크/0볼/아웃!")
                            num_base_score[int(user_id_base)] = int(num_base_score[int(user_id_base)])+1
                        elif(sbo == "SSS"):
                            await message.channel.send("" + message.content[4:7] + ", 3스트라이크/0볼! " + str(num_base_score[user_id_base]) + "회만에 게임 승리!")
                            del num_baseing[user_id_base]
                            del num_base_user[user_id_base]
                            del num_base_score[user_id_base]
                            del num_base_home[user_id_base]
                            print("r")
                        elif(sbo == "BBB"):
                            print("r23")
                            await message.channel.send("" + message.content[4:7] + ", 0스트라이크/3볼")
                            num_base_score[int(user_id_base)] = int(num_base_score[int(user_id_base)])+1
                        elif(not sbo == "NNN" and not sbo == "SSS" and not sbo == "BBB"):
                            print("r2")
                            strike = 0
                            ball = 0
                            for jklo in range(0, len(sbo)):
                                if(sbo[jklo] == "S"):
                                    strike += 1
                                if(sbo[jklo] == "B"):
                                    ball += 1
                            await message.channel.send("" + message.content[4:7] + ", " + str(strike) + "스트라이크/" + str(ball) + "볼")
                            num_base_score[int(user_id_base)] = int(num_base_score[int(user_id_base)])+1
                    except:
                        await message.channel.send("!!ㄹ (숫자)로 적어주십시오(숫자는 3자리 숫자입니다. (예:!!ㄹ 123))")
    if(True): # 끝말잇기
        global end_bind_end
        global end_bind_list
        global end_bind_ready
        global end_bind_user
        global end_binding
        global end_bind_time
        global end_bind_score
        if(message.content.startswith('!!끝말잇기_시작') and not message.author in end_bind_user):
            msg = await message.channel.send("끝말잇기가 5초 뒤에 시작합니다.")
            for i in range(0, 4):
                time.sleep(1)
                await msg.edit(content='끝말잇기가 ' + str(4-i) + '초 뒤에 시작합니다.')
            time.sleep(1)
            await msg.edit(content='끝말잇기가 시작합니다.')
            end_binding.append(True)
            end_bind_time.append(True)
            end_bind_user.append(str(message.author))
            first_word = file_list[random.randrange(0, len(file_list))]
            # random.range()
            await message.channel.send("제시어: " + first_word + "")
            await message.channel.send("" + str(message.author) + "님 시작 단어(" + first_word[len(first_word)-1] + ")") 
            end_bind_end.append(first_word)
        if(message.content.startswith("!!ㅇ")):
            print(str(message.content))
            # print(end_bind_end)
            print(str(message.content[len(str(message.content))-1]))
            aghdg = []
            if(message.author in end_bind_user):
                user_id_base2 = end_bind_user.index(message.author)
                if(end_binding[user_id_base2]):
                    if(str(message.content) == "!!ㅇ !포기!"):
                        if(end_bind_time[user_id_base2]):
                            await message.channel.send(content='당신이 졌군요 /' + str(end_bind_score[user_id_base2]) + '점/패배')
                            del end_bind_ready[user_id_base2]
                            del end_binding[user_id_base2]
                            del end_bind_user
                            del end_bind_end
                            del end_bind_list
                            del end_bind_time
                            del end_bind_score
                    else:
                        if(str(message.content[4]) == end_bind_end[user_id_base2][len(end_bind_end)-1] and str(message.author) == end_bind_user[user_id_base2]):
                            print("asdfds")
                            if(message.content[4:len(message.content)] in file_list and not message.content[4:len(message.content)] in end_bind_list[user_id_base2]):
                                end_bind_time[user_id_base2] = False
                                end_bind_score[user_id_base2] += 1
                                for ggg in range(0, len(file_list)):
                                    if(message.content[len(message.content)-1] == file_list[ggg][0]):
                                        aghdg.append(file_list[ggg])
                                end_bind_end[user_id_base2] = aghdg[random.randrange(0, len(aghdg))]
                                end_bind_list[user_id_base2].append(end_bind_end[user_id_base2])
                                print(end_bind_list[user_id_base2])
                                try:
                                    await message.channel.send("" + end_bind_end[user_id_base2] + ", " + str(message.author) + "님 시작 단어(" + end_bind_end[user_id_base2][len(end_bind_end[user_id_base2])-1] + ")") 
                                    print(end_bind_end[user_id_base2])
                                    msg = await message.channel.send("10초 남음")
                                    end_bind_time[user_id_base2] = True
                                    for ijk in range(0, 10):
                                        if(end_bind_time[user_id_base2]):
                                            time.sleep(1)
                                        if(end_bind_time[user_id_base2]):
                                            await msg.edit(content='' + str(10-ijk) + '초 남음')
                                    if(end_bind_time[user_id_base2]):
                                        time.sleep(1)
                                    if(end_bind_time[user_id_base2]):
                                        await msg.edit(content='당신이 졌군요 /' + str(end_bind_score[user_id_base2]) + '점/패배')
                                        del end_bind_ready[user_id_base2]
                                        del end_binding[user_id_base2]
                                        del end_bind_user
                                        del end_bind_end
                                        del end_bind_list
                                        del end_bind_time
                                        del end_bind_score 
                                except:
                                    await message.msg.edit("워우...제가 졌군요... /" + str(end_bind_score[user_id_base2]) + "점/승리")
                                    del end_bind_ready[user_id_base2]
                                    del end_binding[user_id_base2]
                                    del end_bind_user
                                    del end_bind_end
                                    del end_bind_list
                                    del end_bind_time
                                    del end_bind_score
    if(True): # 복불복
        if(message.content.startswith('!!복불복 ')):
            try:
                if(int(message.content[6:len(message.content)])):
                    pass
                total = int(message.content[6:len(message.content)])
                if(random.randrange(0, total) == 0):
                    await message.channel.send("당첨되셨습니다!")
                else:
                    await message.channel.send("꽝!")
            except:
                await message.channel.send("* !!복불복 (숫자)의 형태로 적어주세요. (확률: 1/(숫자))")
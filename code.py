import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.voice_client import VoiceClient
import asyncio
import time
import random
import os
from discord import opus

OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']
 
def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True
 
    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass
 
    raise RuntimeError('Could not load an opus lib. Tried %s' % (', '.join(opus_libs)))
 
 
load_opus_lib()
BOT_PREFIX = ("") 
for ext in  ["music"]:
    bot.load_extension(ext)


TOKEN = "NDM4MzAxMzk5MjUyNzI5ODU2.DcH4lw.RmhcVZfW81uq1LsTEQSz8rd6nH8"
 

bot = Bot(command_prefix=BOT_PREFIX)
client = discord.Client()




@bot.event
async def on_ready():
	print('시작!')
	await bot.change_presence(game=discord.game(name='Gendo37이랑 코드 손보는중 '))

class Main_Commands():
        def __init__(self, bot):
         self.bot = bot
        def setup(bot):
            bot.add_cog(Music(bot))
            print("Music is loaded")

@bot.command()
async def 냥이():
    possible_responses = [
        '왜 불렀느냐',
        '왜 그러느냐',
        '무슨 문제있느냐',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 안녕():
    possible_responses = [
        '인사를 받아주겠느니라',
        '갑자기 인사를 왜 하는것이냐',
        '안녕하느냐',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 고마워():
    possible_responses = [
        '치...칭찬을 한다고..  내가 널 좋아할..것.. 같으냐..!.',
        '칭찬해준다고 아무것도 나오지 않느니라',
        '너 머리가 잘못된 것이냐 갑자기 이상한 말을 지껄이는 구나',
        '흥, 내가 잘했으니 당연히 칭찬을 받아야 하는 것이니라',

    ]
    await bot.say(random.choice(possible_responses))

@bot.command()
async def 놀아줘():
    possible_responses = [
        '그럴 시간에 우리 흰둥이나 신경쓰거라',
        '쯧 쯧 그러니 니가 머리가 나쁜것이니라',
        '귀찮느니라 혼자서 놀거라',
        '난 내 소중한 흰둥이랑 놀아줘야하니 귀찮게 하지 말거라',

    ]
    await bot.say(random.choice(possible_responses))

  

if __name__ == "__main__":
        for extension in startup_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                exc = '{}: {}' .format(type(e).__name__, e)
                print('failed to load extension {}/n{}'.format(extension, exc))

        


bot.run(os.environ(TOKEN))

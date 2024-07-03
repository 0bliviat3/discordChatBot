# install dicord lib

import configparser
import discord
from discord.ext import commands
from gtts import gTTS
import os

# 설정 파일 읽기
config = configparser.ConfigParser()
config.read('config.ini')

# 디스코드 봇 토큰 가져오기
token = config['discord']['token']

# 봇의 접두사와 토큰 설정
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# 봇이 준비되었을 때 출력할 메시지
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# 간단한 핑 명령어
@bot.command()
async def ping(ctx):
    await ctx.send('형이야~')

@bot.command()
async def hi(ctx):
    await ctx.send('안녕')

@bot.command()
async def agree(ctx):
    await ctx.send('인정맨으로서 인정드립니다')
    
# 봇이 음성 채널에 들어가도록 하는 명령어
@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("먼저 음성 채널에 들어가 주세요.")

# 봇이 음성 채널에서 나가도록 하는 명령어
@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("저는 현재 어떤 음성 채널에도 없습니다.")

# TTS 기능을 사용한 명령어
@bot.command()
async def tts(ctx, *, message: str):
    if ctx.voice_client:
        tts = gTTS(message, lang='ko')
        tts.save("tts.mp3")
        ctx.voice_client.play(discord.FFmpegPCMAudio("tts.mp3"), after=lambda e: os.remove("tts.mp3"))
    else:
        await ctx.send("먼저 봇을 음성 채널에 참가시켜 주세요.")
    
    
bot.run(token)
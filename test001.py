# install dicord lib

import discord
from discord.ext import commands

intentsd = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

async def on_ready():
    print(f'Logged in as {bot.user}')
    
#ping
async def ping(ctx):
    await ctx.send('Pong!')
    
    
bot.run('1165881760709696')
import discord
import os
from dotenv import load_dotenv
from scraper import getscore
from discord.ext import commands
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents=discord.Intents.default()
intents.message_content=True
client= discord.Client(intents=intents)#parameter is entered to fix an error:-Client.__init__() missing 1 required keyword-only argument: 'intents'

f=open(r'fact.txt','r')
r=f.read()
r=r.split('\n')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} has connected to discord:\n'
        f'{guild.name}(id:{guild.id})')
    
loadingmsg="Tallying the Scores..."
@client.event
async def on_message(message):
    if message.content == "/livescore":
        await message.channel.send(loadingmsg)
        
        await message.channel.send(getscore())
        
    elif message.content =="/help":
        await message.channel.send("Commands:\n")
        await message.channel.send("1)/livescore:-Generating Livescore\n")
        await message.channel.send("2)/generate:-Returns a csv of previous scrapes")
    elif message.content =="/generate":
        await message.channel.send("Fetching CSV...\n")
        file=discord.File("score.csv")
        await message.channel.send("Historians fear this csv",file=file)
    elif message.content=="/factme":
        #I wanted to scrape fact websites so hardddd for this. But, since time was low i decided to do it manually...it took 10 mins for this
        await message.channel.send(random.choice(r))
#getscore()
client.run(TOKEN)
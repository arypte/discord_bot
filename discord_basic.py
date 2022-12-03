import discord
from discord.ext import commands

Token = open("token", "r").readline()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())


@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)
    

@bot.command()
async def 따라하기(ctx,*,text):
    await ctx.send(text)
    
@bot.command()
async def play(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
bot.run(Token)


# 드라마 추천
# 제목 , 태그 , 방송사
# 간단한 게임 수도 퀴
import discord
import youtube_dl
import nest_asyncio


from discord.ext import commands
from to import Token , ydl_opts , func1 , func2
from cro import temper , s_r
from discord.voice_client import VoiceClient
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

nest_asyncio.apply()


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())
ydl = YoutubeDL(ydl_opts)


@bot.event
async def on_ready():
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)


@bot.command()
async def Hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def Play(ctx, *, song_title: str):
    # search for the song on YouTube
    ydl_opts = {
        'default_search': 'ytsearch',
        'quiet': True,
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    info = ydl.extract_info(song_title, download=False)

    song_url = info['entries'][0]['webpage_url']

    voice_client = await ctx.author.voice.channel.connect()
    player = discord.FFmpegPCMAudio(song_url)
    player = discord.PCMVolumeTransformer(player)
    voice_client.play(player, after=lambda: print('done'))

@bot.command()
async def Leave(ctx):
    await bot.voice_clients[0].disconnect()

@bot.command()
async def Menu(ctx):
    d = func1()
    output = d
    await ctx.send(output + "추천" )

@bot.command()
async def Help(ctx):
    commands = [
    ("hello", "인사를 합니다."),
    ("cody", "온도와 날씨, 그리고 거기에 맞는 옷을 추천합니다."),
    ("Menu" , "메뉴를 추천해줍니다.") ,
    ("play title", "현재 들어가 있는 보이스 채널에서 title을 재생합니다"), ]
    output = "\n".join([f"!{command}: {description}" for command, description in commands])
    await ctx.send(output)

print( temper , s_r ) 

@bot.command()
async def Cody(ctx):
    await ctx.send( "날씨 : " + temper + "°C " + s_r + "\n" )
    cmp = float(temper)
    output = func2( cmp )
    await ctx.send( output )

bot.run(Token)
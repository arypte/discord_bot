import discord
from discord.ext import commands
from to import Token
import requests
import youtube_dl


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
async def 안녕(ctx):
    await ctx.send("안녕하세요")
    
@bot.command()
async def song_start(voice, url):
    try:
        if not voice.is_playing() and not voice.is_paused():
            ydl_opts = {'format': 'bestaudio'}
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(f'https://www.youtube.com{url}', download=False) # 파일로 다운로드 하지 않고 재생
                URL = info['formats'][0]['url']
            
            voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        #voice.play(discord.FFmpegPCMAudio(executable = './ffmpeg-4.4-full_build-shared/bin/ffmpeg.exe', source='./song.mp3'))

        while voice.is_playing() or voice.is_paused():
            await asyncio.sleep(0.1)
    except:
        return

@bot.command(aliases = ['play', 'p', 'ㅔ'])
async def Play(ctx,*,  keyword):
    try:
        results = YoutubeSearch(keyword, max_results=1).to_dict() # title과 url_suffix를 사용. 자세한 내용은 하단 링크 참고

        channel = ctx.author.voice.channel
        if bot.voice_clients == []:
            await channel.connect()
            #await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))
        voice = bot.voice_clients[0]
        
        await song_start(voice, results[0]['url_suffix'])
    except:
        await ctx.send("Play Error")

bot.run(Token)


# 드라마 추천
# 제목 , 태그 , 방송사
# 명령어 있으면 유툽에서 , 없으면 멜론 차트 1위부터 플레이
# 음악봇, 멜론 차트 플레이 ,
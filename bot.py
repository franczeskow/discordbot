import discord
from discord.ext import commands
import random


def import_token():
    """Imports discord app token from token.txt"""

    with open("token.txt",) as f:
        token = f.read()
    return token


token = import_token()

# Discord command prefix "-"
client = commands.Bot(command_prefix="-")


async def play_smth(file_name,context):
    """Plays file chosen sound from /soundboard """

    file_name="soundboard/"+file_name
    voice_chanel = context.message.author.voice.channel
    v_client = await voice_chanel.connect()
    v_client.play(discord.FFmpegPCMAudio(file_name), after=lambda e: print('done', e))

    while v_client.is_playing():
        pass
    await v_client.disconnect()


# Is ok?
@client.event
async def on_ready():
    print("Everything ok!")

"""
Function that prints message on first text channel if any user changes it voice state ex.: mute, enter voice chanel,
leave voice chanel, kick  etc. Watch out very annoying.

@client.event
async def on_voice_state_update(member,before, after):
    with open("message.txt",) as f:
        message = f.read()
        
    channel_gen = client.get_all_channels()
    category_channel=next(channel_gen)
    first_text_channel = category_channel.channels[0]
    await first_text_channel.send(f"{member} {message}")
"""

@client.command()
async def cytat(ctx):
    """ Prints random line from teksty.txt file"""

    with open("teksty.txt", ) as f:
        teksty = f.readlines()

    random_text=random.choice(teksty)
    await ctx.send(random_text)
    f.close()


# Voice commands
@client.command()
async def ryszard(ctx):
    await play_smth("ryszard.mp3", ctx)


@client.command()
async def chlopi(ctx):
    await play_smth("chlopi.mp3", ctx)


@client.command()
async def kodeks(ctx):
    await play_smth("kodeks.mp3", ctx)


@client.command()
async def konie(ctx):
    await play_smth("konie.mp3", ctx)


@client.command()
async def lapowka(ctx):
    await play_smth("lapowka.mp3", ctx)


@client.command()
async def krzys(ctx):
    await play_smth("krzys.mp3", ctx)


@client.command()
async def lpg(ctx):
    await play_smth("lpg.mp3", ctx)


@client.command()
async def malpa(ctx):
    await play_smth("malpa.mp3", ctx)


@client.command()
async def ojciecpijo(ctx):
    await play_smth("ojciecpijo.mp3", ctx)


@client.command()
async def sanepid(ctx):
    await play_smth("sanepid.mp3", ctx)


@client.command()
async def tango(ctx):
    await play_smth("tango.mp3", ctx)

@client.command()
async def golota(ctx):
    await play_smth("golota.mp3", ctx)


client.run(token)

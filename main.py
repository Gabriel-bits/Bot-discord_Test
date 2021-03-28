import discord
from discord.ext import commands, tasks
from discord.ext.commands import AutoShardedBot
from secrect import Secret
import os, datetime
import asyncio

bot = discord.Client()


@bot.event
async def on_ready():
    print("Bot on")
    print(bot.user.name)
    print(bot.user.id)
    game = discord.Game("pica na sua mina")
    loopcanal.start()
    await bot.change_presence(status=discord.Status.idle, activity=game)
  

@tasks.loop(minutes=5)
async def loopcanal():
    dia_horas = datetime.datetime.now()
    canal = bot.get_channel(id=637407369554558978)
    await canal.send(f"** `{dia_horas.day}`d | `{dia_horas.hour}`h :`{dia_horas.minute}`m **")



# modulos = []

if __name__ == "__main__":
    # for modulo in modulos:
    #     bot.load_extension(modulo)


    bot.run(Secret)

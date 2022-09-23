from concurrent.futures import process
from unicodedata import name
import discord
from discord.ext import commands # Importando comandos da pasta discord.ext do pacote discord
from discord.flags import Intents
import asyncio

allIntents = discord.Intents.all() # Variavel para definir todas as intents
client = commands.Bot(command_prefix='*', intents=allIntents) #Usando intents= para declarar qual intent será usada. (No caso allIntents)


@client.event
async def on_ready():
    print("Olá, Mundo!")
    print("Tudo certo. Estou Online! :D")


@client.command(name="teste")
async def teste(context): # Criando função (def) teste
    await context.message.channel.send("Testado :D") #Enviar mensagem no mesmo canal do comando


@client.command(name='avatar')
async def ping(ctx):
    await ctx.message.channel.send(client.av)



client.run("MTAyMjI5MjA3NDY1OTMyODAyMQ.GM9yDm.DO749CH6VOOYRL-wM1lKQ9_w7aK16SH2IFgMuI") # Acionar bot.
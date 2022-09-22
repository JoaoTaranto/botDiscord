from unicodedata import name
import discord
from discord.ext import commands # Importando comandos da pasta discord.ext do pacote discord
from discord.flags import Intents
import asyncio

allIntents = discord.Intents.all() # Variavel para definir todas as intents
client = commands.Bot(command_prefix='*', intents=allIntents) #Usando intents= para declarar qual intent será usada. (No caso allIntents)


@client.event
async def on_ready():
    print("I'm Ready!")


@client.command(name="teste")
async def teste(context): # Criando função (def) teste
    await context.message.channel.send("Teste") #Enviar mensagem no mesmo canal do comando


@client.command(name='avatar')
async def ping(ctx):
    await ctx.message.channel.send(client.av)



client.run("MTAyMjI5MjA3NDY1OTMyODAyMQ.GFc_WA.07hUnpTF535JmNvLsELgcM4-cMTg7BcraxIJ0s") # Acionar bot.
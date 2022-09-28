from concurrent.futures import process
from unicodedata import name
import discord
from discord.ext import commands # Importando comandos da pasta discord.ext do pacote discord
from discord.flags import Intents
import asyncio
import dotenv
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("bot-token")
allIntents = discord.Intents.all() # Variavel para definir todas as intents
client = commands.Bot(command_prefix='*', intents=allIntents) #Usando intents= para declarar qual intent será usada. (No caso allIntents)


@client.event
async def on_ready():
    print("Olá, Mundo!")
    print("Tudo certo. Estou Online! :D")


############## COMANDOS

@client.command(name="teste")
async def teste(context): # Criando função (def) teste
    await context.message.channel.send("Testado :D") #Enviar mensagem no mesmo canal do comando


@client.command(name='ping')
async def ping(ctx):
    clientPing = client.latency * 1000
    roundPing = round(clientPing, 2)
    channel = client.get_channel(1022871420340019200)
    await channel.send(f'Olá {ctx.author.mention}, seu ping é de {roundPing}') # Concatenação com {}


client.run(token) # Acionar bot.    
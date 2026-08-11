import discord
import random
from discord.ext import commands
from senha import senha
from moeda import cara_coroa
intents = discord.Intents.default()
intents.message_content = True


# Criar um bot com comandos
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command
async def Oi(ctx):
    await ctx.send(f'Oiiii, {ctx.author.mention}!')
@bot.command
async def Senha(ctx):
    await ctx.send(f'Sua senha é: {senha()}')
@bot.command
async def Tchau(ctx):
    await ctx.send(f'Tchau {ctx.author.mention}! :D :wave:')
@bot.command
async def Ajuda(ctx):
    await ctx.send('Comandos disponíveis:\n$oi - O bot irá cumprimentar você.\n$senha - O bot irá gerar uma senha aleatória para você.\n$ajuda - O bot irá mostrar os comandos disponíveis.\n$tchau - O bot irá se despedir de você.\n$roll NdN - O bot irá rolar um dado no formato NdN (ex: 2d6).')
@bot.command()
async def meme(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)
@bot.command()
async def Moeda(ctx):
    await ctx.send(str(cara_coroa()))

bot.run("TOKEN AQUI")

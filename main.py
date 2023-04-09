import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='?', intents=discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + '!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send('Hello There!')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'Pong! ||{round(bot.latency * 1000)} ms||')

@bot.command(name='help')
async def help(ctx):
    em = discord.Embed(title='Help', description='See what all I could do for you!', color=000000)
    em.add_field(name='Commands', value='`?hello` to say hello to me!\n`?ping` to check my ping!\n`?help` to see this message!', inline=False)
    await ctx.send(embed=em)

token = os.environ['TOKEN']
bot.run('token goes here')

import discord
from discord.ext import commands
import json
import random

intents = discord.Intents.default()
intents.members = True

with open('setting.json','r',encoding='utf8') as jfile:
    xxxtan = json.load(jfile)

bot = commands.Bot(command_prefix='X', intents = intents)

@bot.event
async def on_ready():
    print(">> ✅ XXX up <<")

@bot.event
async def on_member_join(member):
      callable = bot.get_channel(805084597381234739)
      await callable.send(f'{member} join!')

@bot.event  
async def on_member_remove(member):
      callable = bot.get_channel(805089502065721364)
      await callable.send(f'{member} leave!')

@bot.command()
async def P(ctx):
    await ctx.send(f'Pussy')

@bot.command()
async def F(ctx):
    await ctx.send(f'fucking')

@bot.command()
async def W(ctx):
    await ctx.send(f'fucked up')

@bot.command()
async def ZZ(ctx):
    await ctx.send(f'修羅沒屌')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

 

@bot.command()
async def 圖片(ctx):
    pic = discord.File('E:\\QQQ\\pic\\A2.jpg')
    await ctx.send(file=pic)

@bot.command()
async def 圖(ctx):
    pic = discord.File('E:\\QQQ\\pic\\A1.jpg')
    await ctx.send(file=pic)

bot.run(xxxtan['TOKEN']) 
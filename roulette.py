import os
import random 

from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='roulette', help='Kicks a random user from the server.')
async def roulette(ctx):
    bot_member = ctx.guild.me
    guild_members = ctx.guild.members
    num_attempts = 0
    member_to_kick = bot_member
    
    while member_to_kick.roles[-1] >= bot_member.roles[-1] or member_to_kick == bot_member:
        if num_attempts > 3:
            break
        member_to_kick = random.choice(guild_members)
        num_attempts += 1
        await ctx.send("Kicking " + str(member_to_kick) + " from the server.")
    
    if num_attempts <= 3:
        await ctx.guild.kick(member_to_kick)

        await ctx.send("Kicked " + str(member_to_kick) + " from the server.")
    
    else: 
        await ctx.send("Could not find members to kick. Please check role hierarchy and make sure RouletteBot is below the Admin role. ")

bot.run(TOKEN)
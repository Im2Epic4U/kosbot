# https://discordapp.com/oauth2/authorize?client_id=582715814386466836&scope=bot&permissions=8

import discord
import json
import os
from discord.ext import commands, tasks
from discord import activity
from discord import state

client = commands.Bot(command_prefix = 'k?')
client.remove_command('help')
OwnerID = 379400007410909186

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name='our users'))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
        channel = discord.utils.get(member.guild.channels, name='⏐-main')
        embed = discord.Embed(description=f"Welcome, {member.mention} to **{member.guild}**!\n↳ Please read over: <#313223569968463893>\n↳Wanna get pinged for announcements? Events? Read over <#476229320067776512> <#546227771123302411>\n↳ Extras! We do <#566432150292004865> and <#553044501783117839>\n↳ Come chat with us once you're done!\n↳ You're the {len(list(member.guild.members))}th member!", colour=discord.Colour.orange())
        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.set_author(name=f'{member.guild.name}', icon_url=f'{member.guild.icon_url}')
        embed.set_image(url="https://i.imgur.com/HZ3jo0t.png")
        await channel.send(content=f'**TAG:** {member.mention}, <@&546833327710142504>', embed=embed)

# @tasks.loop(seconds=10)
# async def bumpreminder(ctx):
#     bump = discord.utils.get(ctx.guild.channels, name='⏐-bump')
#     await bump.send("It's that time again!\n\n<@&546833327815000098>, make sure you do !d bump, !disboard bump to bump our server!")
#     embed = discord.Embed(description="It's that time again!\n\n<@&546833327815000098>, make sure you do !d bump, !disboard bump to bump our server!", colour=discord.Colour.blue())
#     await channel.send(content=None, embed=embed)

# @client.command()
# async def bumptest(ctx):
#     if ctx.author.id == OwnerID:
#         channel = discord.utils.get(ctx.guild.channels, name='⏐-bump')
#         embed = discord.Embed(description="It's that time again!\n\n<@&546833327815000098>, make sure you do !d bump, !disboard bump to bump our server!", colour=discord.Colour.blue())
#         await channel.send(content=None, embed=embed)
#         e = discord.Embed(description=f"Successfully sent bump message, {ctx.author.mention}!", colour=discord.Colour.green())
#         await ctx.send(content=None, embed=e)
#     else:
#         e = discord.Embed(description=f"You don't have permission to execute this command, {ctx.author.mention}!", colour=discord.Colour.red())
#         await ctx.send(content=None, embed=e)

@client.command()
async def load(ctx, extension):
    if message.author.id == OwnerID:
        client.load_extension(f'cogs.{extension}')
        e = discord.Embed(description=f'Loaded {extension}, {ctx.author.mention}!', colour=discord.Colour.green())
        await message.channel.send(content=None, embed=e)
    else:
        e = discord.Embed(description=f"You don't have permission to execute this command, {ctx.author.mention}", colour=discord.Colour.red())
        await message.channel.send(content=None, embed=e)

@client.command()
async def unload(ctx, extension):
    if message.author.id == OwnerID:
        client.unload_extension(f'cogs.{extension}')
        e = discord.Embed(description=f'Unloaded {extension}, {ctx.author.mention}!', colour=discord.Colour.green())
        await message.channel.send(content=None, embed=e)
    else:
        e = discord.Embed(description=f"You don't have permission to execute this command, {ctx.author.mention}", colour=discord.Colour.red())
        await message.channel.send(content=None, embed=e)

@client.command()
async def reload(ctx, extension):
    if message.author.id == OwnerID:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')
        e = discord.Embed(description=f'Reloaded {extension}, {ctx.author.mention}!', colour=discord.Colour.green())
        await message.channel.send(content=None, embed=e)
    else:
        e = discord.Embed(description=f"You don't have permission to execute this command!, {ctx.author.mention}", colour=discord.Colour.red())
        await message.channel.send(content=None, embed=e)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))
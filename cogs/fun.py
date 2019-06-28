import discord
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = 'k?')

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def changegayness(self, ctx, *, arg):
        initialchange = discord.Embed(title=f"Changing gayness to: {arg}%.", colour=discord.Colour.blue())
        await ctx.send(content=None, embed=initialchange)
        global gaynessupdate
        gaynessupdate = f"{arg}"
        await asyncio.sleep(2)
        update = discord.Embed(title="Gayness set to: " + gaynessupdate + "%.", colour=discord.Colour.blue())
        await ctx.send(content=None, embed=update)

    @commands.command()
    async def gayness(self, ctx):
        global gaynessupdate
        embed = discord.Embed(title=gaynessupdate + "%", colour=discord.Colour.blue())
        await ctx.send(content=None, embed=embed)

def setup(client):
    client.add_cog(Fun(client))
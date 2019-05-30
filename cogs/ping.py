import discord
import time
import math
import datetime
from discord.ext import commands

client = commands.Bot(command_prefix = 'k?')

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title='🏓 Pong!', colour=discord.Colour.green())
        embed.add_field(name='Message Latency', value=f'{math.floor(self.client.latency * 1000)}ms', inline=True)
        embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(content=None, embed=embed)

def setup(client):
    client.add_cog(Ping(client))
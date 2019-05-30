import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'k?')
OwnerID = 379400007410909186
Nick = 269946726918389770

class Owner(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def logout(self, ctx):
        if ctx.message.author.id == OwnerID or Nick:
            await ctx.send(f':white_check_mark: Logging out.')
            await self.client.logout()
        else:
            await ctx.send(f"You don't have permission to execute this command!")

    @commands.command()
    async def say(self, ctx, *, arg, amount=1):
        if ctx.message.author.id == OwnerID or Nick:
            await ctx.channel.purge(limit=amount)
            e = discord.Embed(title=f'{arg}', colour=discord.Colour.green())
            await ctx.send(content=None, embed=e)
        else:
            e = discord.Embed(title=f"You don't have permission to use this command, {ctx.author.mention}!")
            await ctx.send(content=None, embed=e)


def setup(client):
    client.add_cog(Owner(client))
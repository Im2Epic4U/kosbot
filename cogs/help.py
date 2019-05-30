import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'k?')

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='**__KosBot Commands__**', description=None, colour=discord.Colour.green())
        embed.add_field(name='**Moderation**', value='**k?ban** - Bans the specified user.\n**k?unban** - Unbans the specified user.\n**k?kick** - Kicks the specified user.\n**k?clear** - You can purge messages with the bot. You must add 1 to the amount of messages you want to remove.\nYou **must** have the <@&437074557099048970> role to use these commands.', inline=True)
        embed.add_field(name='\n*Debug*', value="**k?ping** - Shows the bot's ping and a fun little message." , inline=True)
        embed.add_field(name='\n__Features__', value='**Welcomer** - This welcomes people to the server and is one of the features this bot has. There may be more in the future, so keep an eye out for those!', inline=True)
        embed.add_field(name="Contact real epic#0001 if you find a bug within one of this bot's commands.")
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/582715814386466836/99249f9e7dbcaa7348f42999bb84218c.png')
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.set_image(url='https://images-ext-1.discordapp.net/external/qcqjVkeH-i0OiaKKy0ngzvXZ7Qd9kEBA6f6m4-ZZZOQ/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/379400007410909186/a_264e49cb370914994eda22c49ed2aa96.gif')
        await ctx.send(content=f'{ctx.author.mention}', embed=embed)

def setup(client):
    client.add_cog(Help(client))
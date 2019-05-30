import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'k?')
Staff = 437074557099048970

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        if Staff in [role.id for role in ctx.author.roles]:
            await member.kick(reason=reason)
            embed = discord.Embed(description=f'Kicked **{member.mention}** for **{reason}**', colour=discord.Colour.green())
            await ctx.send(content=None, embed=embed)
        else:
            embed = discord.Embed(description=f"You don't have permission to execute this command, {ctx.author.mention}!")
            await ctx.send(content=None, embed=embed)
            

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if Staff in [role.id for role in ctx.author.roles]:
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    embed = discord.Embed(description=f'Unbanned **{user.mention}**', colour=discord.Colour.green())
                    await ctx.send(content=None, embed=embed)
                    return
            else:
                embed = discord.Embed(description=f"You don't have permission to execute this command, {ctx.author.mention}!", colour=discord.Colour.red())
                await ctx.send(content=None, embed=embed)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if Staff in [role.id for role in ctx.author.roles]:
            await member.ban(reason=reason)
            embed = discord.Embed(description=f'Banned {member.mention} for **{reason}**', colour=discord.Colour.green())
            await ctx.send(content=None, embed=embed)
        else:
            embed = discord.Embed(description=f"You don't have permission to execute this command, {ctx.author.mention}!", colour=discord.Colour.red())
            await ctx.send(content=None, embed=embed)

    @commands.command()
    async def clear(self, ctx, amount=11):
        if Staff in [role.id for role in ctx.author.roles]:
            await ctx.channel.purge(limit=amount)
            embed = discord.Embed(description=f'Cleared **{amount}** messages.', colour=discord.Colour.green())
            await ctx.send(content=None, embed=embed)
            await ctx.channel.purge(limit=1)
        else:
            embed = discord.Embed(description=f"You don't have permission to execute this command, {ctx.author.mention}!", colour=discord.Colour.red())
            await ctx.send(content=None, embed=embed)

def setup(client):
    client.add_cog(Moderation(client))
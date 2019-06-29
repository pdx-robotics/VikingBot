import discord
from discord.ext import commands

class general(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.description = ''

    # ping
    @commands.command(
        usage = '',
        help  = '',
        brief = ''
    )
    async def ping(self,ctx):
        await ctx.send(f':ping_pong: {ctx.message.author.mention} pong! =D')
    
    # about
    @commands.command(
        usage = '',
        help  = '',
        brief = ''
    )
    async def about(self,ctx):

    
    # info
    @commands.command(
        usage = '',
        help  = '',
        brief = ''
    )
    async def info(self,ctx):

    
    # membercount
    @commands.command(
        usage = '',
        help  = '',
        brief = ''
    )
    async def membercount(self,ctx):
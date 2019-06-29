import discord 
from discord.ext import commands

class test_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(usage="test")
    async def ping2(self,ctx):
        """Format: $ping2 | Pings the bot | Testing"""
        msg = f'{ctx.message.author.mention} pong!'
        await ctx.send(msg)
    
    @commands.command(
        help = "Increments integer passed in by user.",
        brief = "Increments integer.",
        usage = "[integer]",
    )
    async def increment(self, ctx, num):
        await ctx.send(int(num)+1)

    @increment.error
    async def increment_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
            ctx.send('Missing required argument [integer]')
        elif isinstance(error,commands.TooManyArguments):
            ctx.send('Too many arguments')
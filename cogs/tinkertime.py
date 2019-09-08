import os,sys
dir_main = os.path.dirname(os.path.realpath(__file__))
dir_include = os.path.join(dir_main,'include')
sys.path.insert(dir_include)

import discord
from discord.ext import commands
import vrs_ids
import vrs_utils as utils

class meetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands for managing Tinkering Session times and polling.'

    # linkupdate
    #@self.bot.checkAdmin()
    @commands.command(
        usage = '[term] [year] [link]',
        help  = 'Updates Availability Poll link.  Provide year and '\
                'school term the poll is meant for.  Link must start'\
                ' with \"http://\" for hyperlink to work.',
        brief = 'Updates link to Availability Poll.'
    ) 
    async def linkupdate(self, ctx, term, year, new_link):
        utils.update_poll_link(term, year, new_link)
        await ctx.send(ctx.message.author, f'Updated link for Availability Poll for {term} {year} to {new_link}')
    
    #addtinker
    @commands.command(
        usage = '[weekday] [start_time] [end_time]',
        brief = 'Adds time for planned weekly Tinkering Sessions.',
        help  = 'Adds time for planned weekly Tinkering Sessions.'\
                '  Start and end times need to be 24 hour time formatted \'XX:XX\''
    )
    async def addtinker(self, ctx, day, startTime, endTime):
        if(utils.valid_day(day) == True):
            utils.remove_tinker_time(day, startTime, endTime)
            await ctx.send(f'Tinkering session time added: {day} from {startTime} to {endTime}')
    
    # removetinker
    @commands.command(
        usage = '[weekday] [start_time] [end_time]',
        brief = 'Removes time that\'s listed for weekly Tinkering Sessions.',
        help  = 'Removes time that\'s listed for weekly Tinkering Sessions.'\
                '  Start and end times need to be 24 hour time formatted \'XX:XX\''
    )
    async def removetinker(self, ctx, day, startTime, endTime):

    
    # change term
    @commands.command(
        usage = '[term] [year]',
        brief = 'Update term and year for planned meetings.',
        help  = 'Update term and year for planned meetings. '
    )
    async def updateterm(self,ctx,term,year):

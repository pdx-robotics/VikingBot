import os,sys
dir_main = os.path.dirname(os.path.realpath(__file__))


import discord
from discord.ext import commands
import vrs_ids

class management(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = 'Commands for managing Tinkering Session times and polling.'

    # linkupdate

    @commands.command(
        usage = '[term] [year] [link]',
        help  = 'Updates Availability Poll link.  Provide year and '\
                'school term the poll is meant for.  Link must start'\
                ' with \"http://\" for hyperlink to work.',
        brief = 'Updates link to Availability Poll.'
    ) 
    async def linkupdate(self, ctx, term, year, new_link):
        
    
    #addtinker
    @commands.command(
        usage = '[weekday] [start_time] [end_time]',
        help  = 'Adds time for planned weekly Tinkering Sessions.',
        brief = 'Adds time for planned weekly Tinkering Sessions.'\
                '  Start and end times need to be 24 hour time formatted \'XX:XX\''
    )
    async def addtinker(self, ctx, day, startTime, endTime):

    
    # removetinker
    @commands.command(
        usage = '[weekday] [start_time] [end_time]',
        help  = 'Removes time that\'s listed for weekly Tinkering Sessions.',
        brief = 'Removes time that\'s listed for weekly Tinkering Sessions.'\
                '  Start and end times need to be 24 hour time formatted \'XX:XX\''
    )
    async def removetinker(self, ctx, day, startTime, endTime):

    
    # change term
    @commands.command(
        usage = '',
        help  = '',
        brief = ''
    )
    async def updateterm(self,ctx,term,year):

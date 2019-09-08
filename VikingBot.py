# Title: VikingBot.py
# Author: Aaron Chan (Chana030102) & Dustin Schnelle (schnelled)
# Date: 1/24/2019
# Note: this is the test version of the VikingBot (VikingBot.py)
#
# Viking Robotics Society - Discord Chatbot
# This Discord Chatbot was created to support the Viking Robotics Society (VRS)
# ==============================================================================
# Events:
#           -> on_ready():  discord event for when the bot is ready to assist the
#                           server.
#           -> on_member_join(member): discord event for greeting people when
#                           they join the server.
#
# General Commands:
#           -> ping(ctx):   discord command for testing purposes.
#           -> help(ctx):   discord command to display all of the support commands.
#           -> about(ctx):  discord command to display information about the
#                           discord bot.
#           -> info(ctx):   discord command to display general information about
#                           the Vikings Robotic Society (VRS).
#
# Admin Commands:
#           -> linkupdate(ctx, term, year, new_link): discord command for admin
#                           usage to update the availability poll link on discord.
#           -> addtinkertime(ctx, day, start, end): add tinkering time to
#                           tinker_times.txt file.
#           -> removetinkertime(ctx, day, start, end): remove tinkering time from
#                           tinker_times.txt file.
#           -> membercount(ctx): obtain the member count for the following roles
#                           (Member, Admin, Aquanautics, Terranuatics, Aeronuatics,
#                           Lab Access)
#
#===============================================================================

import discord, sys, os, inspect, requests
from discord.ext import commands

dir_main = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
dir_include = os.path.join(dir_main,'Include') 
sys.path.insert(0,dir_include)
import vrs_utils as utils
import vrs_ids
import vrs_text 
import vrs_help

url = "https://robotics.ece.pdx.edu/api/announcements.php"
data = vrs_ids.data

#===============================================================================
# Initial setup of the Discord chat bot
#===============================================================================

# Check for mode argument
if len(sys.argv) != 2:
    # Display usage error
    print("Usage Error: python3.6 VikingBot.py -mode")
    # Exit the program
    sys.exit(0)

# Check if the Discord bot is in 'test' mode
if sys.argv[1] == '-t':
    # Initialize bot token for test server
    token = vrs_ids.TOKEN_TESTBOT
    # Initialize role ids for the test server
    admin_id = vrs_ids.ID_ADMIN_TEST
    member_id = vrs_ids.ID_MEMBER_TEST
    aqua_id = vrs_ids.ID_AQUA_TEST
    terra_id = vrs_ids.ID_TERRA_TEST
    aero_id = vrs_ids.ID_AERO_TEST
    lab_id = vrs_ids.ID_LAB_ACCESS_TEST
    # Initialize the used channel ids for the test server
    general_info_id = vrs_ids.ID_TEXT_GENERAL_INFO_TEST
    lobby_id = vrs_ids.ID_TEXT_LOBBY_TEST
    announce_id = vrs_ids.ID_TEXT_ANNOUNCEMENTS_TEST
# Check if the Discord bot is in 'run' mode
elif sys.argv[1] == '-r':
    # Initialize bot token for assisting Viking Robotics Society server
    token = vrs_ids.TOKEN_VIKINGBOT
    # Initialize role ids for the Viking Robotics Society server
    admin_id = vrs_ids.ID_ADMIN
    member_id = vrs_ids.ID_MEMBER
    aqua_id = vrs_ids.ID_AQUA
    terra_id = vrs_ids.ID_TERRA
    aero_id = vrs_ids.ID_AERO
    lab_id = vrs_ids.ID_LAB_ACCESS
    # Initialize the used channel ids for the Viking Robotics Society server
    general_info_id = vrs_ids.ID_TEXT_GENERAL_INFO
    lobby_id = vrs_ids.ID_TEXT_LOBBY
    announce_id = vrs_ids.ID_TEXT_ANNOUNCEMENTS
# Otherwise invalid argument provided
else:
    # Display usage error
    print("Usage Error: invalid mode\n\t-t (test mode)\n\t-r (run mode)")
    sys.exit(0)

# Setup the logging of errors and print statements to log file
utils.setup()
vrs_help.help_setup(dir_main)
# Create an instance of a discord bot
bot = commands.Bot(command_prefix=vrs_ids.BOT_PREFIX)
# Remove defualt help command
bot.remove_command('help')

# VikingBot startup message
print("\n------\n")
print(vrs_text.ASCII_ART)
print("\n------\n")
print("\nDiscord version: {}".format(discord.__version__))
print("\n------\n")

#===============================================================================
# General events
#
# Format of events:
#   @bot.event
#   async def <function>():
#
# List of events:
#           -> on_ready(): discord event for when the bot is ready to assist the
#                          server.
#           -> on_member_join(member): discord event for greeting people when
#                          they join the server.
#
#===============================================================================

# Register a discord event
@bot.event
# Discord bot is ready for server
## Called when the client is done preparing the data received from Discord
async def on_ready():
    # Display bot's login information
    print("Let's build some robots!")
    print("I am running on " + bot.user.name)
    print("With the ID: " + bot.user.id)
    print("\n------\n")

# Register a discord event
@bot.event
# Greet people when they join the server
async def on_member_join(member):
    # Display information about a new member joining the server
    print("\n{} joined the server!".format(member.name))
    print("First time they joined this server was: {}".format(member.joined_at))

    # Obtain the general_info and lobby channel ids for greeting message
    general_info = bot.get_channel(general_info_id)
    lobby = bot.get_channel(lobby_id)

    # Send the greeting message for "new join" to the lobby channel
    await bot.send_message(lobby, vrs_text.welcome_text.format(member.mention, general_info.mention))

@bot.event
async def on_command_error(ctx,error):
    print(f'Error var: {error}')
    print(f'ctx var: {ctx}')
    await reply(error,f'{ctx}. See $help for a list of commands')
#===============================================================================
# General Commands - anyone can use these commands
#
# Format of Commands:
#   @bot.command(pass_context=True)
#   async def <command_name> (ctx, param, *args):
#
# List of Commands:
#           -> ping(ctx):   discord command for testing purposes.
#           -> help(ctx):   discord command to display all of the support commands.
#           -> about(ctx):  discord command to display information about the
#                           discord bot.
#           -> info(ctx):   discord command to display general information about
#                           the Vikings Robotic Society (VRS).
#
#===============================================================================

# Ping command (for testing)
@bot.command(pass_context=True)
async def ping(ctx):
    # Send back the pong message to the channel
    #await bot.say(":ping_pong: {} pong! =D".format(ctx.message.author.mention))
    await reply(ctx,f':ping_pong: {ctx.message.author.mention} pong! =D')

# Display all of the supported commands
@bot.command(pass_context=True)
async def help(ctx, command = None):
    result = vrs_help.get_help(command=command)
    if result[0] == 0:
        await reply(ctx,result[1])
    elif result[0] == 1:
        await reply(ctx,embed=result[1])
       
# Information about the bot itself
@bot.command(pass_context=True)
async def about(ctx):
    # Sends information about the bot to the channel
    await bot.send_message(ctx.message.channel, utils.about())

# Provide information about the society
@bot.command(pass_context=True)
async def info(ctx):
    # Get the general information
    gen_info = utils.gen_info()
    # Get the meeting information
    meetings = utils.meet_info()
    # Send the general and meeting information
    await bot.send_message(ctx.message.channel, embed=gen_info)
    await bot.send_message(ctx.message.channel, embed=meetings)

#===============================================================================
# Admin Commands - admins can use these commands
#
# Format of Admin Commands:
#   @bot.command(pass_context=True)
#   async def <command_name> (ctx, param, *args):
#       if vrs_id.ADMIN_ID in [x.id for x in ctx.message.author.roles]:
#           Do admin command
#       else:
#           Send non-admin denied message for the command
#
# List of Admin Commands:
#           -> linkupdate(ctx, term, year, new_link): discord command for admin
#                           usage to update the availability poll link on discord.
#           -> addtinkertime(ctx, day, start, end): add tinkering time to
#                           tinker_times.txt file.
#           -> removetinkertime(ctx, day, start, end): remove tinkering time from
#                           tinker_times.txt file.
#           -> membercount(ctx): obtain the member count for the following roles
#                           (Member, Admin, Aquanautics, Terranuatics, Aeronuatics,
#                           Lab Access)
#===============================================================================

# Make an announcement
@bot.command(pass_context=True)
async def announce(ctx, *, content:str):
    print(content)
    # Check role of the member for admin permissions
    if admin_id in [x.id for x in ctx.message.author.roles]:
        channel = bot.get_channel(announce_id)
        data['data'] = content
        requests.post(url,data)
        await bot.send_message(channel, "@everyone\n"+content)
    else:
        await bot.reply("You can't perform this command.  Admin permission needed.")


# Update Availability poll link
@bot.command(pass_context=True)
async def linkupdate(ctx, term, year, new_link):
    # Check role of the member for admin permissions
    if admin_id in [x.id for x in ctx.message.author.roles]:
        # Update Availability poll link
        utils.update_poll_link(term, year, new_link)
        # Send message to admin member about update success
        await bot.send_message(ctx.message.author, "You updated the availability poll link to {} {} --> {}".format(term, year, new_link))
    # Otherwise member is not an admin
    else:
        # Send permission denied message to non-admin member
        await bot.send_message(ctx.message.author, "You can't preform this command. Admin permission needed.")

    # Remove the old general information and replace with the newer one using new poll link
    # Create an empty character array (string)
    msgs = []
    # Obtain the general information channel id
    general_info = bot.get_channel(general_info_id)

    # Check if the channel id was obtained
    if general_info == None:
        # Display message that the channel couldn't be found
        print("Couldn't find channel with ID {}".format(general_info_id))
    else:
        # Obtain the old message to be deleted
        async for y in bot.logs_from(general_info, limit=2):
            # Append the current word to the message
            msgs.append(y)
        # Delete the old message
        await bot.delete_messages(msgs)

        # Get the general information
        gen_info = utils.gen_info()
        # Get the meeting information
        meetings = utils.meet_info()
        # Send the general and meeting information
        await bot.send_message(general_info, embed=gen_info)
        await bot.send_message(general_info, embed=meetings)

# Add tinker time (tinker_time.txt)
@bot.command(pass_context=True)
async def addtinkertime(ctx, day, startTime, endTime):
    # Check role of the member for admin permissions
    if admin_id in [x.id for x in ctx.message.author.roles]:
        # Check for valid day of the week
        if(utils.valid_day(day) == True):
            # Add the tinkering session to the text file
            utils.add_tinker_time(day, startTime, endTime)
            # Send message to admin member about the successfully added tinker time
            await bot.send_message(ctx.message.author, "You added a tinker time on {} from {} to {}".format(day, utils.setup_time(startTime), utils.setup_time(endTime)))
        # Otherwise invalid day was provided
        else:
            # Send message to admin member that the day for the tinker time is not valid
            await bot.send_message(ctx.message.author, "Error: Invalid day provided, please check your spelling")
    # Otherwise member is not an admin
    else:
        # Send permission denied message to non-admin member
        await bot.send_message(ctx.message.author, "You can't preform this command. Admin permission needed.")

# Remove tinker time (tinker_time.txt)
@bot.command(pass_context=True)
async def removetinkertime(ctx, day, startTime, endTime):
    # Check role of the member for admin permissions
    if admin_id in [x.id for x in ctx.message.author.roles]:
        # Check for valid day of the week
        if(utils.valid_day(day) == True):
            # Add the tinkering session to the text file
            utils.remove_tinker_time(day, startTime, endTime)
            # Send message to admin member about the successfully removed tinker time
            await bot.send_message(ctx.message.author, "You removed the tinker time on {} from {} to {}".format(day, utils.setup_time(startTime), utils.setup_time(endTime)))
        # Otherwise invalid day was provided
        else:
            # Send message to admin member that the day for the tinker time is not valid
            await bot.send_message(ctx.message.author, "Error: Invalid day provided, please check your spelling.")
    # Otherwise member is not an admin
    else:
        # Send permission denied message to non-admin member
        await bot.send_message(ctx.message.author, "You can't preform this command. Admin permission needed.")

# Obtain the number of members in the server
@bot.command(pass_context=True)
async def membercount(ctx):
    # Check role of the member for admin permissions
    if admin_id in [x.id for x in ctx.message.author.roles]:
        # Declare roles dictionary
        roles = {"Members" : 0,
                 "Admins" : 0,
                 "Lab Access" : 0,
                 "Aquanautics" : 0,
                 "Terranuatics" : 0,
                 "Aeronautics" : 0}
        # Obtain the server
        server = ctx.message.server

        # Loop through all of the people in the server
        for member in server.members:
            # Check if the current person is a member of VRS
            if member_id in [y.id for y in member.roles]:
                roles["Members"] += 1
            # Check if the current person is an Admin of VRS
            if admin_id in [y.id for y in member.roles]:
                roles["Admins"] += 1
            # Check if the current person has lab access
            if lab_id in [y.id for y in member.roles]:
                roles["Lab Access"] += 1
            # Check if the current person is part of the Aquanautics team
            if aqua_id in [y.id for y in member.roles]:
                roles["Aquanautics"] += 1
            # Check if the current person is part of the Terranuatics team
            if terra_id in [y.id for y in member.roles]:
                roles["Terranuatics"] += 1
            # Check if the current person is a part of the Aeronautics team
            if aero_id in [y.id for y in member.roles]:
                roles["Aeronautics"] += 1
            # Check if the current person has lab access

        # Format the role count information
        roleInfo = utils.role_count(roles)

        await bot.send_message(ctx.message.channel, embed=roleInfo)
    # Otherwise member is not an admin
    else:
        # Send permission denied message to non-admin member
        await bot.send_message(ctx.message.author, "You can't preform this command. Admin permission needed.")

async def reply(ctx,msg=None,embed=None):
    if ctx.message.channel:
        if not embed:
            await bot.send_message(ctx.message.channel,msg)
        else:
            await bot.send_message(ctx.message.channel,embed=embed)
    else:
        if not embed:
            await bot.send_message(ctx.message.author,msg)
        else:
            await bot.send_message(ctx.message.author,embed=embed)

# Run the discord client
bot.run(token)
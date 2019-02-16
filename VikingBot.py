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
#
#===============================================================================

import discord, sys
from discord.ext import commands

import vrs_utils
import vrs_ids
import vrs_text

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
    # Initialize admin id for the test server
    admin_id = vrs_ids.ID_ADMIN_TEST
    # Initialize the used channel ids for the test server
    general_info_id = vrs_ids.ID_TEXT_GENERAL_INFO_TEST
    lobby_id = vrs_ids.ID_TEXT_LOBBY_TEST
# Check if the Discord bot is in 'run' mode
elif sys.argv[1] == '-r':
    # Initialize bot token for assisting Viking Robotics Society server
    token = vrs_ids.TOKEN_VIKINGBOT
    # Initialize admin id for the Viking Robotics Society server
    admin_id = vrs_ids.ID_ADMIN
    # Initialize the used channel ids for the Viking Robotics Society server
    general_info_id = vrs_ids.ID_TEXT_GENERAL_INFO
    lobby_id = vrs_ids.ID_TEXT_LOBBY
# Otherwise invalid argument provided
else:
    # Display usage error
    print("Usage Error: invalid mode\n\t-t (test mode)\n\t-r (run mode)")
    sys.exit(0)

# Setup the logging of errors and print statements to log file
vrs_utils.setup()
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
    await bot.say(":ping_pong: {} pong! =D".format(ctx.message.author.mention))

# Display all of the supported commands
@bot.command(pass_context=True)
async def help(ctx):
    # Check for admin member(role)
    if admin_id in [x.id for x in ctx.message.author.roles]:
        # Sends a list of all commands supported to the channel
        await bot.send_message(ctx.message.channel, vrs_utils.help(True))
    # Otherwise not admin member(role)
    else:
        # Send a list of basic commands supported to the channel
        await bot.send_message(ctx.message.channel, vrs_utils.help(False))

# Information about the bot itself
@bot.command(pass_context=True)
async def about(ctx):
    # Sends information about the bot to the channel
    await bot.send_message(ctx.message.channel, vrs_utils.about())

# Provide information about the society
@bot.command(pass_context=True)
async def info(ctx):
    # Get the general information
    gen_info = vrs_utils.gen_info()
    # Get the meeting information
    meetings = vrs_utils.meet_info()
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
#===============================================================================

# Update Availability poll link
@bot.command(pass_context=True)
async def linkupdate(ctx, term, year, new_link):
    # Check role of the member for admin permissions
    if admin_id in [x.id for x in ctx.message.author.roles]:
        # Update Availability poll link
        vrs_utils.update_poll_link(term, year, new_link)
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
        gen_info = vrs_utils.gen_info()
        # Get the meeting information
        meetings = vrs_utils.meet_info()
        # Send the general and meeting information
        await bot.send_message(general_info, embed=gen_info)
        await bot.send_message(general_info, embed=meetings)

# Add tinker time (tinker_time.txt)
@bot.command(pass_context=True)
async def addtinkertime(ctx, day, startTime, endTime):
    # Check role of the member for admin permissions
    if admin_id in [x.id for x in ctx.message.author.roles]:
        # Check for valid day of the week
        if(vrs_utils.valid_day(day) == True):
            # Add the tinkering session to the text file
            vrs_utils.add_tinker_time(day, startTime, endTime)
            # Send message to admin member about the successfully added tinker time
            await bot.send_message(ctx.message.author, "You added a tinker time on {} from {} to {}".format(day, vrs_utils.setup_time(startTime), vrs_utils.setup_time(endTime)))
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
        if(vrs_utils.valid_day(day) == True):
            # Add the tinkering session to the text file
            vrs_utils.remove_tinker_time(day, startTime, endTime)
            # Send message to admin member about the successfully removed tinker time
            await bot.send_message(ctx.message.author, "You removed the tinker time on {} from {} to {}".format(day, vrs_utils.setup_time(startTime), vrs_utils.setup_time(endTime)))
        # Otherwise invalid day was provided
        else:
            # Send message to admin member that the day for the tinker time is not valid
            await bot.send_message(ctx.message.author, "Error: Invalid day provided, please check your spelling.")
    # Otherwise member is not an admin
    else:
        # Send permission denied message to non-admin member
        await bot.send_message(ctx.message.author, "You can't preform this command. Admin permission needed.")

# Run the discord client
bot.run(token)

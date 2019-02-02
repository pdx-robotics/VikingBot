# Title: vrs_utils.py
# Author: Aaron Chan (Chana030102) & Dustin Schnelle (schnelled)
# Date: 1/24/2019
#
# Utilities for the Viking Robotics Society (VRS) discord bot
# ==============================================================================
# Functions:
#           -> setup(): Setup standard output and standard error messages to
#                       print to a log file.
#           -> help():  Creates command descriptions for the test bot.
#           -> about(): Display information about the discord bot.
#           -> gen_info(): Create a discord embed class to display the general
#                       information about the Vikings Robotics Society.
#           -> meet_info(): Create a discord embed class to display the meeting
#                       information about the Viking Robotics Society.
#           -> get_poll_link(): Returns with the information about the terms
#                       availability poll.
#           -> update_poll_link(name, new_link): Update the poll link information
#                       in the poll_link text file.
#           -> add_tinker_time(day, starttime, endtime): Adds a tinker time to
#                       the tinker_time text file.
#           -> n_to_day(n): Converts a number representing the day of the week
#                       into the string representation.
#           -> day_to_n(day): Converts a day of the week (string) to a number
#                       representing the day.
#           -> valid_day(day): Checks the validity of the day of the week.
#           -> setuptime(time): Formats the time for the tinker time file
#                       (tinker_times.txt).
# Classes:
#           -> StreamToLogger(object): Class to log messages from standard
#                       output and standard error.
#
#===============================================================================


import os, sys, datetime, logging
import discord

import vrs_text
sys.path.insert(0, './Include/')
import vrs_classes

# Obtain the current directory path
dir_path = os.path.dirname(os.path.realpath(__file__))
# Directory for the log path
log_path = dir_path + "/log/"
# Directory for the availability poll link
link_poll = dir_path + "/Text/poll_link.txt"
# Directory for the tinkering session times
tinkerfile = dir_path + "/Text/tinker_times.txt"

#-------------------------------------------------------------------------------
# Function:     setup
# Input:        none
# Output:       none
# Decription:   Setup standard output and standard error messages to print to a
#               log file.
#-------------------------------------------------------------------------------
def setup():
    # Check if the log directory doen't exists
    if not os.path.exists(log_path):
        # Create the log directory
        os.makedirs(log_path)

    # Configure the basic logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(name)s:%(message)s',
        filename=log_path + datetime.datetime.now().strftime("discordlog-%Y%m%d-%H%M.log"),
        filemode='a'
    )

    # Write standard output to the log file
    sl = StreamToLogger(logging.getLogger('STDOUT'), logging.INFO)
    sys.stdout = sl

    # Write standard error to the log file
    sl = StreamToLogger(logging.getLogger('STDERR'), logging.ERROR)
    sys.stderr = sl

#-------------------------------------------------------------------------------
# Function:     help
# Input:        none
# Output:       text - the text output for the help command
# Decription:   Creates command descriptions for the test bot.
#-------------------------------------------------------------------------------
def help():
    # Create the text message for command descriptions
    text = vrs_text.code_mark
    text = text + vrs_text.commands_header
    text = text + vrs_text.help_text
    text = text + vrs_text.commands_admin
    text = text + vrs_text.code_mark
    return text

#-------------------------------------------------------------------------------
# Function:     about
# Input:        none
# Output:       text - information about the discord bot
# Description:  Display information about the discord bot.
#-------------------------------------------------------------------------------
def about():
    # Create bot information text
    text = vrs_text.about.format(vrs_text.bot_version)
    return text

#-------------------------------------------------------------------------------
# Function:     gen_info (general information)
# Input:        none
# Output:       embed - Emmbedded information about general information
# Description:  Create a discord embed class to display the general information
#               about the Vikings Robotics Society.
#-------------------------------------------------------------------------------
def gen_info():
    # Create embed discord object for general information
    embed = discord.Embed(title="__|---     VRS General Information     ---|__", description=vrs_text.description, color=0x229954)
    embed.set_footer(text=vrs_text.footer)
    embed.add_field(name="What We Do", value=vrs_text.description2, inline=True)
    embed.add_field(name="Contact", value="Email: "+vrs_text.email, inline=True)
    embed.add_field(name="Website", value=vrs_text.website, inline=True)
    data = get_poll_link()
    embed.add_field(name="Join Us Formally", value=vrs_text.join.format(data[0],data[1]), inline=True)
    embed.add_field(name="Other Resources", value=vrs_text.resources+"\n", inline=True)

    # Return the embedded object
    return embed

#-------------------------------------------------------------------------------
# Function:     meet_info (meeting information)
# Input:        none
# Output:       embed - Emmbedded information about meeting information
# Description:  Create a discord embed class to display the meeting information
#               about the Viking Robotics Society.
#-------------------------------------------------------------------------------
def meet_info():
    # Declare varable for tinkertimes
    tinkertimes = ""

    # Create embed discord object for general information
    embed = discord.Embed(title="__|---     Meetings     ---|__", description=vrs_text.meet_desc, color=0x229954)
    embed.set_footer(text=vrs_text.footer)
    embed.add_field(name="Monthly General Meeings", value=vrs_text.gen_meet_info, inline=True)

    # Loop to obtain information about the current tinkering sessions available
    for x in sessions.sessions:
        # Add current tinker time information
        tinkertimes += "{} form {} to {}\n".format(n_to_day(x.weekday), x.starttime, x.endtime)
    # Add the last time updated information
    tinkertimes += "\n*Last Updated: {}*".format(sessions.lastupdated)
    # Embed the tinker time information for the current term
    embed.add_field(name="{} Weekly Tinker Sessions".format(sessions.term), value=tinkertimes, inline=False)

    # Return the embedded object
    return embed

#-------------------------------------------------------------------------------
# Function:     get_poll_link
# Input:        none
# Output:       data - the link for the poll
# Decription:   Returns with the information about the terms availability poll.
#-------------------------------------------------------------------------------
def get_poll_link():
    # Open the poll_link text file for reading
    with open(link_poll, 'r') as f:
        # Read the data from the file
        read_data = f.read()
    # Close the file
    f.close()

    # Split and return the data
    data = read_data.split("\n")
    return data

#-------------------------------------------------------------------------------
# Function:     update_poll_link
# Input:        name - Name of the current term <Term> <Year>
#               new_link - URL link of the new poll
# Output:       none
# Definition:   Update the poll link information in the poll_link text file.
#-------------------------------------------------------------------------------
def update_poll_link(term, year, new_link):
    # Open the poll_link text file for writing
    with open(link_poll, 'w') as f:
        # Write the new poll information to the file
        f.write("{} {}\n{}".format(term, year, new_link))
    # Close the file
    f.close()

    # Display information about the updated poll link
    print("Poll link has been updated to {} {} --> {}.".format(term, year, new_link))

#-------------------------------------------------------------------------------
# Function:     add_tinker_time
# Input:        day - String representing the day of the week
#               starttime - Starting time of the tinker session (Military time)
#               endtime - End time of the tinker session (Military time)
# Output:       None
# Definition:   Adds a tinker time to the tinker_time text file.
#-------------------------------------------------------------------------------
def add_tinker_time(day, starttime, endtime):
    # Add the tinkering session to the events class
    sessions.add(day_to_n(day), setuptime(starttime), setuptime(endtime))

#-------------------------------------------------------------------------------
# Function:     n_to_day
# Input:        n - the number representing the day of the week
# Output:       (String) - day of the week
# Definition:   Converts a number representing the day of the week into the
#               string representation.
#-------------------------------------------------------------------------------
def n_to_day(n):
    # Check the which day of the week the number represents
    # 0 = Sunday
    if n == '0':
        return "Sunday"
    # 1 = Monday
    elif n == '1':
        return "Monday"
    # 2 = Tuesday
    elif n == '2':
        return "Tuesday"
    # 3 = Wednesday
    elif n == '3':
        return "Wednesday"
    # 4 = Thursday
    elif n == '4':
        return "Thursday"
    # 5 = Friday
    elif n == '5':
        return "Friday"
    # 6 = Saturday
    else:
        return "Saturday"

#-------------------------------------------------------------------------------
# Function:     day_to_n
# Input:        day - String of the day of the week
# Output:       n - The number representation of the day
# Definition:   Converts a day of the week (string) to a number representing the
#               day.
#-------------------------------------------------------------------------------
def day_to_n(day):
    # Convert the string to a number
    # Sunday = 0
    if day == "Sunday" or day == "sunday":
        return '0'
    # Monday = 1
    elif day == "Monday" or day == "monday":
        return '1'
    # Tuesday = 2
    elif day == "Tuesday" or day == "tuesday":
        return '2'
    # Wednesday = 3
    elif day == "Wednesday" or day == "wednesday":
        return '3'
    # Thursday = 4
    elif day == "Thursday" or day == "thursday":
        return '4'
    # Friday = 5
    elif day == "Friday" or day == "friday":
        return '5'
    # Saturday = 6
    else:
        return '6'

#-------------------------------------------------------------------------------
# Function:     valid_day
# Input:        day - String representing the day of the week
# Output:       Boolean value for whether the day is valid
# Definition:   Checks the validity of the day of the week.
#-------------------------------------------------------------------------------
def valid_day(day):
    # Check if the day of the week is valid
    # Sunday is valid
    if day == "Sunday" or day == "sunday":
        return True
    # Monday is valid
    elif day == "Monday" or day == "monday":
        return True
    # Tuesday is valid
    elif day == "Tuesday" or day == "tuesday":
        return True
    # Wednesday is valid
    elif day == "Wednesday" or day == "wednesday":
        return True
    # Thursday is valid
    elif day == "Thursday" or day == "thursday":
        return True
    # Friday is valid
    elif day == "Friday" or day == "friday":
        return True
    # Saturday is valid
    elif day == "Saturday" or day == "saturday":
        return True
    # Not valid day of the week
    else:
        return False

#-------------------------------------------------------------------------------
# Function:     setuptime
# Input:        -> time - Time to format for tinker time file
# Output:       Formated time
# Definition:   Formats the time for the tinker time file (tinker_times.txt)
#-------------------------------------------------------------------------------
def setuptime(time):
    # Format the time
    # 1am (1:00)
    if time == "1" or time == "01" or time == "1am":
        return "01:00"
    # 2am (2:00)
    elif time == "2" or time == "02" or time == "2am":
        return "02:00"
    # 3am (3:00)
    elif time == "3" or time == "03" or time == "3am":
        return "03:00"
    # 4am (4:00)
    elif time == "4" or time == "04" or time == "4am":
        return "04:00"
    # 5am (5:00)
    elif time == "5" or time == "05" or time == "5am":
        return "05:00"
    # 6am (6:00)
    elif time == "6" or time == "06" or time == "6am":
        return "06:00"
    # 7am (7:00)
    elif time == "7" or time == "07" or time == "7am":
        return "07:00"
    # 8am (8:00)
    elif time == "8" or time == "08" or time == "8am":
        return "08:00"
    # 9am (9:00)
    elif time == "9" or time == "09" or time == "9am":
        return "09:00"
    # 10am (10:00)
    elif time == "10" or time == "10am":
        return "10:00"
    # 11am (11:00)
    elif time == "11" or time == "11am":
        return "11:00"
    # 12pm (12:00)
    elif time == "12" or time == "12pm":
        return "12:00"
    # 1pm (13:00)
    elif time == "13" or time == "1pm":
        return "13:00"
    # 2pm (14:00)
    elif time == "14" or time == "2pm":
        return "14:00"
    # 3pm (15:00)
    elif time == "15" or time == "3pm":
        return "15:00"
    # 4pm (16:00)
    elif time == "16" or time == "4pm":
        return "16:00"
    # 5pm (17:00)
    elif time == "17" or time == "5pm":
        return "17:00"
    # 6pm (18:00)
    elif time == "18" or time == "6pm":
        return "18:00"
    # 7pm (19:00)
    elif time == "19" or time == "7pm":
        return "19:00"
    # 8pm (20:00)
    elif time == "20" or time == "8pm":
        return "20:00"
    # 9pm (21:00)
    elif time == "21" or time == "9pm":
        return "21:00"
    # 10pm (22:00)
    elif time == "22" or time == "10pm":
        return "22:00"
    # 11pm (23:00)
    elif time == "23" or time == "11pm":
        return "23:00"
    # 12am (24:00)
    elif time == "24" or time == "12am":
        return "24:00"
    # Otherwise format doesn't match
    else:
        return time


#-------------------------------------------------------------------------------
# Class:        StreamToLogger
# Methods:
#               -> __init__ (initialize)
#               -> write(self, message)
#               -> flush(self)
# Variables:
#               -> logger:
#               -> log_level:
#               -> linebuf:
# Description:  Class to log messages from standard output and standard error.
#-------------------------------------------------------------------------------
class StreamToLogger(object):
    #---------------------------------------------------------------------------
    # Function:     initialize
    # Input:        logger -
    #               log_level -
    # Ouput:        none
    # Definition:   Initializes the StreamToLogger class object.
    #---------------------------------------------------------------------------
    def __init__(self, logger, log_level=logging.INFO):
        # Initialize the stream for the logger file
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    #---------------------------------------------------------------------------
    # Function:     write
    # Input:        buf - the buffer storing the message for the log file
    # Output:       none
    # Definition:   Writes the message the terminal and the log file.
    #---------------------------------------------------------------------------
    def write(self, buf):
        # Write the buffer to the log file
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    #---------------------------------------------------------------------------
    # Function:     flush
    # Input:        none
    # Output:       none
    # Definition:   Flushes the log buffer used by the write function.
    #---------------------------------------------------------------------------
    def flush(self):
        pass

# Create an instance of the event class object
sessions = vrs_classes.Event(tinkerfile)

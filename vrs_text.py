# Title: vrs_text.py
# Author: Aaron Chan (Chana030102) & Dustin Schnelle (schnelled)
# Date: 1/24/2019
#
# String variables needed for the Viking Robotics Society discord bot
# =============================================================================

#=================================================
# Program Startup Message
#=================================================
ASCII_ART = " __      ___ _    _          \n\
 \ \    / (_) |  (_)                      \n\
  \ \  / / _| | ___ _ __   __ _           \n\
   \ \/ / | | |/ / | '_ \ / _` |          \n\
    \  /  | |   <| | | | | (_| |          \n\
     \/   |_|_|\_\_|_| |_|\__, |          \n\
                           __/ |          \n\
  _____       _           |___/           \n\
 |  __ \     | |         | | (_)          \n\
 | |__) |___ | |__   ___ | |_ _  ___ ___  \n\
 |  _  // _ \| '_ \ / _ \| __| |/ __/ __| \n\
 | | \ \ (_) | |_) | (_) | |_| | (__\__ \ \n\
 |_|__\_\___/|_.__/ \___/ \__|_|\___|___/ \n\
  / ____|          (_)    | |             \n\
 | (___   ___   ___ _  ___| |_ _   _      \n\
  \___ \ / _ \ / __| |/ _ \ __| | | |     \n\
  ____) | (_) | (__| |  __/ |_| |_| |     \n\
 |_____/ \___/ \___|_|\___|\__|\__, |     \n\
                                __/ |     \n\
                               |___/      "


#=================================================
# Help Command Text
#=================================================
code_mark = "```"
commands_header = "========__Viking Bot Commands__========\n"
help_text = "$help ==> Show this message\n\
$about ==> Get information about test bot\n\
$info ==> Get information about the Viking Robotics Society\n"
commands_admin = "\n========__Admin Commands__========\n\
$linkupdate <term> <year> <new_link> \n ==> Update Availability Poll link stored \
by Viking Bot. Link must start with http://\n\
$addtinkertime <day_of_the_week> <start_time> <end_time> \n ==> Add tinker time to \
tinker_time.txt file\n\
$removetinkertime <day_of_the_week> <start_time> <end_time> \n ==> Remove tinker \
time from tinker_time.txt file"


#=================================================
# Discord Embed Text - About the Society
#=================================================
footer = "Viking Robotics Society - Portland State University"

title = "Viking Robotics Society"
description = "We are the Robotics Club at Portland State, open for the community to join us."
description2 = "Teach robotics and engineering industry skills through projects."
email = "robotics@pdx.edu"
website = "http://robotics.ece.pdx.edu"
resources = "Viking Robotics [Github](https://github.com/pdx-robotics)\n\
Website for our [3D Printer](http://roboprint.cecs.pdx.edu)"
join = "Here's how you can join us formally:\n\
(1) Let us know more about you by filling out the [New Membership Form](https://goo.gl/forms/AUXMLsyf38IpIoJW2).\n\
(2) Join us on [Orgsync](https://orgsync.com/85238/chapter).\n\
(3) Participate in our [Weekly Availability Poll for {}]({}) so we can schedule around everyone's schedule.\n"

meet_desc = "Meetings are held in the Intelligent Robotics Lab located in the \
Fourth Avenue Building basement level in room 70, unless otherwise specified.\n"
gen_meet_info = "First Friday of every month starting at 6pm\n"

#=================================================
# Welcome Text
#=================================================
welcome_text = "Welcome {} to the Discord Server for Viking Robotics Society at Portland State University!\n\
Our group welcomes students of any major and people of the community to join us in learning robotics.\n\
\n\
Please change your nickname to your real name (FirstName LastName), so we can better identify people on the server.\n\
If we haven't seen you at our meetings yet, be sure to stop by that way we know who you are.\n\
See our {} channel for more information, or ask for help in this channel and we'll get back to you."

#=================================================
# Other Text
#=================================================
bot_version = "2019-01-23"
about = "(Version {}) --- I was made to assist the discord channel for Viking \
Robotics Society at Portland State University"

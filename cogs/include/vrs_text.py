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
helpLess = "Show this message"
helpMore = "Provides more information about the command\n\
command (optional) - More information about the specific command"
aboutLess = "Get information about bot"
aboutMore = "Provides the current version of the bot and it's purpose"
infoLess = "Get information about the Viking Robotics Society"
infoMore = "Information about what the Viking Robotics Society does. Provides \
contact information, website, how to join, and more resources. Also displays \
current VRS meeting information."
admincom = "The list of commands below require admin privileges"
linkupdateLess = "Update Availability Poll link stored by Viking Bot. \
Link must start with http://"
linkupdateMore = "Update Availability Poll link stored by Viking Bot. \
Link must start with http://\n\
term - The term of the available poll\n\
year - The year of the available poll\n\
link - The link for the available poll\n"
addtinkertimeLess = "Add tinker time"
addtinkertimeMore = "Add tinker time to the tinker_time.txt file\n\
day - Day of the tinker session (Ex. Monday)\n\
start - Start time of the tinker session (Format XX:XX)\n\
end - End time of the tinker session (Format XX:XX) \n"
removetinkertimeLess = "Remove tinker time"
removetinkertimeMore = "Remove tinker time from the tinker_time.txt file\n\
day - Day of the tinker session (Ex. Monday)\n\
start - Start time of the tinker session (Format XX:XX)\n\
end - End time of the tinker session (Format XX:XX)\n"
membercountLess = "Display number of members with defined roles"
membercountMore = "Display number of members with the following roles:\n\
Member, Admin, Lab Access, Aquanautics, Terranuatics, & Aeronautics"

#=================================================
# Discord Embed Text - About the Society
#=================================================
footer = "Viking Robotics Society - Portland State University"

title = "Viking Robotics Society"
description = "We are the Robotics Society at Portland State, open for the community to join us."
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
about = "I was made to assist the Discord channel for Viking \
Robotics Society at Portland State University.  You can find my source code on https://github.com/pdx-robotics/VikingBot"

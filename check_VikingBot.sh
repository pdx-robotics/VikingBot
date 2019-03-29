#!/bin/bash
#
# Checks for screen session that's running VikingBot.py
# To be used with crontab to check that Discord bot is running periodically
#
# Add to crontab jobs by using command "crontab -e"
# Add the following line to the opened file to run every 2 hours
#   0 */2 * * * ~/VikingBot/check_VikingBot.sh

if ps -ef | grep SCREEN | grep VikingBot ; then
    exit 0
else
    screen -dmS VikingBot bash -c "python3.6 ~/VikingBot/VikingBot.py -r"
    echo "Restarted VRS Discord bot - VikingBot"
    exit 0

fi

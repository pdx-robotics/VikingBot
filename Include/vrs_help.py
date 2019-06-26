import os, sys, inspect, discord
import vrs_ids, vrs_text

#import inspect
#print(inspect.getfile(inspect.currentframe()))
#print(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
textdir = 'Text'
filehelp = 'command_help.txt'
fileadmin = 'admin_commands.txt'

admin_commands = []
commands = {}  # Empty dicionary to hold text for commands

# import list of admin commands and 
def help_setup(path):
    # Read in descriptions and syntax for supported commands
    with open(os.path.join(path,textdir,filehelp),'r') as f:
        read_data = f.read()
        f.close()
    
    data = read_data.split('\n')
    
    for d in data:
        c = d.split('|')
        commands.update({c[0]:(c[1],c[2])})

    # Read in list of admin commands
    with open(os.path.join(path,textdir,fileadmin),'r') as f:
        read_data = f.read()
        f.close()
    
    for d in read_data.split('\n'):
        admin_commands.append(d)

def get_help(command=None):
    if command == None:
        text = 'Supported commands for this bot: ```'
        for c in commands:
            text += commands[c][0]+'\n'
        text+='```'
        return (0,text)

    elif command in commands:
        embed = discord.Embed(title=None)
        embed.set_footer(text=vrs_text.footer)
        embed.add_field(name=commands[command][0], value = commands[command][1])
        return (1, embed)
    else:
        text = f'{command} is not supported. See $help for a list of commands.'
        return (0,text)



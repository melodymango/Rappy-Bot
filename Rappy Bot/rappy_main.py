'''
This is a learning experience!!

TO-DO:
[!piyo] command. Will show the "piyo piyo" symbol art from PSO2. 

CURRENT BUGS:
1) send_hug() will not work if @everyone or @here is called

'''

import discord
import random
import re

#create client object
client = discord.Client()

#global variables
rappy_hug = 'http://blog-imgs-88.fc2.com/p/s/o/pso2ship10sun/pso20160201_155126_023_ss.jpg'
my_server = '126513229588332544'


#Triggered by 'test'
#Just a way of making sure Rappy can hear you/seeing if you're still connected to the server
def test_result(message):
    return 'I hear you, {0.author.mention}!'.format(message)
     
#Triggered by '!help'. 
#Shows a list of commands available for users to use with Rappy. Does not include secret commands like !fuckyou and !piyo     
def provide_help():
    msg = ("Piyo piyo~ :musical_note: I'm Rappy! Here's what I can do so far:\n\n"
           "`test` - I'll reply! Handy for testing your connection.\n"
           "`!choice: a, b, ..., z` - Need to decide between at least 2 different things? I can do it for you!\n"
           "`!hug <@optional_usernames> ` - Need a hug? I'll hug you back! Or you can have me hug someone else! :hearts: \n")
    return msg  

#Triggered by '!hug <optional_user_name>'
#Gives a hug to you if no username is provided, otherwise will hug a specified user.
def send_hug(message):
    if message.content.strip() == '!hug':
        return '{0.author.mention}\n'.format(message) + rappy_hug
    elif len(message.mentions) == 0:
        return "There's no one by that name to hug! QvQ"
    else:
        output = ''
        for member in message.mentions:
            output += (member.mention + ' ')
        return '{}\n'.format(output) + rappy_hug
        
#Triggered by '!fuckyou'
#Why are you so mean to Rappy? 
def fuck_you(message):
    return 'Fuck you too, {0.author.mention}!'.format(message)  

#Triggered by '!lenny'
#Returns everone's favorite emoticon
def lenny(message):
    lenny_true = re.match('^!lenny( x(\d+))?$', message.content)
    if lenny_true:
        if lenny_true.group(2):
            return '( ͡° ͜ʖ ͡°) ' * int(lenny_true.group(2))
        else:
            return '( ͡° ͜ʖ ͡°)'
    else:
        return 'ABORT ABORT!!!'

#Triggered by '!choice a, b, ..., z '
#Randomly selects a choice from the given options.
def choice(message):
    print('choice called')
    try:
        if message.content.find(':') == -1 or message.content.find(':') > 7:
            raise Exception("Format Error")
        choice_list = re.split(',|;', message.content[message.content.find(':') + 1:])
        print(choice_list)
        if len(choice_list) <= 1:
            return "Did you really expect me to make a choice with 0 or 1 options?"
        return choice_list[random.randint(0, len(choice_list) - 1)]
    except:
        return "You didn't format this command right! It's `!choice: a, b, ..., z`!"

#Rappy is always listening for your commands.
@client.async_event
def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content == 'test':
        yield from client.send_message(message.channel, test_result(message))
    elif message.content == '!help':
        yield from client.send_message(message.channel, provide_help()) 
    elif message.content == '!fuckyou':
        yield from client.send_message(message.channel, fuck_you(message))
    elif message.content == '!piyo':
        yield from client.send_message(message.channel, fuck_you(message))
    elif message.content.startswith('!hug'):
        yield from client.send_message(message.channel, send_hug(message))
    elif message.content.startswith('!choice'):
        yield from client.send_message(message.channel, choice(message))
    elif message.content.startswith('!lenny'):
        yield from client.send_message(message.channel, lenny(message))


@client.async_event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #yield from client.send_message(client.get_channel('126513229588332544'), "I'm online now, piyo!")

client.run('MjM2NTIxODYyMzUwMjQxNzky.CuKV2g.BFu_dRkgcNJUfdcAXpwTsp3SDuE')








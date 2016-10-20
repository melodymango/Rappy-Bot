'''
This is a learning experience!!

TO-DO:
[!piyo] command. Will show the "piyo piyo" symbol art from PSO2. 

CURRENT BUGS:
1) send_hug() will mention the wrong user if there are two or more users with the same username/nickname on the server

'''

import discord
import random
import re

#create client object
client = discord.Client()
rappy_hug = 'http://blog-imgs-88.fc2.com/p/s/o/pso2ship10sun/pso20160201_155126_023_ss.jpg'

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
           "`!hug <optional_username> ` - Need a hug? I'll hug you back! Or you can have me hug someone else! :hearts: \n")
    return msg  

#Triggered by '!hug <optional_user_name>'
#Gives a hug to you if no username is provided, otherwise will hug a specified user.
def send_hug(message):
    if message.content == '!hug':
        return '{0.author.mention}\n'.format(message) + rappy_hug
    #Will not work correctly if there are two or more users sharing the same nickname/username
    else:
        user_name = message.content[4:].strip()
        if client.get_server('126513229588332544').get_member_named(user_name) != None:
            return '{}\n'.format(client.get_server('126513229588332544').get_member_named(user_name).mention) + rappy_hug
        else:
            return "There's no one by that name I can hug! QvQ"
        
#Triggered by '!fuckyou'
#Why are you so mean to Rappy? 
def fuck_you(message):
    return 'Fuck you too, {0.author.mention}!'.format(message)  

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


@client.async_event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    #yield from client.send_message(client.get_channel('126513229588332544'), "I'm online now, piyo!")

client.run('MjM2NTIxODYyMzUwMjQxNzky.CuKV2g.BFu_dRkgcNJUfdcAXpwTsp3SDuE')








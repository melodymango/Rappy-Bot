'''
This is a learning experience!!
'''

import discord
import random
import re

client = discord.Client()

def test_result(message):
    return 'I hear you, {0.author.mention}!'.format(message)
     
def provide_help():
    msg = ("Piyo piyo~ :musical_note: I'm Rappy! Here's what I can do so far:\n\n"
           "`test` - I'll reply! Handy for testing your connection.\n"
           "`!choice: a, b, ..., z` - Need to decide between at least 2 different things? I can do it for you!\n"
           "`!hug` - Need a hug? I'll hug you back! :hearts: \n")
    return msg  

def send_hug(message):
    if message.content == '!hug':
        return 'http://blog-imgs-88.fc2.com/p/s/o/pso2ship10sun/pso20160201_155126_023_ss.jpg'
    else:
        user_name = message.content[4:].strip()
        return '{}\nhttp://blog-imgs-88.fc2.com/p/s/o/pso2ship10sun/pso20160201_155126_023_ss.jpg'.format(user_name)

def fuck_you(message):
    return 'Fuck you too, {0.author.mention}!'.format(message)  

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
    for member in client.get_server('126513229588332544'):
        print(member.)

client.run('MjM2NTIxODYyMzUwMjQxNzky.CuKV2g.BFu_dRkgcNJUfdcAXpwTsp3SDuE')








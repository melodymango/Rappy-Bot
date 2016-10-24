'''
Handling of custom commands
'''

default_commands = ['test', 'help', 'fuckyou', 'piyo', 'hug', 'choice', 'lenny', 'newcommand' ]
command_types = ['image', 'copypasta']
image_types = ['.jpg', '.png', '.gif']

def new_command(message):
    try:
        nc_arguments = message.content.split()
        if nc_arguments[1] in default_commands:
            return 'You cannot overwrite a default command!'
        if nc_arguments[2] not in command_types:
            return "Not a valid command type: please use \"image\" or \"copypasta\"."
        
        if nc_arguments[2] == 'image':
            if nc_arguments[3].startswith('http://i.imgur.com/') and nc_arguments[3][len(nc_arguments[3]) - 4:] in image_types:
                return 'We good, fam.'
            else:
                return 'NOPE NOPE NOPE'
                
        return 'So far, so good!'
    except:
        return 'Nothing happened because you probably made a formatting error!'


def return_position_server(server_list: list, server_name: str):
    """Loops through the current servers until it finds the server that it is asking for"""  # noqa: E501
    index = 0
    for i in range(0, len(server_list)):
        if(server_list[i].name == server_name):
            index = i
        else:
            continue
    return index


def find_channel(server_name: str, channel_name: str, bot):
    """Grabs the current server, and looks for the channel passed in"""
    index = return_position_server(bot.guilds, server_name)
    channel_list = bot.guilds[index].channels
    for i in channel_list:
        if(i.name == channel_name):
            return i.id
        else:
            continue


def find_role(server_name: str, role_name: str, bot):
    index = return_position_server(bot.guilds, server_name)
    role_list = bot.guilds[index].roles
    for i in role_list:
        if(i.name == role_name):
            return i
        else:
            continue

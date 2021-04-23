import discord
from discord.ext import commands
from members import find_role, find_channel
import os
from dotenv import load_dotenv
load_dotenv()
STARTING_ROLE = os.getenv("START_ROLE")
GUILD = os.getenv('KNIGHTHACKS')
CODE_OF_CONDUCT_MESSAGE = os.getenv('CODE_MESSAGE')
LOGGING_CHANNEL = os.getenv('LOGGING_CHANNEL_ID')
class ClubWelcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        new_user_msg = ("Hi there! Welcome to the Knight Hacks Discord server.\n" + 
        "We're happy you're here!\nIn order to finish joining:" +  
        "\n\t- Please accept the Code of Conduct using the ✅ reaction" + 
        " in the #code-of-conduct channel\n\t- Please set your nickname to match our" + 
        " naming rules.\nTo check out the awesome ways to get involved, go to the" +  
        " #club-information channel.\nAnd be sure to introduce yourself in" + 
        " #introductions!")
        
        channel = self.bot.get_channel(LOGGING_CHANNEL)
        embed = discord.Embed(description = "User " + member.mention + " joined the server.", color=0x00ff00)
        await channel.send(embed = embed)
        try:
            member_role = find_role(GUILD, STARTING_ROLE, self.bot)
            await member.add_roles(member_role)
            await member.send(new_user_msg)
        except:
            embed = discord.Embed(description = "Couldn't send welcome DM to " + member.mention, color=0xff0000)
            await channel.send(embed = embed)
    """
    Waits for the ✅ emoji to be used on the specified message
    Checks if the role is unverified, then changes to member
    """
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.guild_id is None:
            return
        message_id = payload.message_id
        if message_id == int(CODE_OF_CONDUCT_MESSAGE):
            emoji = payload.emoji.name
            if(emoji == "✅"):
                user = payload.member
                for i in user.roles:
                    if(i.name == STARTING_ROLE):
                        await user.remove_roles(i)
                        member_role = find_role(GUILD, "Member", self.bot)
                        await user.add_roles(member_role)
                        channel = self.bot.get_channel(LOGGING_CHANNEL)

                        embed = discord.Embed(description = "User " + user.mention + " has accepted #code-of-conduct.", color=0x00ff00)
                        await channel.send(embed = embed)

def setup(bot):
    bot.add_cog(ClubWelcome(bot))
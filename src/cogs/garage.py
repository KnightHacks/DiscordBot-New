from discord.ext import commands


class Garage(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['parking'])
    async def garage(self, ctx):
        pass
        # complete_url = 'https://secure.parking.ucf.edu/GarageCount/iframe.aspx'


def setup(bot):
    bot.add_cog(Garage(bot))

from discord.ext import commands


class ShakespeareInsults(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.command()
    # async def insult(self, ctx):


def setup(bot):
    bot.add_cog(ShakespeareInsults(bot))

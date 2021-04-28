from discord.ext import commands
import random


class Devselect(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        aliases=["pr-reviewers", "pr-reviewer-select", "pr", "pr-review"]
    )
    @commands.has_role("Dev Team")
    async def devselect(self, ctx, count, *names):
        count = int(count)
        pr_reviewers = ", ".join(random.choices(names, k=count))
        await ctx.send(
            f"{ctx.author.mention}"
        )
        await ctx.send("PR reviewers selected from list are: " + pr_reviewers)


def setup(bot):
    bot.add_cog(Devselect(bot))

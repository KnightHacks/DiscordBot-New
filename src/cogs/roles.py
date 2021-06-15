import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
import os
from discord_slash.utils.manage_commands import create_choice, create_option
from dotenv import load_dotenv

load_dotenv()
MSGID = os.getenv('823687567206776862')
GUILD_ID = int(os.getenv('GUILD_ID'))

roles_map = {
        # Format:
        # 'emoji' : 'rolename'
        "👔": "OPS",
        "python": "Python",
        "java": "Java",
        "clang": "CLang",
        "cplusplus": "C++",
        "csharp": "C#",
        "javascript": "JavaScript",
        "htmlcss": "HTML/CSS",
        "rust": "Rust",
        "lua": "Lua",
        "linux": "Linux",
        "windows": "Windows",
        "macos": "MacOS",
        "math": "Math",
        "👩‍🔬": "Physics",
        "knighthacks": "knighthacks"
    }

choices = map(
    lambda entry:
        create_choice(
            name=entry,
            value=entry
        ), roles_map.values())


class Roles(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name='addRole', description='Adds a role to your account.', guild_ids=[GUILD_ID], options=[
        create_option(
            name="role",
            description="The role to add.",
            option_type=3,
            required=True,
            choices=map(
                lambda entry:
                    create_choice(
                        name=entry,
                        value=entry
                    ), roles_map.values())
        )
    ])
    async def _addrole(self, ctx: SlashContext, role: str):
        # Show the user that the bot is thinking.
        await ctx.defer()

        # Fetch the role from the cache.
        fetched_role = discord.utils.get(ctx.guild.roles, name=ctx.args[0])

        # This branch shouldn't happen, but just in case...
        if (fetched_role is None):
            await ctx.send(f"Error: could not find the role: '{ctx.args[0]}'")
            return

        # Check prior membership
        if (fetched_role in ctx.author.roles):
            await ctx.send(f"You are already part of {role}.")
            return

        # Add member to role.
        member = ctx.author
        await member.add_roles(fetched_role)

        # We did it!
        await ctx.send(f"Successfully registered for role: {role}!")

    @cog_ext.cog_slash(name='removeRole', description='Removes a role from your account.', guild_ids=[GUILD_ID], options=[
        create_option(
            name="role",
            description="The role to remove.",
            option_type=3,
            required=True,
            choices=map(
                lambda entry:
                    create_choice(
                        name=entry,
                        value=entry
                    ), roles_map.values())
        )
    ])
    async def _removerole(self, ctx: SlashContext, role: str):
        # Show the user that the bot is thinking.
        await ctx.defer()

        # Fetch the role from the cache.
        fetched_role = discord.utils.get(ctx.guild.roles, name=ctx.args[0])

        # This branch shouldn't happen, but just in case...
        if (fetched_role is None):
            await ctx.send(f"Error: Could not find the role: '{ctx.args[0]}.'")
            return

        # Check prior membership
        if (fetched_role not in ctx.author.roles):
            await ctx.send(f"You are not a member of {role}.")
            return

        # Add member to role.
        member = ctx.author
        await member.remove_roles(fetched_role)

        # We did it!
        await ctx.send(f"Successfully removed role: {role}!")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.guild_id is None:
            return

        message_id = payload.message_id
        role = None
        if message_id == int(MSGID):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name in self.roles_map:
                role = discord.utils.get(
                    guild.roles, name=self.roles_map[payload.emoji.name])
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.add_roles(role)
                    print('Role assignment: Done.')
            else:
                print('Role not found.')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.guild_id is None:
            return

        message_id = payload.message_id
        role = None

        if message_id == int(MSGID):
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)

            if payload.emoji.name in self.roles_map:
                role = discord.utils.get(
                    guild.roles, name=self.roles_map[payload.emoji.name])
            else:
                role = discord.utils.get(guild.roles, name=payload.emoji.name)

            if role is not None:
                member = discord.utils.find(
                    lambda m: m.id == payload.user_id, guild.members)
                if member is not None:
                    await member.remove_roles(role)
                    print('Role removal: Done.')
            else:
                print('Role not found.')

# Connect cog to bot


def setup(bot):
    bot.add_cog(Roles(bot))

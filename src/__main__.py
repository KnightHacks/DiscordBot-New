import os
from src import bot

TOKEN = os.getenv('DISCORD_TOKEN')


def main():
    bot.run(TOKEN)

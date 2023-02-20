import discord
from discord.ext import commands
from discord.ui import View

class Ticket(View):

    def __int__(self, bot) -> None:
        super().__init__(timeout=None)
        self.client: commands.Bot = bot

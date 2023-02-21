import discord
from discord.ext import commands
from discord.ui import View
from checkmate.models.modals import RequestReceiver

class PurchaseMenu(View):

    def __init__(self, bot) -> None:
        super().__init__(timeout=None)
        self.client: commands.Bot = bot

    @discord.ui.button(label="Custom Bot", style=discord.ButtonStyle.primary)
    async def custom_bot(self, interaction: discord.Interaction, button: discord.ui.Button):
        modal = RequestReceiver()
        await interaction.response.send_modal(modal)
        self.stop()

    @discord.ui.button(label="Pre-Made Bot", style=discord.ButtonStyle.secondary)
    async def premade_bot(self, interaction: discord.Interaction, button: discord.ui.Button):
        pass

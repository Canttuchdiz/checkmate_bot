import discord
from discord import PartialEmoji
from discord.ext import commands
from discord.ui import View
from checkmate.models.modals import RequestReceiver
from checkmate.utils.config import Config


class PurchaseMenu(View):

    def __init__(self, bot) -> None:
        super().__init__(timeout=None)
        self.client: commands.Bot = bot

    @discord.ui.button(label=Config.OPTIONS[0], style=discord.ButtonStyle.primary,
                       emoji='<:developer:1077792501332709498>')
    async def custom_bot(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        """
        Button used for submitting a custom bot request.
        """
        modal = RequestReceiver()
        await interaction.response.send_modal(modal)
        self.stop()

    @discord.ui.button(label=Config.OPTIONS[1], style=discord.ButtonStyle.secondary, emoji='🤖')
    async def premade_bot(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        """
        Button used for choosing a premade bot to be bound to your bot.
        """
        pass

    @discord.ui.button(label=Config.OPTIONS[2], style=discord.ButtonStyle.secondary, emoji='☁')
    async def hosting(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        """
        Button used for submitting a hosting request.
        """
        pass


class TicketClose(View):

    def __init__(self, channel: discord.TextChannel):
        super().__init__(timeout=None)
        self.channel = channel

    @discord.ui.button(label="Close", style=discord.ButtonStyle.danger, emoji='🔒')
    async def close(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.channel.delete()
        self.stop()

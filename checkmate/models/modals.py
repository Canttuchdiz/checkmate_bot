import discord
from discord.ext import commands
from discord.ui import Modal
from checkmate.utils.config import Config
from checkmate.models.types import CustomBot, RequestData
import traceback

class RequestReceiver(Modal, title='Bot Request'):

    description = discord.ui.TextInput(label='Description', style=discord.TextStyle.paragraph)

    def __init__(self) -> None:
        super().__init__(timeout=None)
        self.order_category: int = Config.ORDER_CAT

    async def on_submit(self, interaction: discord.Interaction) -> None:
        data = RequestData(interaction.guild, interaction.user, self.description.value, interaction.response, "Orders")
        request = CustomBot(data)
        await request.create_request()
        await interaction.response.edit_message(content="Request was sent!", view=None)
        self.stop()



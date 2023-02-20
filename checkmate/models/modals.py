import discord
from discord.ext import commands
from discord.ui import Modal
from checkmate.utils.config import Config
import traceback

class RequestReceiver(Modal, title='Bot Request'):

    description = discord.ui.TextInput(label='Description', style=discord.TextStyle.paragraph)

    def __init__(self, dev: str) -> None:
        super().__init__(timeout=None)
        self.order_category: int = Config.ORDER_CAT
        self.dev = dev

    async def on_submit(self, interaction: discord.Interaction) -> None:

        category = discord.utils.get(interaction.guild.categories, name="Orders")
        channel = await category.create_text_channel(name="order")
        embed = discord.Embed(title=f"Bot Request", description=self.description.value,
                              color=discord.Color.blurple())
        embed.set_author(name=interaction.user, icon_url=interaction.user.avatar)
        embed.set_footer(text=f"ID · {interaction.user.id}")
        if self.dev:
            await channel.send(content=f"<@{self.dev}>", embed=embed)
        else:
            await channel.send(embed=embed)

        await interaction.response.send_message("Request was sent!", ephemeral=True)

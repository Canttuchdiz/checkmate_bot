import discord
from discord import app_commands
from discord.ext import commands
from checkmate.utils.config import Config
from checkmate.models.modals import RequestReceiver
from typing import Optional, Union, List, Any

class Broker(commands.Cog):

    def __int__(self, bot) -> None:
        self.client: commands.Bot = bot

    async def dev_autocomplete(self, interaction: discord.Interaction, current: str) -> Any:
        devs = [interaction.guild.get_member(user_id) for user_id in Config.DEVS]
        return [app_commands.Choice(name=dev.name, value=str(dev.id)) for dev in devs if current.lower() in dev.name.lower()]

    # Send modal with user request
    @app_commands.command(name="buy", description="Allows user to fill out bot request")
    @app_commands.autocomplete(developer=dev_autocomplete)
    async def buy(self, interaction: discord.Interaction, developer: Optional[str]) -> None:

        modal = RequestReceiver(developer)
        await interaction.response.send_modal(modal)

async def setup(bot):
    await bot.add_cog(Broker(bot))

import discord
from discord import app_commands
from discord.ext import commands
from discord.types.snowflake import Snowflake
from checkmate.utils.config import Config
from checkmate.models.views import PurchaseMenu
from typing import Optional, Union, List, Any

class Broker(commands.Cog):

    def __init__(self, bot) -> None:
        self.client: commands.Bot = bot
        self.in_ticket: List[Snowflake] = []

    # async def dev_autocomplete(self, interaction: discord.Interaction, current: str) -> Any:
    #     devs = [interaction.guild.get_member(user_id) for user_id in Config.DEVS]
    #     return [app_commands.Choice(name=dev.name, value=str(dev.id)) for dev in devs if current.lower() in dev.name.lower()]

    # Send modal with user request
    @app_commands.command(name="buy", description="Allows user to fill out bot request")
    async def buy(self, interaction: discord.Interaction) -> None:
        view = PurchaseMenu(self.client)
        options = '**|**'.join([f"``{option}``" for option in Config.OPTIONS])
        embed = discord.Embed(title="Purchase Options", color=discord.Color.yellow(),
                              description="You have the option to choose:\n" + options)
        for i, button in enumerate(view.children):
            embed.add_field(name=button.label, value=f"${Config.PRICES[i]}")
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)
        self.in_ticket.append(interaction.user.id)


async def setup(bot):
    await bot.add_cog(Broker(bot))

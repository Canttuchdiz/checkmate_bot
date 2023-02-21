import discord
from typing import Union

class UtilMethods:

    @staticmethod
    async def text_cat(guild: discord.Guild, category: str,
                 user_client: Union[discord.User, discord.Member]) -> discord.TextChannel:
        category = discord.utils.get(guild.categories,
                                     name=category)
        channel = await category.create_text_channel\
            (name=f"order-{user_client.name}")
        return channel

    @staticmethod
    def embedify(title: str, description: str, color: discord.Color) -> discord.Embed:
        embed = discord.Embed(title=title, description=description, color=color)
        return embed

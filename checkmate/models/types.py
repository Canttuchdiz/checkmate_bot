from __future__ import annotations
import discord
from checkmate.utils.utilities import UtilMethods
from dataclasses import dataclass
from typing import Union


class BaseRequest:

    def __init__(self, data: RequestData) -> None:
        self.guild = data.guild
        self.user_client = data.user_client
        self.description = data.description
        self.response = data.response
        self.category = data.category

    def _request_embed(self) -> discord.Embed:
        embed = discord.Embed(title=f"Bot Request", description=self.description,
                              color=discord.Color.blurple())
        embed.set_author(name=self.user_client, icon_url=self.user_client.avatar)
        embed.set_footer(text=f"ID · {self.user_client.id}")
        return embed

    async def create_request(self) -> None:
        channel = await UtilMethods.text_cat(self.guild, self.category, self.user_client)
        embed = self._request_embed()
        await channel.send(embed=embed)


class CustomBot(BaseRequest):

    def __int__(self, data: RequestData):
        super().__init__(data)
        pass


class PreMadeBot(BaseRequest):
    pass


# put methods on dataclass
@dataclass
class RequestData:
    guild: discord.Guild
    user_client: Union[discord.User, discord.Member]
    description: str
    response: discord.InteractionResponse
    category: str

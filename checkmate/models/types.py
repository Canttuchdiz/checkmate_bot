from __future__ import annotations
import discord
from checkmate.utils.utilities import UtilMethods
from dataclasses import dataclass
from typing import Union


class BaseRequest:

    def __init__(self, data: RequestData) -> None:
        self.data = data
        self.guild = data.guild
        self.user_client = data.user_client
        self.description = data.description
        self.response = data.response
        self.category = data.category

    async def create_request(self) -> None:
        channel = await UtilMethods.text_cat(self.guild, self.category, self.user_client)
        await channel.set_permissions(self.user_client, send_messages=True, read_messages=True,
                                      attach_files=True, external_emojis=True, read_message_history=True)
        embed = self.data.request_embed()
        from checkmate.models.views import TicketClose
        view = TicketClose(channel)
        await channel.send(embed=embed, view=view)


class CustomBot(BaseRequest):

    def __int__(self, data: RequestData) -> None:
        super().__init__(data)
        pass


class PreMadeBot(BaseRequest):
    pass


class HostingRequest(BaseRequest):
    pass


# put methods on dataclass
@dataclass
class RequestData:
    guild: discord.Guild
    user_client: Union[discord.User, discord.Member]
    description: str
    response: discord.InteractionResponse
    category: str
    budget: str

    def request_embed(self) -> discord.Embed:
        embed = discord.Embed(title=f"Custom Bot Request", color=discord.Color.blurple())
        embed.set_author(name=self.user_client, icon_url=self.user_client.avatar)
        embed.add_field(name="Request", value=self.description)
        embed.add_field(name="Budget", value=self.budget)
        embed.set_footer(text=f"ID · {self.user_client.id}")
        return embed

import discord
from discord.ext import commands
import traceback
import sys

class Events(commands.Cog):
    """
    Handles events, and encapsulates two event commands.
    """


    def __init__(self, bot) -> None:
        self.client: commands.Bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print('Ready!')
        print('Logged in as ---->', self.client.user)
        print('ID:', self.client.user.id)
        # print(f'Version: {Config.VERSION}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error) -> None:
        ignored = (commands.CommandNotFound,)

        # Anything in ignored will return and prevent anything happening.
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        # elif isinstance(error, InvalidTable):
        #     await ctx.send("Please provide a valid table")

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.NotOwner):
            await ctx.send(f"{ctx.command} is reserved for the bot owners.")

            # For this error example we check to see where it came from...
        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'
                await ctx.send('I could not find that member. Please try again.')

        else:
            # All other Errors not returned come here. And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        """Below is an example of a Local Error Handler for our command do_repeat"""


async def setup(bot):
    await bot.add_cog(Events(bot))
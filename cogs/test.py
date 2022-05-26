import discord
import base64
import datetime
import whois
import aiowiki
import utils

from typing import Optional, Union

from discord import Color, Member, Role, User
from discord.ext import commands

class Test(commands.Cog, name='Test'):
    """Get info for Discord objects, domains, and more"""

    def __init__(self, bot: utils.CustomBot):
        self.bot: utils.CustomBot = bot

    @commands.command(aliases=['img'])
    async def test(self, ctx: utils.CustomContext, *, user: Optional[discord.User]):
        """Shows user's avatar using their ID or name"""

        descp = '''
         Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
         Quisque vel mi facilisis justo sodales iaculis. Proin fringilla diam aliquet arcu faucibus ullamcorper. Fusce eget enim non neque blandit vulputate vel non libero. Ut semper hendrerit fringilla. Donec lacinia ut lorem vel ultrices. Nulla vitae libero sit amet libero dapibus condimentum ut sit amet felis. 
         Cras in nisl tempus, suscipit eros imperdiet, commodo dui. Ut gravida congue purus, nec ullamcorper metus dapibus et. In ut posuere felis. Nulla posuere pulvinar interdum. Maecenas sit amet leo a sapien bibendum viverra. Vestibulum eleifend tellus eu lacus porttitor sagittis at ullamcorper eros.
         '''
        embed = utils.create_embed(title='Test Embed Here', color='#1ABC9C', image='https://i.imgur.com/wxhEPNq.png', thumbnail='https://i.imgur.com/xVA6z7W.png')
        embed.description = descp
        embed.add_field(name="Field 1 test", value=f'Some random text inline', inline=True)
        embed.add_field(name="Field 2 test", value=f'Some random text inline', inline=True)
        embed.add_field(name="Field 3 test", value=f'Some random text inline', inline=True)
        embed.add_field(name="Field 4 big test", value=f'Some random text that is not inlinein this case', inline=False)

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Test(bot))

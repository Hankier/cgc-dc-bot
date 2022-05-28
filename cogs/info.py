import discord
import base64
import datetime
import whois
import aiowiki
import utils

from typing import Optional, Union

from discord import Color, Member, Role, User
from discord.ext import commands

class Info(commands.Cog, name='Information'):
    """Help for bot."""

    def __init__(self, bot: utils.CustomBot):
        self.bot: utils.CustomBot = bot

    @commands.command(aliases=['pomoc'])
    async def info(self, ctx: utils.CustomContext):
        """Shows help"""


        description = """
        `info` - wyświetla pomoc,
        `gas` - pokazuje koszty gasu w GWEI,
        `nft <fraza>` - wyświetla listę wyboru kolekcji które zawierają <fraza> aby wyświetlić informacje,
        `add <slug>` - dodaje kolekcje o podanym slugu (dla CGC link opensea to `https://opensea.io/collection/coolguyscapital` a slug to końcówka `coolguyscapital`,
        `add ` - wyświetla pomoc jak pobrać slug kolekcji,
        `list` - wyświetla listę śledzonych kolekcji (dużo pojektów, raczej nie polecam używać).

        Jestem otwarty, zgłaszaj wszystkie pomysły, bugi, zadawaj pytania, postaram się odpowiedzieć. :)
        """
        cgc_dashboard = 'http://stats.coolguys.space/d/5WEccYunk/stats-of-colletions?orgId=1&var-collection=Cool%20Guys%20NFT&from=now-2d&to=now'

        embed_color = discord.Color.teal()
        embed = utils.create_embed(title='Pomoc', color='#1ABC9C')
        #embed.description = description
        embed.add_field(name='Lista komend', value=f'{description}', inline=False)
        embed.add_field(name='Dashboard z statystykami', value=f'[Dashboard Cool Guys NFT]({cgc_dashboard})', inline=False)
        embed.add_field(name='Kontakt Discord', value=f'<@453871191162224643>', inline=False)
        embed.add_field(name='Kontakt mail', value=f'[hankier@hqr.sh](mailto:hankier@hqr.sh)', inline=False)

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Info(bot))

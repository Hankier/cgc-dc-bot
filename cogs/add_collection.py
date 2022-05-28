import discord
import base64
import datetime
import whois
import aiowiki
import json
import utils
import requests

from typing import Optional, Union
from .collection import Collection

from discord import Color, Member, Role, User
from discord.ext import commands

class AddCollection(commands.Cog, name='AddCollection'):
    """Gas value for Etherneum."""

    def __init__(self, bot: utils.CustomBot):
        self.bot: utils.CustomBot = bot
        self.api = self.bot.config.hqr_api()

    @commands.command()
    async def add(self, ctx: utils.CustomContext, *, user: Optional[discord.User]):
        """Add collection to gather stats."""
        params = ' '.join(ctx.message.content.split()[2:])
        user = user or ctx.author
        if len(params) == 0:
            embed = utils.create_embed(title='None collection-slug provided', color='#DC143C', image='https://i.imgur.com/YXTozq4.png')
            info = """
            You have to provide colletion slug form opensea.io
            For example for Cool Guys Capital NFT it's `coolguyscapital`.
            Go to opensea.io collection page and copy slug from link.
            Take a look on image instruction.
            """
            embed.description = info
            await ctx.send(embed=embed)
        else:
            url = f'{self.api}/take-all'
            myobj = {"user": f"{user.id}", "collection": params}
            response = requests.post(url, json=myobj)
            info = response.json()
            print(info)
            if not info['error']:
                collection = Collection(response.json())
                if info['added']:
                    embed = collection.embed(title_prefix='Collection added: ')
                    await ctx.send(embed=embed)
                if not info['added']:
                    embed = collection.embed(title_prefix='Collection exists: ', color='#FE5000')
                    await ctx.send(embed=embed)
            elif not info['added'] and info['error']:
                embed = utils.create_embed(title='Something went wrong.', color='#DC143C')
                embed.description = 'Couldn\'t add to database.'
                embed.add_field(name='Reason', value=f'{info["reason"]}', inline=False)
                await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(AddCollection(bot))

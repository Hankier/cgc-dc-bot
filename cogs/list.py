import discord
import utils
import random
import requests

from discord.ext import commands
from typing import Optional, Union
from .collection import Collection

class Collections(commands.Cog, name='Collections'):

    def __init__(self, bot: utils.CustomBot):
        self.bot: utils.CustomBot = bot

    def get_project_list(self):
        url = 'http://api.coolguys.space/projects'
        myobj = {"user":"xyz"}
        x = requests.post(url, json=myobj)
        return x.json()['projects']

    @commands.command(aliases=['collections'])
    async def list(self, ctx: utils.CustomContext, *, user: Optional[discord.User]):
        projects = self.get_project_list()

        results = utils.chunks(projects, 25)
        for k, chunk in enumerate(results,0):
            embed = utils.create_embed(title='Lista śledzonych kolekcji NFT', color='#cc00ff')
            for i,x in enumerate(chunk, 1 + (25 * k)):
                embed.add_field(name=f'{i}. {x["name"]}', value=f'[opensea.io/collection/{x["opensea"]}](https://opensea.io/collection/{x["opensea"]})', inline=False)

            await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Collections(bot))

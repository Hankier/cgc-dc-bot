import discord
import utils
import random
import requests

from discord.ext import commands
from typing import Optional, Union
from .collection import Collection


class NFTDropdown(discord.ui.Select):
    def __init__(self, params, projects, api):
        self.api = api

        options = []


        for project in projects:
            options.append(discord.SelectOption(label=f'{project["name"]}'))

        super().__init__(placeholder='Choose NFT project', min_values=1, max_values=1, options=options)

    def get_project_info(self, pr_id: int):
        url = f'{self.api}/project-info'
        myobj = {"user":"xyz","password":"xyz", "project_id": pr_id}
        x = requests.post(url, json=myobj)
        return x.json()

    def get_project_info_by_name(self, name: str):
        url = f'{self.api}/project-info-name'
        myobj = {"user":"xyz","password":"xyz", "project_name": name}
        x = requests.post(url, json=myobj)
        return x.json()

    async def callback(self, interaction: discord.Interaction):
        value = self.values[0]
        project_info = self.get_project_info_by_name(value)
        info = Collection(project_info)
        embed = info.embed()


        await interaction.response.send_message(ephemeral=False, embed=embed)


class NFTDropdownView(discord.ui.View):
    def __init__(self, params, projects, api):
        super().__init__()

        self.add_item(NFTDropdown(params, projects, api))


class NFTDrop(commands.Cog, name='NFTDrop'):

    def __init__(self, bot: utils.CustomBot):
        self.bot: utils.CustomBot = bot
        self.api = bot.config.hqr_api()

    def get_project_list(self, params):
        url = f'{self.api}/projects-like'
        myobj = {"user":"xyz","password":"xyz", "project_id": 1, "like": params}
        x = requests.post(url, json=myobj)
        return x.json()['projects']

    @commands.command(aliases=['collection'])
    async def nft(self, ctx: utils.CustomContext, *, user: Optional[discord.User]):
        params = ' '.join(ctx.message.content.split()[2:])
        if len(params) == 0:
            await ctx.send('None info provided.')
        else:
            projects = self.get_project_list(params)
            if len(projects) == 0:
                await ctx.send('No match found.')
            else:
                await ctx.send('Matching collections:', view=NFTDropdownView(params, projects, self.api))


async def setup(bot):
    await bot.add_cog(NFTDrop(bot))

import discord
import base64
import datetime
import whois
import aiowiki
import utils
import requests

from typing import Optional, Union

from discord import Color, Member, Role, User
from discord.ext import commands

class GasEth(commands.Cog, name='GasEth'):
    """Gas value for Etherneum."""

    def __init__(self, bot: utils.CustomBot):
        self.bot: utils.CustomBot = bot

    @commands.command(aliases=['fee'])
    async def gas(self, ctx: utils.CustomContext):
        """Shows Gas values."""

        api_key = self.bot.config['ETHERSCAN_API_KEY']
        gas_api = f'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={api_key}'
        gas_value = requests.post(gas_api)
        gas_title = ':fuelpump: Jaki mamy Gas?'
        if gas_value.status_code == 200:
            gas_price = gas_value.json()['result']
            print(f'Gas {gas_price}')
            gas_slow = gas_price['SafeGasPrice']
            gas_midi = gas_price['ProposeGasPrice']
            gas_fast = gas_price['FastGasPrice']

            embed = utils.create_embed(title=gas_title, color='#1ABC9C')
            embed.add_field(name=':turtle: Slow   |   > 10min', value=f'{gas_slow} GWEI', inline=False)
            embed.add_field(name=':person_walking: Avg  |   ~ 3 min', value=f'{gas_midi} GWEI', inline=False)
            embed.add_field(name=':rocket:  Fast  |   < 15 sec', value=f'{gas_fast} GWEI', inline=False)
            await ctx.send(embed=embed)
        else:
            embed = utils.create_embed(title=gas_title, color='#DC143C')
            embed.description = ""
            embed.add_field(name=':disappointed_relieved: Mam problem', value=f'Nie udało się pobrać danych. \nSpróbuj później.', inline=False)
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(GasEth(bot))

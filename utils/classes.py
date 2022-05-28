import discord
import asyncio
import yaml

from discord import Message, User
from discord.ext import commands, menus
from .config import Config

from typing import Union, Optional, Dict, List

__all__ = [
    'CustomContext',
    'CustomBot',
    'CustomMenu',
]


class CustomContext(commands.Context):
    def __init__(self, **attrs):
        super().__init__(**attrs)
        self.bot: CustomBot = self.bot
        self.uncaught_error = False

    async def send(self, *args, **kwargs) -> Message:
        kwargs['reference'] = kwargs.get('reference', self.message.reference)

        return await super().send(*args, **kwargs)

    @property
    def basic_config(self):
        return self.bot.basic_configs.get(self.guild.id, BasicConfig(self.guild))

    @property
    def logging_config(self):
        return self.bot.logging_configs.get(self.guild.id, LoggingConfig(self.guild))


class CustomBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.config = Config()
        self.cogs_list: List[str] = []
        self.fully_ready = False
        self.session = None

    async def setup_hook(self):
        self.loop.create_task(self.startup())

    async def get_context(self, message: Message, *, cls=CustomContext) -> CustomContext:
        return await super().get_context(message, cls=cls)

    async def on_message(self, message):
        print(f'On message: {message}')
        if not self.fully_ready:
            await self.wait_for('fully_ready')
        await self.process_commands(message)

    async def startup(self):
        await self.wait_until_ready()


        self.fully_ready = True
        self.dispatch('fully_ready')

    async def close(self):
        await super().close()

    async def get_owner(self) -> User:
        if not self.owner_id and not self.owner_ids:
            info = await self.application_info()
            self.owner_id = info.owner.id

        return await self.fetch_user(self.owner_id or list(self.owner_ids)[0])

    @staticmethod
    def get_custom_prefix(_bot: 'CustomBot', message: discord.Message):
        return commands.when_mentioned_or('$')(_bot, message)

class CustomMenu(menus.MenuPages):
    @menus.button('\N{WASTEBASKET}\ufe0f', position=menus.Last(3))
    async def do_trash(self, _):
        self.stop()
        await self.message.delete()

    def stop(self):
        self.call_end_event()
        super().stop()

    async def finalize(self, timed_out):
        self.call_end_event()

    def call_end_event(self):
        self.bot.dispatch('finalize_menu', self.ctx)

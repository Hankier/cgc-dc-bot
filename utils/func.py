import time
import datetime
import discord

from discord import Embed, User, Member, Permissions
from typing import Union, Any, Callable, Tuple, List, Coroutine, Optional

__all__ = [
    'create_embed',
    'chunks',
    'fix_url'
]

LOGO        = 'https://i.imgur.com/xVA6z7W.png'
LOGO_SMOL   = 'https://i.imgur.com/uHbOoz4.png'

def create_embed(title: str, color: str, image=None, thumbnail=None) -> Embed:
    """Makes a discord.Embed with options for image and thumbnail URLs, and adds a footer and creator"""

    embed = discord.Embed(title=title, color=discord.Color.from_str(color), timestamp=datetime.datetime.utcnow())
    embed.set_image(url=fix_url(image))

    if thumbnail is not None:
        embed.set_thumbnail(url=fix_url(thumbnail))
    else:
        embed.set_thumbnail(url=fix_url(LOGO_SMOL))
    embed.set_footer(text=f'hqrNFT • Created by Hankier#0001 • hqr.sh ', icon_url=fix_url(LOGO_SMOL))

    return embed

def fix_url(url: Any):
    if not url:
        return None

    return str(url)



def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

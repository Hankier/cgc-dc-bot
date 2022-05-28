import discord
import asyncio
import aiohttp
import utils


cogs = [
    'cogs.info',
    'cogs.gas',
    'cogs.nft',
    'cogs.test',
    'cogs.add_collection',
    'cogs.list'
]


headers = {
    'User-Agent': 'hqrNFT#2712 "A Discord bot"'
}


intents = discord.Intents(
    reactions=True,
    messages=True,
    members=True,
    guilds=True,
    emojis=True,
    bans=True
)


async def startup():
    bot = utils.CustomBot(
        activity=discord.Game(name='hqrNFT'),
        allowed_mentions=discord.AllowedMentions(replied_user=False),
        command_prefix=utils.CustomBot.get_custom_prefix,
        #help_command=utils.CustomHelp(),
        strip_after_prefix=True,
        case_insensitive=True,
        max_messages=20000,
        intents=intents,
    )

    bot.cogs_list = cogs
    for cog in cogs:
        print(f'Cog -> {cog}')
        await bot.load_extension(cog)

    async with aiohttp.ClientSession(headers=headers) as session:
        bot.session = session
        await bot.start(bot.config.dc_token())

if __name__ == '__main__':
    asyncio.run(startup())

import discord
import urllib.parse
import utils

class Collection:
    def __init__(self, data):
        self.db_info = data['project']
        self.opensea = data['opensea']

    def name(self):
        return self.opensea['name']

    def opensea_url(self):
        slug = self.opensea['slug']
        return f'https://opensea.io/collection/{slug}'

    def etherscan(self):
        return self.opensea['primary_asset_contracts'][0]['address']

    def etherscan_url(self):
        return f'https://etherscan.io/address/{self.etherscan()}'

    def description(self):
        return self.opensea['description']

    def logo(self):
        return self.opensea['image_url']

    def banner(self):
        return self.opensea['banner_image_url']

    def site(self):
        return self.opensea['external_url']

    def discord(self):
        return self.opensea['discord_url']

    def twitter(self):
        return self.opensea['twitter_username']

    def twitter_url(self):
        return f'https://twitter.com/{self.opensea["twitter_username"]}'

    def instagram(self):
        return self.opensea['instagram_username']

    def instagram_url(self):
        return f'https://www.instagram.com/{self.instagram()}'

    def supply(self):
        return self.opensea['stats']['total_supply']

    def owners(self):
        return self.opensea['stats']['num_owners']

    def floor(self):
        return self.opensea['stats']['floor_price']

    def sales(self):
        return self.opensea['stats']['total_sales']

    def volume(self):
        return f"{round(self.opensea['stats']['total_volume'], 2)}Eth"

    def average_price(self):
        return f"{round(self.opensea['stats']['average_price'], 2)}Eth"

    def dashboard(self):
        params = {
                'orgId': 1,
                'from': 'now-2d',
                'to': 'now',
                'var-collection': f'{self.name()}'
                }
        params_str = urllib.parse.urlencode(params)
        dashboard = f'http://stats.coolguys.space/d/5WEccYunk/stats-of-colletions?{params_str}'

        return dashboard

    def embed(self):
        embed_color = discord.Color.green()
        embed = utils.create_embed(title=self.name(), color='#cc00ff', image=self.banner(), thumbnail=self.logo())
        embed.description = self.description()
        embed.add_field(name="Opensea", value=f'[{self.name()}]({self.opensea_url()})', inline=True)
        embed.add_field(name="Etherscan", value=f'[{self.etherscan()}]({self.etherscan_url()})', inline=True)

        if self.site():
            embed.add_field(name="Site", value=f'[{self.site()}]({self.site()})', inline=True)
        else:
            embed.add_field(name="Site", value=f'None', inline=True)

        if self.twitter():
            embed.add_field(name="Twitter", value=f'[{self.twitter()}]({self.twitter_url()})', inline=True)
        else:
            embed.add_field(name="Twitter", value=f'None', inline=True)

        if self.discord():
            embed.add_field(name="Discord", value=f'[{self.discord()}]({self.discord()})', inline=True)
        else:
            embed.add_field(name="Discord", value=f'None', inline=True)

        if self.instagram():
            embed.add_field(name="Instagram", value=f'[{self.instagram()}]({self.instagram_url()})', inline=True)
        else:
            embed.add_field(name="Instagram", value=f'None', inline=True)

        embed.add_field(name="Supply", value=f'{self.supply()}', inline=True)
        embed.add_field(name="Owners", value=f'{self.owners()}', inline=True)
        embed.add_field(name="Floor", value=f'{self.floor()}', inline=True)
        embed.add_field(name="Sales", value=f'{self.sales()}', inline=True)
        embed.add_field(name="Volume", value=f'{self.volume()}', inline=True)
        embed.add_field(name="Avg Sale Price", value=f'{self.average_price()}', inline=True)
        embed.add_field(name="Dashboard", value=f'[Dashboard for {self.name()}]({self.dashboard()})', inline=False)
        return embed

def fix_url(url):
    if not url:
        return None

    return str(url)

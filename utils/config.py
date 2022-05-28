from dotenv import dotenv_values

__all__ = [
    'Config'
]

class Config():
    def __init__(self, ):
        self.config = dotenv_values(".env")

    def hqr_api(self):
        return self.config['HQRNFT_API_URL']

    def etherscan_api_key(self):
        return self.config['ETHERSCAN_API_KEY']

    def dc_token(self):
        return self.config['BOT_DC_TOKEN']


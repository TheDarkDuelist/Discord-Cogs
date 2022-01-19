import configparser
from binance.spot import Spot as BNB
from discord.ext import commands

config = configparser.ConfigParser()
config.read(r"C:\Users\TESTBENCH\Documents\Python Projects\Discord Tutorial Bot\config.ini")
key_bnb = config["BINANCE"]
base_url = key_bnb["BASE_URL"]
spot_client = BNB(base_url)

def crypto_price(ticker, decimals):
    pair_info = spot_client.ticker_price(ticker)
    pair_values = pair_info.values()
    values_list = list(pair_values)
    the_price = round(float(values_list[1]), decimals)
    return the_price

class priceCrypto(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def price(self, ctx, *, args):
        coin = args.split(' ')
        currency = coin[0]
        if currency.lower() == 'bitcoin':
            symbol, ticker = 'BTC', 'BTCUSDT'
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
    
    def setup(client):
        client.add_cog(priceCrypto(client))
    
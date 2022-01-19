from discord.ext import commands
import configparser
from binance.spot import Spot as Client
import math
import urllib.request, json
from discord.ext.commands.errors import CheckFailure

configs = configparser.ConfigParser()
configs.read(r'C:\Users\TESTBENCH\Documents\Python\config.ini')
key_binance = configs['BINANCE']
base_url = key_binance["BINANCE_API"]
spot_client = Client(base_url)

def crypto_price(ticker, decimals):
    pair_info = spot_client.ticker_price(ticker)
    pair_values = pair_info.values()
    valuesList = list(pair_values)
    the_price = round(float(valuesList[1]), decimals)
    return the_price

class priceCrypto(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_any_role("Nobles", "Elders", "Admin")
    async def price(self, ctx, *, args):
        coin = args.split(' ')
        currency = coin[0]
        if currency.lower() == "btc" or currency.lower() == "bitcoin":
            if currency.lower() == "bitcoin":
                try:
                    if coin[1].lower() == "cash":
                        symbol, ticker = "BCC", "BCCUSDT"
                        the_price = crypto_price(ticker, 2)
                        await ctx.send(f"{symbol}: ${str(the_price)}")
                        return
                except:
                    symbol, ticker = "BTC", "BTCUSDT"
                    the_price = crypto_price(ticker, 2)
                    await ctx.send(f"{symbol}: ${str(the_price)}")
                    return
            symbol, ticker = "BTC", "BTCUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "eth" or currency.lower() == "ethereum":
            try:
                if coin[1].lower() == "classic":
                    symbol, ticker = "ETC", "ETCUSDT"
                    the_price = crypto_price(ticker, 2)
                    await ctx.send(f"{symbol}: ${str(the_price)}")
                    return
            except:
                symbol, ticker = "ETH", "ETHUSDT"
                the_price = crypto_price(ticker, 2)
                with urllib.request.urlopen("https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=TV284S8URNDMWPY5DQ7WFKTGSWANNA2DEH") as url:
                    data = json.loads(url.read().decode())
                    values = list(data.values())
                    gasPrice = list(values[2].values())
                    slowPrice = (int(gasPrice[1]) * 21000 * math.pow(10, -9)) * the_price
                    slow = round(slowPrice, 2)
                    averagePrice = (int(gasPrice[2]) * 21000 * math.pow(10, -9)) * the_price
                    average = round(averagePrice, 2)
                    fastPrice = (int(gasPrice[3]) * 21000 * math.pow(10, -9)) * the_price
                    fast = round(fastPrice, 2)
                await ctx.send(f"{symbol}: ${str(the_price)}\nGas Price (gwei/$)\nSlow: {str(gasPrice[1])}/${str(slow)}\nAverage: {str(gasPrice[2])}/${str(average)}\nFast: {str(gasPrice[3])}/${str(fast)}")
                return
        if currency.lower() == "avax" or currency.lower() == "avalanche":
            symbol, ticker = "AVAX", "AVAXUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "bnb" or currency.lower() == "binance" or currency.lower() == "binancecoin":
            symbol, ticker = "BNB", "BNBUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "etc" or currency.lower() == "ethereuemclassic":
            symbol, ticker = "ETC", "ETCUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "bcc":
            symbol, ticker = "BCC", "BCCUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "vet" or currency.lower() == "vechain":
            symbol, ticker = "VET", "VETUSDT"
            the_price = crypto_price(ticker, 6)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "xmr" or currency.lower() == "monero":
            symbol, ticker = "XMR", "XMRUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "ltc" or currency.lower() == "litecoin":
            symbol, ticker = "ltc", "LTCUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "doge" or currency.lower() == "dogecoin":
            symbol, ticker = "DOGE", "DOGEUSDT"
            the_price = crypto_price(ticker, 4)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "rvn" or currency.lower() == "ravencoin" or currency.lower() == "raven":
            symbol, ticker = "RVN", "RVNUSDT"
            the_price = crypto_price(ticker, 4)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "ada" or currency.lower() == "cardano":
            symbol, ticker = "ADA", "ADAUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "coti":
            symbol, ticker = "COTI", "COTIUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "xrp" or currency.lower() == "ripple":
            symbol, ticker = "XRP", "XRPUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "sol" or currency.lower() == "solana":
            symbol, ticker = "SOL", "SOLUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "aave":
            symbol, ticker = "AAVE", "AAVEUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "1inch" or currency.lower() == "inch":
            symbol, ticker = "1INCH", "1INCHUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "iota" or currency.lower() == "miota":
            symbol, ticker = "IOTA", "IOTAUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "shib" or currency.lower() == "shiba" or currency.lower() == "shibainu":
            symbol, ticker = "SHIB", "SHIBUSDT"
            the_price = crypto_price(ticker, 8)
            await ctx.send(f"{symbol}: ${str('{0:.8f}'.format(the_price))}")
            return
        if currency.lower() == "xlm" or currency.lower() == "stellar" or currency.lower() == "stellarlumens":
            symbol, ticker = "XLM", "XLMUSDT"
            the_price = crypto_price(ticker, 4)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "pols" or currency.lower() == "polkastarter":
            symbol, ticker = "POLS", "POLSUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "dot" or currency.lower() == "polkadot":
            symbol, ticker = "DOT", "DOTUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "matic" or currency.lower() == "polygon":
            symbol, ticker = "MATIC", "MATICUSDT"
            the_price = crypto_price(ticker, 2)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "one" or currency.lower() == "harmony" or currency.lower() == "harmonyone":
            symbol, ticker = "ONE", "ONEUSDT"
            the_price = crypto_price(ticker, 4)
            await ctx.send(f"{symbol}: ${str(the_price)}")
            return
        if currency.lower() == "help":
            await ctx.send("My human adds cryptos manually. If there is not one on the list that you would like added, please pm him the coin and he will try to find the binance ticker for it. All coins currently are search as <coin>/USDT for price. Below is a list of currently supported coins.\n"\
                "Bitcoin, Avalanche, Ethereum, Binance Coin, Ethereum Classic, Bitcoin Cash, VeChain, Monero, Litecoin, Dogecoin, Ravencoin, Shiba Inu, Stellar Lumens, Polkastarter, Polkadot, Matic/Polygon and Harmony One")
            return
        else:
            msg = "Sorry, that crypto may not currently be supported. Please use '-price help' for a current list."
            await ctx.send(msg)
            return
    
    @price.error
    async def price_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            msg = "Sorry but that feature is only for subscribed members."
            await ctx.send(msg)
            return

    def setup(client):
        client.add_cog(priceCrypto(client))
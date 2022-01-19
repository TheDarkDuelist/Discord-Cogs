from binance.spot import Spot as Client
import pandas as pd

base_url = "https://api.binance.com"

spot_client = Client(base_url)
#coin_price with coin-usdt marker
btcusd_price = spot_client.ticker_price('BTCUSDT')
#need to get values of the dictionary created above
values = btcusd_price.values()
#need to list the values created above
valuesList = list(values)
#the value we want is in the 1st index
print(valuesList[1])
path = r'yourfilepath\symbols.csv'
exchange_info = spot_client.exchange_info()
symbols = pd.DataFrame(exchange_info['symbols'])
symbolList = symbols.to_csv(path, columns=['symbol'], index=False)
print(symbolList)
symbolsToAdd = ['BTCUSDT','AVAXUSDT','ETHUSDT','BNBUSDT','ETCUSDT','BCCUSDT','VETUSDT','XMRUSDT',\
   'LTCUSDT','DOGEUSDT','RVNUSDT','ADAUSDT','COTIUSDT','XRPUSDT','SOLUSDT','AAVEUSDT','1INCHUSDT',\
      'IOTAUSDT','SHIBUSDT','XLMUSDT','POLSUSDT','DOTUSDT','MATICUSDT']
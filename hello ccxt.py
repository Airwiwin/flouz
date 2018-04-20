import ccxt
# print(ccxt.ex) # print a list of all available exchange classes

# Load the poloniex exhange. There is
# limited functionality available with the
# public API where you don't need to key e.g
# we can query the exchanges's state. We
# can't place trades without setting up a key
# and passing this to ccxt.
poloniex = ccxt.poloniex()
poloniex.load_markets()

# poloniex.markets is just a massive
# dictionary, so we could access all of the
# keys via poloniex.markets.keys() to see
# all of the available markets in poloniex.
# Alternatively you could just print out
# poloniex.markets, but be warned there is a
# lot of data!
print(poloniex.markets['ETC/BTC'])

#-------------------------------------------
# Expected Output:
#-------------------------------------------
#
# {'base': 'ETC',
#  'id': 'BTC_ETC',
#  'info': {'baseVolume': '520.62905349',
#           'high24hr': '0.00161111',
#           'highestBid': '0.00137092',
#           'id': 171,
#           'isFrozen': '0',
#           'last': '0.00137568',
#           'low24hr': '0.00129881',
#           'lowestAsk': '0.00137561',
#           'percentChange': '-0.13766149',
#           'quoteVolume': '353091.22875089'},
#  'limits': {'amount': {'max': 1000000000, 
#                        'min': 1e-08},
#  'cost': {'max': 1000000000, 
#           'min': 0.0},
#  'price': {'max': 1000000000, 
#            'min': 1e-08}},
#  'maker': 0.0015,
#  'precision': {'amount': 8, 
#                'price': 8},
#  'quote': 'BTC',
#  'symbol': 'ETC/BTC',
#  'taker': 0.0025}
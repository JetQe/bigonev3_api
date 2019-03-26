from bigonev3 import TradeApi
import config

api = TradeApi(config.API_KEY, config.API_SECRET)

a = 2

if a == 1:
    # getServerTimestamp
    print ("====getServerTimestamp=====")
    print (api.getServerTimestamp())

    # getMarketTicker
    print ("====getMarketTicker=====")
    print (api.getMarketTicker('BTC-USDT'))

    # getMarketDepth
    print ("====getMarketDepth=====")
    print (api.getMarketDepth('BTC-USDT'))

    # getMarketDepth
    print ("====getMarketDepth=====")
    print (api.getMarketDepth('BTC-USDT', 100))

    # getCandles
    print ("====getCandles=====")
    print (api.getCandles('BTC-USDT', 'day1'))

    # getAssets
    print ("====getAssets=====")
    print (api.getAssets())

    # getBalances
    print ("====getBalances=====")
    print (api.getBalances())

    # getOneBalance
    print ("====getOneBalance=====")
    print (api.getOneBalance('USDT'))

else:

    # createOrder
    print ("====createOrder=====")
    print (api.createOrder('PRS-USDT','ASK','0.054','20'))
    # getOrders
    print ("====getOrders=====")
    print (api.getOrders('PRS-USDT'))

    # getOrder
    #print ("====getOrder=====")
    #print (api.getOrder('569192385'))

    # cancelOrder
    #print ("====cancelOrder=====")
    #print (api.cancelOrder('571415739'))

    # cancelOrders
    print ("====cancelOrders=====")
    print (api.cancelOrders('PRS-USDT'))

    # getMyTrades
    print ("====getMyTrades=====")
    print (api.getMyTrades('PRS-USDT'))

    #print (api.getMyTrades('PRS-USDT', '1', '10'))

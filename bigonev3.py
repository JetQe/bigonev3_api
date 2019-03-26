# encoding: utf-8

'''
Exin Tech
'''

import urllib
import requests 
import time
import json
import jwt

# constant
TIMEOUT = 30
BIGONE_API_HOST = "big.one/api/v3"


#----------------------------------------------------------------------
def createJwt(api_key, secret_key):
    """signature"""

    ts = int(1000000000 * time.time())
    payload = {
          "type": "OpenAPI",
          "sub": api_key,
          "nonce": ts
    }
    encoded = jwt.encode(payload, secret_key, algorithm='HS256')
    return encoded 


########################################################################
class TradeApi(object):
    

    #----------------------------------------------------------------------
    def __init__(self, api_key="", api_secret=""):
        """init"""

        self.api_key = api_key
        self.api_secret = api_secret
        self.hosturl = 'https://%s' %BIGONE_API_HOST
    
    #----------------------------------------------------------------------    
    def http(self, url, params, headers, method):
        """http request"""

        try:
	    if method == 'POST' and url == 'https://big.one/api/v3/viewer/orders':	
	    	response = requests.post(url, data=json.dumps(params), headers=headers,  timeout=TIMEOUT)
	    else:
	    	response = requests.request(method, url, params=params, headers=headers,  timeout=TIMEOUT)
            if response.status_code == 200:
                return True, response.json()
            else:
                return False, u'Request Fail, Status Code：%s' %response.status_code
        except Exception as e:
            return False, u'Request exception: %s' %e

    #----------------------------------------------------------------------
    def addReq(self, path, params, signiture, method):
        """redirect"""

	    headers = {'Content-Type': 'application/json'}
        if signiture:
            token = createJwt(self.api_key, self.api_secret)
            headers['Authorization'] =  'Bearer {}'.format(token)
        url = self.hosturl + path
        return self.http(url, params, headers, method)
    
    #----------------------------------------------------------------------
    def getBalances(self):
        """all assets balances"""

        path = '/viewer/accounts'
        params = {}
        return self.addReq(path, params, True, 'GET')

    #----------------------------------------------------------------------
    def getOneBalance(self, symbol):
        """one asset balance"""

        path = '/viewer/accounts/'+symbol
        params = {
	    'asset_symbol': symbol
	    }
        return self.addReq(path, params, True, 'GET')

    #----------------------------------------------------------------------
    def createOrder(self, symbol, side, price, amount):
        """create an order"""

        path = '/viewer/orders'
        params = {
            'asset_pair_name': symbol,
            'price': price,
            'side': side,
            'amount': amount
        }
        return self.addReq(path, params, True, 'POST')           

    #----------------------------------------------------------------------
    def getOrders(self, symbol, page_token=None, side=None, state=None, limit=None):
        """one asset orders"""

        path = '/viewer/orders'
        params = {
            'asset_pair_name': symbol
	    }
        if page_token:
            params['page_token'] = page_token
        if side:
            params['side'] = side
        if state:
            params['state'] = state
        if limit:
            params['limit'] = limit
        return self.addReq(path, params, True, 'GET')             

    #----------------------------------------------------------------------
    def getOrder(self, orderId):
        """get order from id"""

        path = '/viewer/orders/'+orderId
        return self.addReq(path, {}, True, 'GET')

    #----------------------------------------------------------------------
    def cancelOrder(self, orderId):
        """cancel an order"""

        path = '/viewer/orders/'+orderId+'/cancel'
        params = {
            'id': orderId
        }
        return self.addReq(path, params, True, 'POST') 

    #----------------------------------------------------------------------
    def cancelOrders(self, symbol):
        """cancel orders of one asset"""

        path = '/viewer/orders/cancel'
        params = {
            'asset_pair_name': symbol
        }
        return self.addReq(path, params, True, 'POST') 

    #----------------------------------------------------------------------
    def getMyTrades(self, symbol, page_token= None, limit=None):
        """trades of user"""

        path = '/viewer/trades'
        params = {
            'asset_pair_name': symbol
        }
        if page_token:
            params['page_token'] = page_token
        if limit:
            params['limit'] = limit
        return self.addReq(path, params, True, 'GET')

    #----------------------------------------------------------------------
    def getAssets(self):
        """Assets"""

        path = '/asset_pairs'
        return self.addReq(path, {}, False, 'GET')

    #----------------------------------------------------------------------
    def getCandles(self, symbol, period, limit=None):
        """ohlc candles"""  

	    path = '/asset_pairs/'+symbol+'/candles'
        params = {
	        "period": period
        }
        if limit:
            params['limit'] = limit
        return self.addReq(path, params, False, 'GET')

    #----------------------------------------------------------------------
    def getMarketDepth(self, symbol, limit=None):
        """orderbook"""

	    path = '/asset_pairs/'+symbol+'/depth'
	    if limit:
            params['limit'] = limit
        return self.addReq(path, {}, False, 'GET')

    #----------------------------------------------------------------------
    def getMarketTicker(self, symbol):
        """ticker"""

        path = '/asset_pairs/'+symbol+'/ticker'
        return self.addReq(path, {}, False, 'GET')
    
    #----------------------------------------------------------------------
    def getServerTimestamp(self):
        """server timestamp"""

        path = '/ping'
        return self.addReq(path, {}, False, 'GET')

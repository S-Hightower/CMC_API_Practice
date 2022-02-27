import requests
from requests import Session
import secrets
from pprint import pprint as pp

# Reference API
#https://coinmarketcap.com/api/documentation/v1/
class CMC:

    def __init__(self, token):
        self.apiurl = 'https://pro-api.coinmarketcap.com'
        self.headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': token}
        self.Session = Session()
        self.Session.headers.update(self.headers)

    def getAllCoins(self):
        url = self.apiurl + '/v1/cryptocurrency/map'
        r = self.Session.get(url)
        data = r.json()['data']
        return data

    def getPrice(self,symbol):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'symbol': symbol}
        r = self.Session.get(url, params=parameters)
        data = r.json()['data']
        return data

    def getPriceByName(self,slug):
        url = self.apiurl + '/v1/cryptocurrency/quotes/latest'
        parameters = {'slug': slug}
        r = self.Session.get(url, params=parameters)
        data = r.json()['data']
        return data

    def getMetadata(self,slug):
        url = self.apiurl + '/v1/cryptocurrency/info'
        parameters = {'slug': slug}
        r = self.Session.get(url, params=parameters)
        data = r.json()['data']
        return data

cmc = CMC(secrets.API_KEY)

# TEST CASES
# pp(cmc.getPrice('ETH'))
# pp(cmc.getPriceByName('ethereum'))
# pp(cmc.getMetadata('bitcoin'))
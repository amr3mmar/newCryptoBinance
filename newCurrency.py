import requests
from utils import setInterval, beep

def checkCryptoListing():
    base_url = "https://api.binance.com"
    response = requests.get(base_url + '/api/v3/ticker/price').json()
    result = []
    for i in response:
        result.append(i['symbol'])
    return result

def checkNewCrypto():
    currentListing = checkCryptoListing()
    currentListingLen = len(currentListing)
    if not currentListingLen==oldListingLen:
        newCurrencies = list(set(currentListing) - set(oldListing))
        print(newCurrencies)
        beep()
    

oldListing = checkCryptoListing()
oldListingLen = len(oldListing)
print(oldListingLen)
setInterval(checkNewCrypto, 5)
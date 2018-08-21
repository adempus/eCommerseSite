import requests
from .shopdatabase import ShopDatabase


class ShopDAO(object):
    def __init__(self):
        self._database = ShopDatabase()
        self.status()

    def addNewUser(self, userModel):
        # self._database.Persistence.persistNewUser(userModel)
        pass

    def addNewProduct(self, productModel):
        pass
        # self._database.Persistence.persistNewProduct(productModel)

    def status(self):
        print('Database initiated')


class LocationDAO(object):
    def __init__(self):
        self._allCountriesURL = 'https://restcountries.eu/rest/v2/all?fields=name;'
        self._allStatesURL= 'http://api.geonames.org/childrenJSON?'
        self._allCitiesURL = ''

    def _getJsonResponse(self, url):
        return requests.get(url).json()

    def countriesList(self):
        data = self._getJsonResponse(self._allCountriesURL)
        return [x['name'] for x in data]

    def statesList(self, country):
        geonameId = self.getGeonameId(country)
        url = f'{self._allStatesURL}geonameId={geonameId}&username=jmorin722'
        gname = self.hasGeoname(self._getJsonResponse(url))
        if gname: return [x['name'] for x in gname]
        else:return None

    def getGeonameId(self, countryName):
        geonameURL = f'http://api.geonames.org/searchJSON?q={countryName}&maxRows=10&username=jmorin722'
        gname = self.hasGeoname(self._getJsonResponse(geonameURL))
        if gname: return [x['geonameId'] for x in gname if x['name'] in countryName].pop()
        else: return None

    def citiesList(self, region):
        ''':param region can be a state or some other classification of region. '''

    def hasGeoname(self, jsonResponse):
        # print(jsonResponse)
        if 'geonames' in jsonResponse:
            return jsonResponse['geonames']


if '__main__'==__name__:
    locdao = LocationDAO()
    print(locdao.countriesList())
    # res = locdao.getGeonameId('united states of america')['geonames']
    # target = [x['geonameId'] for x in res if x['name'] in 'United States of America']
    print(locdao.statesList('Canada'))


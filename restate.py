import requests
import xml.etree.ElementTree as et 
from geopy.geocoders import Nominatim as nom

class API_Data():
    def __init__(self):
        self.base_url = 'http://www.zillow.com/webservice/GetRegionChildren.htm'
        with open('Zillow_API_Key.txt','r') as file:
            self.zwsid = file.read()
            print(self.zwsid)
        self.citystate = [['Chicago','IL'],['Seattle','WA'],['Portland','OR']]
        self.loc_sample()
        #self.request_data()

    def loc_sample(self):
        geolocator = nom(user_agent='real_estate')
        location = geolocator.reverse('41.8781, -87.6298')
        print(location.address)


    def request_data(self):
        params = {'zws-id':self.zwsid,'state':self.citystate[0][1],
                  'city':self.citystate[0][0],'childtype':'neighborhood'}
        self.data = requests.get(url=self.base_url,params=params)
        self.root = et.fromstring(self.data.text)
        self.head = self.root[2][2] 
        for region in self.head.findall('region'):
            self.parse_data(region)
        #print(self.data.text)

    def parse_data(self,region):
        categories = ['name','zindex','latitude','longitude']
        for value in categories:
            for elem in region.findall(value):
                print(elem.text)

if __name__ == '__main__':
    API_Data()
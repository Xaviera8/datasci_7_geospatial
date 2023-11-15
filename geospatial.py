import requests
import urllib.parse

api_key = 'AIzaSyCWX6hvR2Nf4GF8JqIbaLrrA5DEEkvVMdM'

# url for the api we are using, it requires certain arguments
search = 'https://maps.googleapis.com/maps/api/geocode/json?address='

#location argument we will pass into our api
location_raw = '97 catherine street valley stream ny'

#this removes any whitespace so that it can be properly read inside a url
location_clean = urllib.parse.quote(location_raw)

#adding the nessecary arguments into one variable
url_requests_part1 = search + location_clean + '&key=' + api_key
url_requests_part1

response = requests.get(url_requests_part1)

response.text

response_dictionary = response.json()

response_dictionary.keys()
response_dictionary['status']

#This looks through the dictionary response_dictionary and finds the value for the key results. It then finds the first item in list of values 
#with the 0. The first item in that list provides another list which the key geometry is accessed through

response_dictionary['results'][0]['geometry']['location']
lat_long = response_dictionary['results'][0]['geometry']['location']
lat_long

#Returns the value for the provided key 'lat' in the dictionary lat_long
lat = lat_long['lat']
lat

#Returns the value for the provided key 'lng' in the dictionary lat_long
long = lat_long['lng']
long

# I STOPPED MY VIDEO AT 2:06:45

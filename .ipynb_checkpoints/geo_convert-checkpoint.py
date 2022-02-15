from opencage.geocoder import OpenCageGeocode
from geopy.geocoders import OpenCage
import time


api_key = ''
try:
    with open("geocode.ini") as f:
        information = f.read()
        api_key = information.split(": ")[1]
except:
    api_key = ''
    print("No api-key found!")

def geocode_address(address: dict) -> tuple:
    """
    Lookup coordinates from a postal address.
    
    :param address: A dictonary containing the address of the place including street, number, zip-code, city country
    :return: A tupel containing the coordinates. (longitude, latitude)
    """
    geocoder = OpenCage(api_key=api_key)
    query = '%s %s, %s %s, %s' % (address["street"], address["number"], address["zip_code"], address["city"], address["country"])
    # print(query)
    coordinates = geocoder.geocode(query=query, exactly_one=True)
    time.sleep(1)
    # print(coordinates)
    return coordinates.latitude, coordinates.longitude
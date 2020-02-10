from pymongo import MongoClient
import pandas as pd
import json as js

def asGeoJSON(lat,lng):
    '''function to apply to latitude and longitude series to create a new column with a JSON 'point'''
    lat = float(lat)
    lng = float(lng)
    return {
        "type":"Point",
        "coordinates":[lng,lat]
    }

client = MongoClient("mongodb://localhost/companies")
db = client.get_database()

def officesComp(coord, bd, meters):
    '''Function to know distance from office to old company, starbucks, airport, bar, etc...'''
    coordinates = coord['coordinates']
    comp = (db[f'{bd}'].aggregate([{'$geoNear': {'near': { 'type': "Point", 'coordinates': coordinates },
        'distanceField': "dist.calculated",
        'maxDistance': meters,
        'spherical': 'true'}}]))
    officescomp = len(list(comp))
    return officescomp


def nearestStarbucks(lat, long, cd):
    '''Function to know distance from office to starbucks'''
    coordinates = cd['location'][0]['coordinates']
    near = (db['starbucks'].aggregate([{'$geoNear': {'near': { 'type': "Point", 'coordinates': coordinates },
        'distanceField': "dist.calculated",
        'maxDistance': 500,
        'spherical': 'true'}}]))
    nearest = []
    for d in near:
        nearest.append((d['Latitude'],d['Longitude']))
    return nearest

def nearestAirports(lat, long, cd):
    '''Function to know distance from office to airport'''
    coordinates = cd['location'][0]['coordinates']
    near = (db['airports'].aggregate([{'$geoNear': {'near': { 'type': "Point", 'coordinates': coordinates },
        'distanceField': "dist.calculated",
        'maxDistance': 10000,
        'spherical': 'true'}}]))
    nearest = []
    for d in near:
        nearest.append((d['latitude_deg'],d['longitude_deg']))
    return nearest

def nearestComp(lat, long, cd):
    '''Function to know distance from office to old company'''
    coordinates = cd['location'][0]['coordinates']
    near = (db['oldestOffices'].aggregate([{'$geoNear': {'near': { 'type': "Point", 'coordinates': coordinates },
        'distanceField': "dist.calculated",
        'maxDistance': 2000,
        'spherical': 'true'}}]))
    nearest = []
    for d in near:
        nearest.append((d['latitude'],d['longitude']))
    return nearest

def requestMap(lat, long):
    '''Requesting nearby night clubs to offices'''
    token = os.getenv('MAPS_KEY')
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key={token}&location={lat},{long}&radius=1000&type=night_club'
    res = requests.get(url)
    if res.status_code != 200:
        raise ValueError('Bad Response: {}'.format(res.status_code))
    return res.json()

import requests

overpass_url = 'https://overpass-api.de/api/interpreter'
overpass_query = '''
[out:json];
area[name="Zürich"][place="city"];
node[amenity="toilets"](area);
out;
'''

response = requests.get(overpass_url, params={'data': overpass_query})

'''
python3 ExampleNo01.py

https://pybit.es/articles/openstreetmaps-overpass-api-and-python/
'''
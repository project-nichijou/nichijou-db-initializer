from database.database import NichijouDatabase

import json
import requests


data = requests.get('https://cdn.jsdelivr.net/gh/project-nichijou/nichijou-db-essential@latest/data.json')
data = json.loads(data.text)['data']

database = NichijouDatabase()

for key in data.keys():
	names = data[key]
	nid = int(key)
	for name in names:
		database.write('anime_name', {
			'nid': nid,
			'name': name
		})

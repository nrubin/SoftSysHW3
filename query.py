"""
Path from Meg Ryan to Kevin Bacon

MATCH p=shortestPath( (bacon:Person {name:"Kevin Bacon"})-[*]-(meg:Person {name:"Meg Ryan"}) ) RETURN p

Get a node with a given name
MATCH (n {name: "Kevin Bacon"}) RETURN n
"""

import requests
import json

def bacon_path():
	data = {
	  "to" : "http://localhost:7474/db/data/node/210",
	  "max_depth" : 10,
	  "algorithm" : "shortestPath"
	}

	r2 = requests.post("http://localhost:7474/db/data/node/195/path", data=json.dumps(data))
	print r2.text
	# print r2.json()

def get_node_url(name):
	data = {
	"query" : "MATCH (n {name: {name}}) RETURN n",
	"params": {
		"name" : name
		}
	}
	r = requests.post("http://localhost:7474/db/data/cypher", data=json.dumps(data))
	return r.json()["data"][0][0]["self"]

if __name__ == '__main__':
	bacon_path()
	print get_node_url("Kevin Bacon")
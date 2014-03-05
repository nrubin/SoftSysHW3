"""
Path from Meg Ryan to Kevin Bacon

MATCH p=shortestPath( (bacon:Person {name:"Kevin Bacon"})-[*]-(meg:Person {name:"Meg Ryan"}) ) RETURN p

Get a node with a given name
MATCH (n {name: "Kevin Bacon"}) RETURN n
"""

import requests
import json

def get_shortest_path(origin_node,destination_node,max_depth=10):
	"""
	Takes an origin node URL and a destination node URL and returns the list of node URLs that connect
	the two nodes, including the origin and destination nodes.
	Args:
		origin_node: string, the url of the origin node (e.g. http://localhost:7474/db/data/node/195)
		destination_node: string, the url of the destination node
	Returns:
		A dictionary containing the nodes in the path, the edges in the path, the path length, and the start and end of the path
	"""
	data = {
	  "to" : destination_node,
	  "max_depth" : max_depth,
	  "algorithm" : "shortestPath"
	}
	url = origin_node + "/path"
	response = requests.post(url, data=json.dumps(data))
	return response.json()

def get_node_url(name):
	"""
	Gets the url of a node based on the actor's name
	Args:
		name: string, the actor's name (case sensitive)
	Returns:
		The URL of the node as a string
	"""
	data = {
	"query" : "MATCH (n {name: {name}}) RETURN n",
	"params": {
		"name" : name
		}
	}
	r = requests.post("http://localhost:7474/db/data/cypher", data=json.dumps(data))
	return r.json()["data"][0][0]["self"]

if __name__ == '__main__':
	th_url = get_node_url("Meg Ryan")
	kb_url = get_node_url("Kevin Bacon")
	print get_shortest_path(th_url,kb_url)
'''
API Data Layer for Querying


'''
from quart import Quart, jsonify, render_template
from pymemgraph import MemgraphClient
import json
from typing import List, Dict

import os

app = Quart(__name__)
memgraph = MemgraphClient(host="ocalhost", port=7687)
BASE_URL="http://localhost:3000/api/v1"
@app.route(os.path.join(BASE_URL,'/'))

@app.route('/')
async def index():
    return await render_template('index.html')

async def get_graph():
    query="""
    MATCH (n)
    OPTIONAL MATCH (n)-[r]->[m]
    return n, r, m
    """
    results = await memgraph.execute(query)
    
    nodes = {}
    links = []
        
    for record in results:
        source = record['n']
        if source['id'] not in nodes:
            nodes[source['id]]']] = {
                'id': source['id'],
                'label': source.get('name', source['id']),
                'type': source['type'],
                'metadata': {
                    k: v for k, v in source.items()
                    if k not in ['id','name','type']
                }
            }

        if record['r'] and record['m']:
            target = record['m']
            if target['id'] not in nodes:
                nodes[target['id']] = {
                    'id': target['id'],
                    'label': target.get('name', target['id']),
                    'type': target['type'],
                    'metadata': {
                        k: v for k, v in target.items()
                        if k not in ['id','name','type']
                    }
            }  
                
                links.append({
                'source': source['id'],
                'target': target['id'],
                'type': type(record['r']).__name__,
                'metadata': {
                    k: v for k, v in record['r'].items()
                    if k not in ['source', 'target', 'type']
                }
            })
        return jsonify({
            'nodes':List(nodes.values()),
            "links": links,
        })
            
if __name__ == '__main__':
    app.run()

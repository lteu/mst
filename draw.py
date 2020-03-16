import networkx as nx
import csv
import time
import sys
import pandas as pd
import plotly.graph_objects as go


def loadMst(numb):
	matrix = []
	with open('csv-mst/'+str(numb)+'.csv') as csvfile:
		valreader = csv.reader(csvfile, delimiter=',')
		for row in valreader:
			aRow = []
			for x in row:
				aRow.append(float(x))
			matrix.append(aRow)
	return matrix

def addNodesToG(G, arr):
	for x in range(len(arr)):
		nd = x
		G.add_node(nd)
	return G

def addEdgesToG(G, arr):
	for x in range(len(arr)):
		for y in range(len(arr[x])):
			if arr[x][y] != 0:
				G.add_edge(x,y)
	return G

def posToNodeTrace(G,pos):
	node_x = []
	node_y = []
	for node in G.nodes():
	    x, y = pos[node]
	    node_x.append(x)
	    node_y.append(y)

	node_trace = go.Scatter(
	    x=node_x, y=node_y,
	    mode='markers',
	    hoverinfo='text',
	    marker=dict(
	        showscale=True,
	        colorscale='YlGnBu',
	        reversescale=True,
	        color=[],
	        size=10,
	        colorbar=dict(
	            thickness=15,
	            title='Node Connections',
	            xanchor='left',
	            titleside='right'
	        ),
	        line_width=2))
	return node_trace

def posToNodeTraceWithIsolates(G,pos,isolates):
	node_x = []
	node_y = []
	for node in G.nodes():
		if node in isolates:
			continue
		x, y = pos[node]
		node_x.append(x)
		node_y.append(y)
	# print(node_x,isolates)
	# sys.exit()
	node_trace = go.Scatter(
	    x=node_x, y=node_y,
	    mode='markers',
	    hoverinfo='text',
	    marker=dict(
	        showscale=True,
	        colorscale='YlGnBu',
	        reversescale=True,
	        color=[],
	        size=10,
	        colorbar=dict(
	            thickness=15,
	            title='Node Connections',
	            xanchor='left',
	            titleside='right'
	        ),
	        line_width=2))
	return node_trace


def posToEdgeTrace(G,pos):
	edge_x = []
	edge_y = []
	for edge in G.edges():
	    x0, y0 = pos[edge[0]]
	    x1, y1 = pos[edge[1]]
	    edge_x.append(x0)
	    edge_x.append(x1)
	    edge_x.append(None)
	    edge_y.append(y0)
	    edge_y.append(y1)
	    edge_y.append(None)

	edge_trace = go.Scatter(
	    x=edge_x, y=edge_y,
	    line=dict(width=0.5, color='#888'),
	    hoverinfo='none',
	    mode='lines')
	return edge_trace

def adjInfo(G):
	node_adjacencies = []
	node_text = []
	for node, adjacencies in enumerate(G.adjacency()):
	    # print(adjacencies)
	    node_adjacencies.append(len(adjacencies[1]))
	    node_text.append('# of connections: '+str(len(adjacencies[1])))
	return node_adjacencies,node_text

def mst_draw(numb,mode):


	start = time.time()

	arr = loadMst(numb)
	# ----- drawing -----

	G=nx.DiGraph()
	

	# show the MST result
	G = addNodesToG(G, arr)
	G = addEdgesToG(G, arr)

	pos=nx.spring_layout(G,scale=2) # maybe there are also other ways of drawing
	
	edge_trace = posToEdgeTrace(G,pos)
	node_trace = posToNodeTrace(G,pos)

	node_adjacencies,node_text = adjInfo(G)
	node_trace.marker.color = node_adjacencies
	node_trace.text = node_text




	fig = go.Figure(data=[edge_trace, node_trace])
	fig.show()


def main(args):
	mst_draw(1,'pearson')
	# do something
	# mst_gen(0)
	# for x in range(1,38):
	# 	mst_draw(x,'ed')
	# 	mst_draw(x,'pearson')
	

if __name__ == '__main__':
  main(sys.argv[1:])



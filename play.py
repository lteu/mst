import plotly.graph_objects as go


import numpy as np
import plotly

from draw import *


arr = loadMst(1)
arr2 = loadMst(2)
arr3 = loadMst(3)
G=nx.DiGraph()
G = addNodesToG(G, arr)
G = addEdgesToG(G, arr)
pos=nx.spring_layout(G,scale=2)
edge_trace1 = posToEdgeTrace(G,pos)

node_trace = posToNodeTrace(G,pos)


G=nx.DiGraph()
G = addNodesToG(G, arr2)
G = addEdgesToG(G, arr2)
edge_trace2 = posToEdgeTrace(G,pos)


G=nx.DiGraph()
G = addNodesToG(G, arr3)
G = addEdgesToG(G, arr3)
edge_trace3 = posToEdgeTrace(G,pos)


steps = []
for x in range(3):
    slider_step = {"args": [
            [x],
            {"frame": {"duration": 300, "redraw": False},
             "mode": "immediate",
             "transition": {"duration": 300}}
        ],"label": x,
            "method": "animate"}
    steps.append(slider_step)



sliders = [dict(
        active=10,
        currentvalue={"prefix": "Time line: "},
        pad={"t": 50},
        steps=steps
    )]

fig = go.Figure(
    data=[go.Scatter(x=[0, 0], y=[0, 0])],
    layout=go.Layout(
        # xaxis=dict(range=[0, 5], autorange=False),
        # yaxis=dict(range=[0, 5], autorange=False),
        title="Start Title",
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                          method="animate",
                          # args=[None]
                          args = [None, {"frame": {"duration": 1200, "redraw": False}}]
                          )])],
        sliders=sliders
    ),
    frames=[go.Frame(data=[edge_trace1],name="0"),
            go.Frame(data=[edge_trace2],name="1"),
            go.Frame(data=[edge_trace3],name="2",
                     layout=go.Layout(title_text="End Title"))]
)

fig.add_trace(
    node_trace
)

fig.show()










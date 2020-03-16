import plotly.graph_objects as go


import numpy as np
import plotly

from draw import *


def main(args):

  mst = []
  for numb in range(1,33):
    mst.append(loadMst(numb))


  isolates = []

  # remove unused nodes
  cum_df = pd.DataFrame(mst[0])
  for x in range(1,len(mst)):
    tmp = pd.DataFrame(mst[x])
    cum_df += tmp
  G=nx.Graph()
  G = addNodesToG(G, cum_df.values.tolist())
  G = addEdgesToG(G, cum_df.values.tolist())
  isolates = list(nx.isolates(G))
  G=nx.DiGraph()
  G = addNodesToG(G, mst[0])
  G = addEdgesToG(G, mst[0])
  # shape
  pos=nx.spring_layout(G,scale=2)

  # pos=nx.spiral_layout(G)
  # pos=nx.shell_layout(G)
  # pos=nx.spectral_layout(G)



  # print(pos)
  # sys.exit()


  # nodes
  node_trace = posToNodeTraceWithIsolates(G,pos,isolates)

  # edges
  edge_traces = []
  for x in range(len(mst)):
    G=nx.DiGraph()
    G = addNodesToG(G, mst[x])
    G = addEdgesToG(G, mst[x])
    edge_trace = posToEdgeTrace(G,pos)
    edge_traces.append(edge_trace)
    
  # edge_trace1 = posToEdgeTrace(G,pos)
  # G=nx.DiGraph()
  # G = addNodesToG(G, arr2)
  # G = addEdgesToG(G, arr2)
  # edge_trace2 = posToEdgeTrace(G,pos)
  # G=nx.DiGraph()
  # G = addNodesToG(G, arr3)
  # G = addEdgesToG(G, arr3)
  # edge_trace3 = posToEdgeTrace(G,pos)

  # steps
  steps = []
  for x in range(len(mst)):
      slider_step = { "args": [
                                [x],
                                {"frame": {"duration": 300, "redraw": False},
                                  "mode": "immediate",
                            "transition": {"duration": 300, "easing": "linear"}}],
                    "label" : x,
                    "method": "animate"}
      steps.append(slider_step)



  sliders = [dict(
          active=1,
          currentvalue={"prefix": "Time-line: "},
          pad={"t": 40},
          steps=steps
      )]


  # frames  
  frames = []
  for x in range(len(mst)):
    frames.append(go.Frame(data=[edge_traces[x]],name=str(x)))


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
                            args = [None, {"frame": {"duration": 1000, "redraw": False}}]
                            )])],
          sliders=sliders
      ),
      frames = frames
      # frames=[go.Frame(data=[edge_trace1],name="0"),
      #         go.Frame(data=[edge_trace2],name="1"),
      #         go.Frame(data=[edge_trace3],name="2",
      #                  layout=go.Layout(title_text="End Title"))]
  )

  fig.add_trace(
      node_trace
  )

  # fig.show()
  plotly.offline.plot(fig, filename = 'filename.html', auto_open=False)


if __name__ == '__main__':
  main(sys.argv[1:])








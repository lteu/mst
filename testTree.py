import plotly.graph_objects as go
import numpy as np
import plotly

from draw import *


def frame_args(duration):
    return {
            "frame": {"duration": duration},
            "mode": "immediate",
            "fromcurrent": True,
            "transition": {"duration": duration, "easing": "linear"},
        }


def main(args):
    # mst_draw(1,'pearson')

    # Create figure
    fig = go.Figure(
        layout=go.Layout(
        # xaxis=dict(range=[0, 5], autorange=False),
        # yaxis=dict(range=[0, 5], autorange=False),
        title="MST for XXX daya"    
      # layout=go.Layout(
      #       xaxis=dict(range=[0, 5], autorange=False),
      #       yaxis=dict(range=[0, 5], autorange=False)
      #       )
      )
    )
    
    hasSetNodes = False
    for numb in np.arange(1,6):
        arr = loadMst(numb)
        G=nx.DiGraph()
        G = addNodesToG(G, arr)
        G = addEdgesToG(G, arr)
        
        if not hasSetNodes:
            pos=nx.spring_layout(G,scale=2)
            edge_trace = posToEdgeTrace(G,pos)
            node_trace = posToNodeTrace(G,pos)
            hasSetNodes = True
        else:
            edge_trace = posToEdgeTrace(G,pos)

        fig.add_trace(
            edge_trace
        )
        fig.add_trace(
            node_trace
        )

    # Make 10th trace visible

    # Create and add slider
    steps = []
    for i in range(int(len(fig.data)/2)):
        step = dict(
            method="restyle",
            args=["visible", [False] * len(fig.data)],
        )
        step["args"][1][i*2] = True  # Toggle i'th trace to "visible"
        step["args"][1][i*2+1] = True
        steps.append(step)


    # only step 0 is visible
    for x in range(len(fig.data)):
        fig.data[x].visible = False
    fig.data[0].visible = True
    fig.data[1].visible = True



    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Time line: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        # updatemenus = [
        #     {
        #         "buttons": [
        #             {
        #                 "args": [step["args"],{"frame": {"duration": 500, "redraw": False},
        #                         "fromcurrent": True, "transition": {"duration": 300,
        #                                                             "easing": "quadratic-in-out"}}],
        #                 "label": "&#9654;", # play symbol
        #                 "method": "animate",
        #             },
        #             # {
        #             #     "args": [None],
        #             #     "label": "&#9724;", # pause symbol
        #             #     "method": "animate",
        #             # },
        #         ],
        #         "direction": "up",
        #         "type": "buttons",
        #     }
        #  ],
        sliders=sliders
    )

    # fig.update_layout(
    #     updatemenus=[dict(
    #         type="buttons",
    #         buttons=[dict(label="Play",
    #                       method="animate",
    #                       args=[None])])]
    # )
    




    fig.show()
    # plotly.offline.plot(fig, filename = 'filename.html', auto_open=False)



if __name__ == '__main__':
  main(sys.argv[1:])



import plotly.graph_objects as go

fig = go.Figure(
    data=[

    go.Scatter(x=[0, 1], y=[0, 1])],
    layout=go.Layout(
        xaxis=dict(range=[0, 5], autorange=False),
        yaxis=dict(range=[0, 5], autorange=False),
        title="Start Title",
        # updatemenus=[dict(
        #     type="buttons",
        #     buttons=[dict(label="Play",
        #                   method="animate",
        #                   args=[None])])]
        updatemenus = [{"type": "buttons",
                 "buttons": [{"label": "Your Label",
                              "method": "animate",
                              "args": ["frame1", "frame2"]}]}]
    ),
    frames=[go.Frame(data=[go.Scatter(x=[1, 2, 2], y=[1, 2, 8])]),
            go.Frame(data=[go.Scatter(x=[1, 4, 6], y=[1, 4, 4])]),
            go.Frame(data=[go.Scatter(x=[3, 4, 4], y=[3, 4, 5])],
                     layout=go.Layout(title_text="End Title"))]
)

fig.show()
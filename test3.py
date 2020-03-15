import plotly.graph_objects as go
import numpy as np
import plotly

# Create figure
fig = go.Figure(

  layout=go.Layout(
        xaxis=dict(range=[0, 5], autorange=False),
        yaxis=dict(range=[0, 5], autorange=False)
        )
)

# Add traces, one for each slider step
# for step in np.arange(0, 5, 0.1):
#     fig.add_trace(
#         go.Scatter(
#             visible=False,
#             line=dict(color="#00CED1", width=6),
#             name="𝜈 = " + str(step),
#             x=np.arange(0, 10, 0.01),
#             y=np.sin(step * np.arange(0, 10, 0.01))))

for step in np.arange(0, 1.5, 0.1):
    fig.add_trace(

        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=6),
            name="𝜈 = " + str(step),
            x=[1+step, 2, 2],
            y=[1+step, 2, 3]
        )

    )

# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="restyle",
        args=["visible", [False] * len(fig.data)],
    )
    step["args"][1][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Frequency: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show()

# plotly.offline.plot(fig, filename = 'filename.html', auto_open=False)
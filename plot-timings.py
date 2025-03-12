import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
from terrier.evaluate import format_fig


category_colors = {
    "Amphibian" : "green",
    "Flatworm" : "brown",
    "TERL" : "#601A4A",
    "DeepTE" : "#EE442F",
    "Terrier" : "#63ACBF",
}

marker_symbols = {
    "TERL" : "circle",
    "DeepTE" : "diamond",
    "Terrier" : "star-triangle-up",
}

fig = make_subplots(rows=1, cols=2, shared_yaxes=True, horizontal_spacing=0.01, subplot_titles=('a. CPU Timings', 'b. GPU Timings'))

df = pd.read_csv('timings.csv')

def plot_scatter(plot_col, column):
    x = df['Filesize (MB)']
    y = df[column]
    m, c = np.polyfit(x, y, 1)

    trend_x = np.array((x.min(), x.max()))
    trend_y = m * trend_x + c

    software = column.split(' ')[0]
    for category in df['Category'].unique():
        data = df[df['Category'] == category]
    fig.add_trace(
        go.Scatter(x=df['Filesize (MB)'], y=df[column], mode='markers', name=f"{software}", marker_color=category_colors[software], showlegend=plot_col==1, 
                             marker_symbol=marker_symbols[software], marker_size=12,
                             legendgroup=f"legend{plot_col}"
        ), row=1, col=plot_col,
    )

    # Calculate mx + c trendline

    fig.add_trace(go.Scatter(x=trend_x, y=trend_y, marker_color=category_colors[software], mode='lines', showlegend=False, name=f'Trend: y = {m:.1f}x + {c:.1f}'), row=1, col=plot_col)

    fig.add_annotation(
        x=x.max()+0.15, y=df[column].max(),
        text=f"y = {m:.1f}x + {c:.1f}", 
        showarrow=False, 
        font=dict(size=18), 
        xanchor="right", 
        yanchor="bottom",
        font_color=category_colors[software],
        # xref="paper",
        # yref="paper",
        row=1, col=plot_col,
    )


plot_scatter(2, 'Terrier GPU')
plot_scatter(2, 'DeepTE GPU')
plot_scatter(2, 'TERL GPU')

plot_scatter(1, 'Terrier CPU')
plot_scatter(1, 'DeepTE CPU')
plot_scatter(1, 'TERL CPU')


format_fig(fig)

fig.update_xaxes(title_text='Filesize (MB)', row=1, col=1)
fig.update_xaxes(title_text='Filesize (MB)', row=1, col=2)
fig.update_yaxes(title_text='Computation Time (s)', row=1, col=1)

fig.update_layout(width=1200, height=600)
# set margin
fig.update_layout(margin=dict(l=0, r=0, t=20, b=20))

# put legend in top left corner of plot
fig.update_layout(
    legend=dict(
        x=0.01,
        y=0.98,
        xanchor='left',
        yanchor='top',
        xref='paper',
        yref='paper',
        orientation='v',
    ),
)

fig.show()
fig.write_image("terrier-experimental-data-timings.pdf")

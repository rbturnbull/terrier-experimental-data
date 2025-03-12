import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from terrier.evaluate import format_fig

df = pd.read_csv("summary.csv")

fig = make_subplots(
    rows=2, cols=2, 
    subplot_titles=(
        "RepeatModeler", 
        "Terrier", 
    ),
    shared_xaxes=True,
    shared_yaxes=True,
    vertical_spacing=0.01,
    horizontal_spacing=0.03,
    row_heights=[0.14, 0.86],
)

categories = ["DNA", "LINE", "LTR", "Other", "Unknown"]
colors = {
    "DNA": "purple",
    "LINE": "#EE442F",
    "LTR": "#63ACBF",
    "Other": "#999999",
    "Unknown": "black",
}


for category in categories:
    color = colors[category]
    amphibians = df[df["Organism Type"] == "Amphibian"]
    flatworms = df[df["Organism Type"] == "Flatworm"]
    flatworms_species_names = [f"<i>{species}</i>" for species in flatworms["Species"]]
    fig.add_trace(
        go.Bar(
            y=flatworms_species_names,
            x=flatworms[f"Terrier {category}"],
            name=category,
            marker_color=color,
            showlegend=False,
            orientation='h',
        ),
        row=1,
        col=2,
    )
    fig.add_trace(
        go.Bar(
            y=flatworms_species_names,
            x=flatworms[f"RepeatModeler {category}"],
            name=category,
            marker_color=color,
            showlegend=True,
            orientation='h',
        ),
        row=1,
        col=1,
    )
    species_names = [f"<i>{species}</i>" for species in amphibians["Species"]]
    fig.add_trace(
        go.Bar(
            y=species_names,
            x=amphibians[f"Terrier {category}"],
            name=category,
            marker_color=color,
            showlegend=False,
            orientation='h',
        ),
        row=2,
        col=2,
    )
    fig.add_trace(
        go.Bar(
            y=species_names,
            x=amphibians[f"RepeatModeler {category}"],
            name=category,
            marker_color=color,
            showlegend=False,
            orientation='h',
        ),
        row=2,
        col=1,
    )

# Stack bars
fig.update_layout(barmode='stack')
format_fig(fig)
fig.update_layout(
    xaxis3_title="TE Count",
    xaxis4_title="TE Count",
    yaxis1_title="Flatworms",
    yaxis3_title="Amphibians",
    legend_title="",
    width=1200,
    height=1650,
)
# set margins
fig.update_layout(margin=dict(l=0, r=0, t=20, b=10))

# put legend inside the plot
fig.update_layout(
    legend=dict(
        # orientation="h",
        yanchor="top",
        y=0.995,
        xanchor="right",
        # change order
        traceorder="normal",
        x=0.99,
    ),
)


fig.show()
fig.write_image("terrier-experimental-data-summary.pdf")
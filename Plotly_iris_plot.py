import plotly.express as px

fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="petal_length",
    size="petal_length",
    hover_data={
        "sepal_width": True,
        "sepal_length": True,
        "petal_length": True
    },
    title="🌸 Iris Dataset — Sepal Width vs Sepal Length",
    labels={
        "sepal_width": "Sepal Width",
        "sepal_length": "Sepal Length",
        "petal_length": "Petal Length"
    },
    color_continuous_scale="Viridis",
    template="plotly_dark"
)

fig.update_traces(
    marker=dict(
        opacity=0.85,
        line=dict(width=1, color="white")
    )
)

fig.update_layout(
    title=dict(
        text="🌸 Iris Dataset — Sepal Width vs Sepal Length",
        x=0.5,
        xanchor="center",
        font=dict(size=24)
    ),
    xaxis=dict(
        title="Sepal Width",
        showgrid=True,
        zeroline=False
    ),
    yaxis=dict(
        title="Sepal Length",
        showgrid=True,
        zeroline=False
    ),
    coloraxis_colorbar=dict(
        title="Petal Length"
    ),
    width=1000,
    height=650
)

fig.show()

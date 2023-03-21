import streamlit as st
import json
import networkx as nx
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def create_graph(data):
    # Create a NetworkX graph from the JSON data
    G = nx.Graph()

    for node in data["nodes"]:
        G.add_node(node["id"], label=node["label"])

    for edge in data["edges"]:
        G.add_edge(edge["source"], edge["target"])

    # Create a Plotly figure from the graph
    pos = nx.spring_layout(G)

    fig = make_subplots(rows=1, cols=1)
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        fig.add_trace(
            go.Scatter(x=[x0, x1, None], y=[y0, y1, None], mode="lines"),
            row=1,
            col=1,
        )

    node_x = []
    node_y = []
    node_label = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_label.append(G.nodes[node]["label"])

    fig.add_trace(
        go.Scatter(x=node_x, y=node_y, mode="markers+text", text=node_label),
        row=1,
        col=1,
    )

    fig.update_layout(
        showlegend=False,
        height=600,
        width=800,
        margin=dict(l=0, r=0, b=0, t=0),
        hovermode="closest",
        plot_bgcolor="white",
    )

    return fig


# Define the Streamlit app
st.title("JSON Node Graph")
uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    # Load the JSON data
    data = json.load(uploaded_file)

    # Create the node graph
    fig = create_graph(data)

    # Show the node graph
    st.plotly_chart(fig)


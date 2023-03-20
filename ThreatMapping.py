import streamlit as st
import networkx as nx
import json
import plotly.graph_objects as go
import altair as alt
import pandas as pd


# Define a function to load and parse the JSON file
def load_json_file(uploaded_file):
    data = json.loads(uploaded_file.read().decode("utf-8"))
    return data


# Define a function to create a node map
def create_node_map(data):
    G = nx.DiGraph()
    for key in data:
        G.add_node(str(key))  # Convert key to string to make it hashable
        value = data[key]
        if isinstance(value, (list, tuple)):
            for v in value:
                G.add_edge(str(key), str(v))  # Convert key and value to string to make them hashable
        elif isinstance(value, dict):
            for k, v in value.items():
                G.add_edge(str(key), f"{str(k)}={str(v)}")  # Convert key, subkey and value to string to make them hashable
        else:
            G.add_edge(str(key), str(value))  # Convert key and value to string to make them hashable
    return G


# Define a function to create a Plotly figure from a networkx graph
def create_plotly_figure(G):
    pos = nx.spring_layout(G)
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
    node_x = []
    node_y = []
    node_text = []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node)
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=False,
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
    node_trace.text = node_text
    for node, adjacencies in enumerate(G.adjacency()):
        node_trace.marker.color.append(len(adjacencies[1]))
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>Node map of JSON data',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)))
    return fig


# Define a function to create an Altair chart from a networkx graph
def create_altair_chart

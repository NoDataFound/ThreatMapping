import streamlit as st
import json
import networkx as nx
import matplotlib.pyplot as plt
from io import StringIO

def load_json(json_str):
    G = nx.Graph()
    data = json.loads(json_str)
    for node, adj_list in data.items():
        for adj_node in adj_list:
            G.add_edge(node, adj_node)
    return G

def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.show()

st.title("Nodemap Visualizer")

# Allow user to upload a JSON file
json_file = st.file_uploader("Upload a JSON file", type=["json"])

if json_file is not None:
    # Load the JSON data
    json_str = json_file.read().decode("utf-8")

    # Convert JSON data to NetworkX graph
    graph = load_json(json_str)

    # Draw the nodemap
    draw_graph(graph)

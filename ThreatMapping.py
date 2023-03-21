import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph

# Set page title and description
st.set_page_config(page_title="JSON Node Graph", page_icon=":bar_chart:", layout="wide")
st.title("JSON Node Graph")

# Upload JSON file
uploaded_file = st.file_uploader("Choose a JSON file", type="json")

if uploaded_file is not None:
    # Load JSON data
    data = json.load(uploaded_file)

    # Create NetworkX graph from JSON data
    graph = json_graph.node_link_graph(data)

    # Draw graph using NetworkX and Matplotlib
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_size=100, node_color='r', alpha=0.8)
    nx.draw_networkx_edges(graph, pos, alpha=0.5)
    nx.draw_networkx_labels(graph, pos, font_size=8, font_family='sans-serif')
    plt.axis('off')
    st.pyplot()

    # Show raw JSON data
    st.subheader("Raw JSON data")
    st.json(data)


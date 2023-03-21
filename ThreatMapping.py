import streamlit as st
import json
import networkx as nx
import matplotlib.pyplot as plt

st.title('JSON Node Graph Visualizer')
st.text('This app allows you to upload a JSON file and visualize it with a node graph')

# Get JSON file from user
json_file = st.file_uploader('Upload a JSON file', type = 'json')
if json_file is not None:
    # Load the JSON file
    with open(json_file) as f:
        data = json.load(f)

    # Generate graph from JSON data  
    G = nx.Graph(data)

    # Draw graph 
    plt.figure(figsize=(8, 8)) 
    nx.draw_networkx(G, with_labels=True, node_color='skyblue', node_size=1200, alpha=0.5, linewidths=5, font_size=16) 

    # Show graph in Streamlit app 
    st.pyplot()

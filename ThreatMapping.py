import streamlit as st
import json
import pandas as pd
import networkx as nx
import altair as alt

# Set page config
st.set_page_config(layout="wide")

# Define function to create node map
def create_node_map(data):
    G = nx.Graph()
    for key in data:
        for value in data[key]:
            G.add_edge(key, value)
    return G

# Define function to create Altair chart from networkx graph
def create_altair_chart(G):
    pos = nx.spring_layout(G)
    nodes = pd.DataFrame.from_dict(pos, orient='index', columns=['x', 'y']).reset_index().rename(columns={'index': 'id'})
    edges = pd.DataFrame(list(G.edges), columns=['source', 'target'])
    nodes_and_edges = alt.LayerChart().transform_lookup(
        lookup='id',
        from_=alt.Data(values=nodes),
        as_={'x': 'x', 'y': 'y'}
    ).transform_lookup(
        lookup='source',
        from_=alt.Data(values=edges),
        as_={'source_x': 'x', 'source_y': 'y'}
    ).transform_lookup(
        lookup='target',
        from_=alt.Data(values=nodes),
        as_={'target_x': 'x', 'target_y': 'y'}
    ).transform_fold(
        ['source_x', 'source_y', 'target_x', 'target_y'],
        as_=['dimension', 'value']
    ).encode(
        x=alt.X('value:Q', scale=alt.Scale(domain=[-1, 1]), axis=None),
        y=alt.Y('value:Q', scale=alt.Scale(domain=[-1, 1]), axis=None),
        detail='id:N'
    ).mark_circle(
        opacity=0.5,
        stroke='black',
        strokeWidth=0.5
    )
    return nodes_and_edges

# Define function to create table from JSON data
def create_table(data):
    df = pd.json_normalize(data)
    return df

# Main app code
st.title('JSON Visualization App')

# Create file uploader
uploaded_file = st.file_uploader('Upload JSON file', type=['json'])

# Load data and create visualization and table if file is uploaded
if uploaded_file is not None:
    data = json.load(uploaded_file)

    # Create node map and Altair chart
    G = create_node_map(data)
    chart = create_altair_chart(G)

    # Create table
    table = create_table(data)

    # Display visualization and table
    st.write('## Visualization')
    st.altair_chart(chart, use_container_width=True)
    st.write('## Table')
    st.write(table)

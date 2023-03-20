from collections.abc import Iterable
import json
import networkx as nx
import altair as alt
import pandas as pd
import streamlit as st

def create_node_map(data):
    G = nx.Graph()
    for key in data:
        if isinstance(data[key], Iterable) and not isinstance(data[key], str):
            for value in data[key]:
                if isinstance(value, dict):
                    value = tuple(sorted(value.items()))
                G.add_edge(key, value)
        elif isinstance(data[key], dict):
            data[key] = tuple(sorted(data[key].items()))
            G.add_edge(key, data[key])
        else:
            G.add_edge(key, data[key])
    return G

def create_altair_chart(graph):
    source, target = zip(*graph.edges())
    nodes = list(set(source + target))
    nodes_df = pd.DataFrame({'id': nodes, 'label': nodes})
    edges_df = pd.DataFrame({'source': source, 'target': target})
    chart = alt.Chart(edges_df).mark_circle(size=200).encode(
        x=alt.X('source:N', axis=alt.Axis(title='Source Node')),
        y=alt.Y('target:N', axis=alt.Axis(title='Target Node')),
        tooltip=['source', 'target']
    ).properties(width=600, height=600)
    text = chart.mark_text(fontSize=20).encode(
        text='id'
    )
    return (chart + text).interactive()

def main():
    st.title("JSON Visualizer")
    st.write("Upload a JSON file to visualize its contents.")
    file = st.file_uploader("Upload JSON", type=["json"])
    if file is not None:
        data = json.load(file)
        graph = create_node_map(data)
        st.subheader("Node Map")
        st.altair_chart(create_altair_chart(graph), use_container_width=True)
        st.subheader("Table")
        df = pd.DataFrame(data.items(), columns=['Key', 'Value'])
        st.dataframe(df)

if __name__ == "__main__":
    main()

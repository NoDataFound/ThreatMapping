import streamlit as st
import json
import networkx as nx
import pydot


def load_json(contents):
    data = json.loads(contents)
    return data


def build_graph(data):
    G = nx.MultiDiGraph()
    for step in data["steps"]:
        G.add_node(step["name"], label=step["name"])
        for target in step["targets"]:
            G.add_edge(step["name"], target)
    return G


def visualize_graph(G):
    dot_str = nx.drawing.nx_pydot.to_pydot(G).to_string()
    graph = pydot.graph_from_dot_data(dot_str)
    graph[0].set('dpi', '300')
    st.graphviz_chart(graph[0].to_string())


def main():
    st.title("Attack Flow Visualizer")
    st.write("Upload your JSON file below")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        contents = uploaded_file.read()
        data = load_json(contents)
        st.write("Your file has been loaded!")
        st.write(data)

        G = build_graph(data)
        st.write("Your attack flow visual:")
        visualize_graph(G)


if __name__ == "__main__":
    main()

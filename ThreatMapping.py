import streamlit as st
import json
import networkx as nx
import pygraphviz as pgv


def load_json(contents):
    data = json.loads(contents)
    return data


def build_graph(data):
    G = nx.DiGraph()

    steps = []
    targets = []

    # Extract the steps and targets from the JSON data
    for step in data["facets"]["mitreTechniques"]:
        steps.append(step["name"])
        targets.extend(step["name"])

    # Add the steps as nodes in the graph
    for step in steps:
        G.add_node(step)

    # Add the targets as edges in the graph
    for target in targets:
        G.add_edge(target, target.split(".")[0])

    return G


def visualize_graph(G):
    dot_str = nx.drawing.nx_agraph.to_agraph(G).to_string()
    graph = pgv.AGraph(dot_str)
    graph.layout(prog="dot")
    graph.draw("graph.png")
    st.image("graph.png")


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

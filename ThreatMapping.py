import streamlit as st
import json
import networkx as nx
from networkx.drawing.nx_agraph import to_agraph


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
    graph = to_agraph(G)
    if graph is not None:
        graph.node_attr.update(fontname="Arial", fontsize="10")
        graph.edge_attr.update(fontname="Arial", fontsize="10")
        graph.graph_attr.update(fontname="Arial", fontsize="12")
        graph.draw(format="png", prog="dot")
        img = graph.draw(format="png", prog="dot")
        st.image(img)
    else:
        st.write("Error while visualizing graph: Graph object is None.")


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

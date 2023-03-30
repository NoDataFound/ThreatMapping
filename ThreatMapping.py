import streamlit as st
import json
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
from nxpd import draw
from nxpd import nxpdParams
from nxpd import nxpd


def load_json(json_file):
    with open(json_file, "r") as f:
        data = json.load(f)
    return data


def build_graph(data):
    G = nx.MultiDiGraph()
    for step in data["steps"]:
        G.add_node(step["name"], label=step["name"])
        for target in step["targets"]:
            G.add_edge(step["name"], target)
    return G


def visualize_graph(G):
    pos = graphviz_layout(G, prog="dot")
    nxpdParams['show'] = 'ipynb'
    draw(G, pos=pos, show=True, format='png')


def main():
    st.title("Attack Flow Visualizer")
    st.write("Upload your JSON file below")

    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        data = load_json(uploaded_file)
        st.write("Your file has been loaded!")
        st.write(data)

        G = build_graph(data)
        st.write("Your attack flow visual:")
        visualize_graph(G)


if __name__ == "__main__":
    main()

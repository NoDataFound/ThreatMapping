import streamlit as st
import json
import networkx as nx
import matplotlib.pyplot as plt

# Define a function to load and parse the JSON file
def load_json_file(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

# Define a function to create a node map
def create_node_map(data):
    G = nx.DiGraph()
    for key in data:
        G.add_node(key)
        for value in data[key]:
            G.add_edge(key, value)
    return G

# Define the Streamlit app
def main():
    # Set the title and description
    st.set_page_config(page_title="JSON Node Map Visualizer", page_icon=":eyes:")
    st.title("JSON Node Map Visualizer")
    st.markdown("""
        This app allows you to upload a JSON file and visualize it as a node map and all Streamlit visualization types.
    """)

    # Add a file uploader
    uploaded_file = st.file_uploader("Choose a JSON file", type=["json"])

    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Load the JSON file
        data = load_json_file(uploaded_file)

        # Create a node map
        G = create_node_map(data)

        # Visualize the node map
        st.subheader("Node Map Visualization")
        fig, ax = plt.subplots(figsize=(10, 10))
        nx.draw(G, with_labels=True, ax=ax)
        st.pyplot(fig)

        # Visualize all Streamlit visualization types
        st.subheader("Streamlit Visualization Types")
        st.write("This is a sample text.")
        st.markdown("This is a sample markdown.")
        st.latex(r"\int_{a}^{b} x^2 dx")
        st.header("This is a sample header.")
        st.subheader("This is a sample subheader.")
        st.code("print('This is a sample code.')", language="python")
        st.json(data)
        st.table(data)
        st.dataframe(data)
        st.line_chart(data)
        st.area_chart(data)
        st.bar_chart(data)
        st.pyplot(fig)

# Run the Streamlit app
if __name__ == "__main__":
    main()

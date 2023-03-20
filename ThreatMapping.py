import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Define function to parse JSON file
def parse_json(file):
    data = pd.read_json(file)
    data = data.groupby('category').size().reset_index(name='count')
    data = data.sort_values('count', ascending=False)
    return data

# Define function to create static visualization
def create_chart(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(data['category'], data['count'])
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title('Categories by Count')
    ax.tick_params(axis='x', rotation=90)
    return fig

# Define main function for Streamlit app
def main():
    st.title('JSON File Visualizer')
    file = st.file_uploader('Upload JSON file', type='json')
    if file:
        data = parse_json(file)
        st.write(data)
        fig = create_chart(data)
        st.pyplot(fig)

if __name__ == '__main__':
    main()

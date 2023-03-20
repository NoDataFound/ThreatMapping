import streamlit as st
import pandas as pd
import plotly.express as px

# Define function to parse JSON file
def parse_json(file):
    data = pd.read_json(file)
    data = data.groupby('category').size().reset_index(name='count')
    data = data.sort_values('count', ascending=False)
    return data

# Define function to create static visualization
def create_chart(data):
    fig = px.bar(data, x='category', y='count', color='category')
    return fig

# Define main function for Streamlit app
def main():
    st.title('JSON File Visualizer')
    file = st.file_uploader('Upload JSON file', type='json')
    if file:
        data = parse_json(file)
        st.write(data)
        fig = create_chart(data)
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()

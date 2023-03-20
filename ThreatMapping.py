import streamlit as st
import json
import pandas as pd

# Function to load JSON file
def load_json(file):
    data = json.loads(file.read().decode('utf-8'))
    return data

# Function to load text file containing key names
def load_text(file):
    with file:
        keys = [line.strip() for line in file]
    return keys

# Streamlit app code
st.title('JSON Visualization and Prioritization')

# File uploader for JSON file
json_file = st.file_uploader('Upload JSON file', type='json')

# File uploader for text file containing key names
text_file = st.file_uploader('Upload text file containing key names', type='txt')

if json_file and text_file:
    # Load JSON data
    data = load_json(json_file)

    # Load key names from text file
    keys = load_text(text_file)

    # Count occurrences of key names in JSON data
    key_counts = {}
    for key in keys:
        count = sum(1 for obj in data if key in obj)
        key_counts[key] = count

    # Sort key counts in descending order
    sorted_counts = sorted(key_counts.items(), key=lambda x: x[1], reverse=True)

    # Create dataframe of key counts
    df = pd.DataFrame(sorted_counts, columns=['Key', 'Count'])

    # Bar chart of key counts
    st.bar_chart(df)

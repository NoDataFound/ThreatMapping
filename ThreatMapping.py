import streamlit as st
import json

# Function to load JSON file
def load_json(file):
    with open(file) as f:
        data = json.load(f)
    return data

# Function to load text file containing key names
def load_key_names(file):
    with open(file, 'r') as f:
        key_names = f.read().splitlines()
    return key_names

# Function to map JSON to key names
def map_json_to_keys(data, key_names):
    mapped_data = {}
    for key in key_names:
        if key in data:
            mapped_data[key] = data[key]
        else:
            mapped_data[key] = None
    return mapped_data

# Streamlit app code
st.title('JSON Key Mapping')

# File uploader for JSON file
json_file = st.file_uploader('Upload JSON file', type='json')

# File uploader for text file containing key names
key_names_file = st.file_uploader('Upload text file containing key names')

if json_file and key_names_file:
    # Load JSON data and key names
    data = load_json(json_file)
    key_names = load_key_names(key_names_file)

    # Map JSON data to key names
    mapped_data = map_json_to_keys(data, key_names)

    # Display mapped data
    st.write('Mapped data:')
    st.write(mapped_data)

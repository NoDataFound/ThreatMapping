import streamlit as st
import json
import pandas as pd
import altair as alt

# Function to load JSON file
def load_json(file):
    data = json.loads(file.read().decode('utf-8'))
    return data


# Function to load text file containing key names
def load_key_names(file):
    with open(file, 'r') as f:
        key_names = f.read().splitlines()
    return key_names

# Function to count items in JSON data
def count_items(data):
    items = {}
    for key in data:
        if isinstance(data[key], list):
            for item in data[key]:
                if item not in items:
                    items[item] = 1
                else:
                    items[item] += 1
    return items

# Streamlit app code
st.title('JSON Visualization and Prioritization')

# File uploader for JSON file
json_file = st.file_uploader('Upload JSON file', type='json')

# File uploader for text file containing key names
key_names_file = st.file_uploader('Upload text file containing key names')

if json_file:
    # Load JSON data
    data = load_json(json_file)

    # Count items in JSON data
    items = count_items(data)

    # Convert items to Pandas DataFrame
    df = pd.DataFrame.from_dict(items, orient='index', columns=['count'])
    df.index.name = 'item'
    df.reset_index(inplace=True)

    # Sort items by count
    df.sort_values('count', ascending=False, inplace=True)

    # Create visualization using Altair
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X('count:Q', axis=alt.Axis(title='Count')),
        y=alt.Y('item:N', axis=alt.Axis(title='Item'), sort=alt.EncodingSortField('count', order='descending'))
    ).properties(
        width=800,
        height=500,
        title='JSON Visualization'
    )

    # Display visualization
    st.altair_chart(chart, use_container_width=True)

if key_names_file:
    # Load key names from text file
    key_names = load_key_names(key_names_file)

    # Display key names
    st.write('Key names:')
    st.write(key_names)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

with open('data.json') as f:
    data = json.load(f)

with open('ssc_keys.txt', 'r') as f:
    key_values = f.read().splitlines()

def create_visualization(data, key_values):
    df = pd.DataFrame(data.items(), columns=['key', 'value'])
    df['color'] = df['other_key'].map({'value1': 'red', 'value2': 'green', 'value3': 'blue'})
    df = df[df['key'].isin(key_values)]
    fig, ax = plt.subplots()
    ax.scatter(df['key'], df['value'], c=df['color'])
    ax.set_xlabel('Key')
    ax.set_ylabel('Value')
    return fig

st.title('Visualizing Data Connections')
fig = create_visualization(data, key_values)
st.pyplot(fig)

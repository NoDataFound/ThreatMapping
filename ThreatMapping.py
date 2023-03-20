import streamlit as st
import pandas as pd
import altair as alt

# Define function to parse JSON file
def parse_json(file):
    data = pd.read_json(file)
    return data

# Define function to create dynamic visualization
def create_chart(data):
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('category:N', sort='-y'),
        y=alt.Y('count:Q'),
        color=alt.Color('category:N')
    ).properties(
        width=600,
        height=400
    ).transform_aggregate(
        count='count()',
        groupby=['category']
    ).transform_window(
        rank='rank(count)',
        sort=[alt.SortField('count', order='descending')]
    ).transform_filter(
        alt.datum.rank <= 10
    ).transform_window(
        index='row_number()'
    ).transform_filter(
        alt.datum.index <= 10
    ).properties(
        title='Top 10 Categories by Count'
    )
    return chart


# Define main function for Streamlit app
def main():
    st.title('JSON File Visualizer')
    file = st.file_uploader('Upload JSON file', type='json')
    if file:
        data = parse_json(file)
        st.write(data)
        chart = create_chart(data)
        st.altair_chart(chart, use_container_width=True)

if __name__ == '__main__':
    main()

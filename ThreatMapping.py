import streamlit as st
import json
import stix2

st.set_page_config(page_title="JSON to STIX 2.0 Converter")
def json_to_stix(json_data):
    try:
        data = json.loads(json_data)
        stix_data = stix2.parse(data)
        return stix_data
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("JSON to STIX Converter")
    json_file = st.file_uploader("Upload a JSON file", type=["json"])
    if json_file is not None:
        json_data = json_file.read().decode("utf-8")
        stix_data = json_to_stix(json_data)
        if isinstance(stix_data, str):
            st.error(stix_data)
        else:
            st.json(stix_data)
if __name__ == "__main__":
    main()

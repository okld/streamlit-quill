import streamlit as st
from streamlit_quill import st_quill


st.sidebar.title(":computer: Quill Editor")
placeholder = st.sidebar.text_input("Placeholder", "Some placeholder text")
html = st.sidebar.checkbox("Return HTML", False)
read_only = st.sidebar.checkbox("Read only", False)

content = st_quill(
    placeholder=placeholder,
    html=html,
    readonly=read_only,
)

st.write(content)

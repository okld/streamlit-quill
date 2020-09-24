import streamlit as st
from streamlit_quill import st_quill

content = st_quill()
st.write(content)

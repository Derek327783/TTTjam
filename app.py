import streamlit as st

st.title("Upload your audio files and get an image for inspiration!")
uploaded_file = st.file_uploader("Upload an audio file",type =["wav"],key="Audio_file_input")

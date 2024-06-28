import streamlit as st

st.title("Upload your audio files and get an image for inspiration!")
uploaded_file = st.file_uploader("Upload an audio file",type =["wav"],key="Audio_file_input")
if st.button("Get tempo"):
    st.caption("110bpm")
if st.button("Get a textual description of your audio"):
    st.caption("I am now deaf")
if st.button("Get image inspiration"):
    st.caption("You do not want to see what image I came up with.")


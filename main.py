import streamlit as st
from flask import Genre_spotting_service as BNP
from flask import Beat_tracking_service as bt

st.title("Upload your audio files and get an image for inspiration!")
uploaded_file = st.file_uploader("Upload an audio file",type =["wav"],key="Audio_file_input")
if st.button("Get genre of music"):
    st.caption(BNP.run_inference(raw_data=uploaded_file))
if st.button("Get tempo of music"):
    st.caption(bt.beat_getter(uploaded_file))
if st.button("Get a textual description of your audio"):
    st.caption("I am now deaf")
if st.button("Get image inspiration"):
    st.caption("You do not want to see what image I came up with.")


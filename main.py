# This is a sample Python script.
import streamlit as st


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.title("Paste Your Audio File")
    audio = st.file_uploader("Open")



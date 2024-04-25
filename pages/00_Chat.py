# Home Page
import streamlit as st
from utilities.icon import page_icon


st.set_page_config(
    page_title="Medical Chat",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)





def main():
    """
    The main function that runs the application.
    """

    page_icon("💬")
    st.subheader("Medical Chat Playground", divider="red", anchor=False)

if __name__ == "__main__":
    main()
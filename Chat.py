# Home Page
import streamlit as st
import sys
sys.path.append('..')
# from models folder import chatmodel.py to get the askme function
from models.chatmodel import askme


st.set_page_config(
    page_title="Medical Chat",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)



def page_icon(emoji: str):
    """
    Shows an emoji as a Notion-style page icon.

    :param emoji: The emoji to display.

    Returns:
        None
    """

    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )






def main():
    """
    The main function that runs the application.
    """
    page_icon("💬")
    st.subheader("Medical Chat Playground")

    st.write("This is a playground for the Medical Chat application.")

    message_container = st.container(height=500, border=True)

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar = "🩺" if message["role"] == "assistant" else "😷"
        with message_container.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    prompt = st.text_input("Enter your question:")
    if st.button('Submit'):
        if prompt:
            try:
                prompt = prompt.strip()  # Strip any leading/trailing whitespace
                if prompt:  # Check if the prompt is not empty after stripping
                    response = askme(prompt)
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    with message_container.chat_message("assistant", avatar="🩺"):
                        st.markdown(response)
                else:
                    st.error("Please enter a non-empty question.")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
        else:
            st.error("Please enter a question to get an answer.")

    st.warning('This application is for informational purposes only and not intended as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.', icon="⚠️")

if __name__ == "__main__":
    main()
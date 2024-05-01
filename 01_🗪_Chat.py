# Home Page
import streamlit as st
from models.chatmodel import initialize_chat_model, get_model_response

# Initialize the chat model
generator = initialize_chat_model()


st.set_page_config(
    page_title="Medical Chat",
    page_icon="🗪",
    layout="wide",
    initial_sidebar_state="expanded",
)


def extract_model_names(models_info: list) -> tuple:
    """
    Extracts the model names from the list of models.

    :param models_info: The list of models.

    Returns:
        A tuple of the model names.
    """
    return tuple(model["name"] for model in models_info["models"])



def page_icon(emoji: str):
    st.write(f'<span style="font-size: 78px; line-height: 1">{emoji}</span>', unsafe_allow_html=True)




def main():
    """
    The main function that runs the application.
    """
    page_icon("🗪")
    st.subheader("Medical Chat Playground")

    message_container = st.container(height=500, border=True)

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state.messages:
        avatar = "🤖" if message["role"] == "assistant" else "😎"
        with message_container:
            st.markdown(f"{avatar} {message['content']}")

    prompt = st.text_input("Enter a prompt here...")
    if prompt and st.button("Send"):
        st.session_state.messages.append(
            {"role": "user", "content": prompt}
        )

        with message_container:
            st.markdown(f"😎 {prompt}")

        with st.spinner("AI is thinking..."):
            response = get_model_response(generator, prompt)
            st.session_state.messages.append(
                {"role": "assistant", "content": response}
            )

        # Display response
        with message_container:
            st.markdown(f"🤖 {response}")

if __name__ == "__main__":
    main()




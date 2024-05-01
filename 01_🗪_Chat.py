# Home Page
import streamlit as st
import sys
import streamlit as st
from transformers import pipeline
from PIL import Image
sys.path.append('..')
# from models folder import chatmodel.py to get the askme function
from models.chatmodel import askme



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
    page_icon("🗪")
    st.subheader("Medical Chat Playground", divider="red", anchor=False)

    client = huggingface_hub.HfApi(
        base_url="http://localhost:8000",
        api_key="ollama",
    )

    models_info = ollama.list()
    available_models = extract_model_names(models_info)

    if available_models:
        selected_model = st.selectbox(
            "Pick a model available locally on your system:", available_models

        )
    else:
        st.warning("You have not pulled any model from Ollama yet!", 
                   icon="⚠️")
        if st.button("Go to settings to download a model"):
            st.page_switcher.switch(page="03_⚙️_Settings")

    message_container = st.container(height=500, border=True)

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    for message in st.session_state.messages:
        avatar = "🤖" if message["role"] == "assistant" else "😎"
        with message_container.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
    
    if prompt := st.chat_input("Enter a prompt here..."):
        try:
            st.session_state.messages.append(
                {"role": "user", "content": prompt})
            
            message_container.chat_message("user", avatar="😎").markdown(prompt)

            with message_container.chat_message("assistant", avatar="🤖"):
                with st.spinner("AI is thinking..."):
                    stream = client.chat.completions.create(
                        model=selected_model,
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        stream=True,
                    )
                response = st.write_stream(stream)
            st.session_state.messages.append(
                {"role": "assistant", "content": response})
        
        except Exception as e:
            st.error(e, icon="🚨")


if __name__ == "__main__":
    main()
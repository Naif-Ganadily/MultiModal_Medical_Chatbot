# Multimodal Interface
import streamlit as st
from PIL import Image
from io import BytesIO
import base64
from utilities.icon import page_icon
from models.multimodal import get_gemini_response


st.set_page_config(
    page_title="Medical Image Analysis",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

def img_to_base64(image):
    buffered =BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

'''
def get_allowed_model_names(models_info: dict) -> tuple:
    allowed_models = ["Med-Palm2:latest", "Med-Flamingo2:latest"]
    return tuple(
        model
        for model in allowed_models
        if model in [m["name"] for m in models_info["models"]]
    )
'''
def display_chat_messages(container, messages):
    for message in messages:
        role = message["role"]
        content = message["content"]
        avatar = "🖼️" if role == "assistant" else "👨‍⚕️"
        with container:
            st.markdown(f"{avatar} {role.capitalize()}: {content}")








def main():
    page_icon("🧊")
    st.subheader("Medical Image Analysis", divider="red")

    if "chat_messages" not in st.session_state:
        st.session_state.chat_messages = []

    col1, col2 = st.columns(2)

    with col2:
        container1 = st.container()
        uploaded_file = st.file_uploader("Upload an image for analysis", type=["png", "jpg", "jpeg"], key="file_uploader")
        if uploaded_file is not None:
            image = Image.open(BytesIO(uploaded_file.getvalue()))
            st.session_state.uploaded_file_state = uploaded_file.getvalue()
            with container1:
                st.image(image, caption="Uploaded image")

    with col1:
        container2 = st.container()
        display_chat_messages(container2, st.session_state.chat_messages)
        user_input = st.text_input("Ask a question about the image:", key="user_input")
        
        if st.button("Analyze", key="analyze_button"):
            if uploaded_file is not None and user_input:
                st.session_state.chat_messages.append({"role": "user", "content": user_input})
                image_base64 = img_to_base64(image)
                response_text = get_gemini_response(user_input, image_base64)
                st.session_state.chat_messages.append({"role": "assistant", "content": response_text})
                display_chat_messages(container2, st.session_state.chat_messages)

if __name__ == "__main__":
    main()






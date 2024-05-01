# Settings for the Multimodal and Chat Interface

import streamlit as st
from time import sleep
from utilities.icon import page_icon

st.set_page_config(
    page_title="AI Management",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    page_icon("⚙️"),
    st.subheader("AI Management", divider="red", anchor=False)

    st.subheader("Download AI Models", anchor=False)
    model_name = st.text_input(
        "Enter the name of the model to download", placeholder="Llama 3"
    )

    if st.button(f":green[**Download**]:red[**{model_name}**]"):
        if model_name:
            try:
                ollama.pull(model_name)
                st.success(f"Download model: {model_name}", icon="✅")
                st.balloons()
                sleep(1)
                st.rerun()
            except Exception as e:
                st.error(
                    f"""Failed to download model: {
                        model_name}. Error: {str(e)}""",
                        icon="❌",
                )
        else:
            st.warning("Please enter a model name.", icon="⚠️")

    st.divider()

    st.subheader("Create model", anchor=False)
    modelfile = st.text_area(
        "Enter the modelfile",
        height=100,
        placeholder="""FROM Llama 3 SYSTEM you are mario from super mario bros.""",
    )
    model_name = st.text_input(
        "Enter the name of the model to create", placeholder="Llama 3"

    )

    if st.button(f"Create model: {model_name}"):
        if model_name and modelfile:
            try:
                ollama.create(model=model_name, modelfile=modelfile)
                st.success(f"Created model: {model_name}", icon="✅")
                st.balloons()
                sleep(1)
                st.rerun()
            except Exception as e:
                st.error(
                    f"""Failed to create model: {
                        model_name}. Error: {str(e)}""",
                        icon="❌",
                )
        else:
            st.warning("Please enter a model name and modelfile.", icon="⚠️")

    st.divider()

    st.subheader("Delete Models", anchor=False)
    models_info = ollama.list()
    available_models = [m["name"] for m in models_info["models"]]

    if available_models:
        selected_models = st.multiselect("Select models to delete", available_models)
        if st.button("🗑️ :red[**Delete Selected Model(s)**]"):
            for model in selected_models:
                try:
                    ollama.delete(model)
                    st.success(f"Deleted model: {model}", icon="✅")
                    sleep(1)
                    st.rerun()
                except Exception as e:
                    st.error(
                        f"""Failed to delete model: {
                            model}. Error: {str(e)}""",
                            icon="❌",
                    )


import streamlit as st
from fpdf import FPDF
from utilities.icon import page_icon

st.set_page_config(
    page_title="Download Results",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

def create_pdf(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in content:
        pdf.cell(200, 10, txt=line, ln=True)
    pdf_filename = 'chat_report.pdf'
    pdf.output(pdf_filename)
    return pdf_filename

def main():
    page_icon("📄")
    st.subheader("Download Chat or Analysis Results", divider="red")

    # Assume session_state.chat_messages is a list of dictionaries with 'role' and 'content' keys
    if "chat_messages" in st.session_state:
        chat_content = [f"{msg['role']}: {msg['content']}" for msg in st.session_state.chat_messages]
        if st.button("Download Chat Results"):
            pdf_filename = create_pdf(chat_content)
            with open(pdf_filename, "rb") as file:
                st.download_button(
                    label="Download PDF",
                    data=file,
                    file_name=pdf_filename,
                    mime="application/pdf"
                )

if __name__ == "__main__":
    main()
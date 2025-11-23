import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
try:
    from agent import run_agent
except ValueError as e:
    st.error(
        "The application has encountered an error. "
        "This is likely due to a missing `GEMINI_API_KEY` in your Streamlit Cloud secrets. "
        "Please go to your app's settings, add the `GEMINI_API_KEY` as a secret, and reboot the app. "
        "For more information, see the [Streamlit documentation on secrets management](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/secrets-management)."
    )
    st.stop()

# --- Utility Functions ---
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def save_metadata(filename, summary, quiz):
    try:
        with open("memory.json", "r+") as f:
            memory = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        memory = []
    
    memory.append({
        "filename": filename,
        "summary": summary,
        "quiz": quiz
    })
    
    with open("memory.json", "w") as f:
        json.dump(memory, f, indent=4)

# --- Streamlit UI ---
st.set_page_config(layout="wide")
st.title("📚 AI Study Assistant")

if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = ""
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "quiz" not in st.session_state:
    st.session_state.quiz = ""
if "filename" not in st.session_state:
    st.session_state.filename = ""

with st.sidebar:
    st.header("Upload PDF")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        st.session_state.filename = uploaded_file.name
        st.session_state.extracted_text = extract_text_from_pdf(uploaded_file)
        st.success("PDF uploaded and text extracted!")
        st.write(f"**File:** {st.session_state.filename}")

    if st.session_state.extracted_text:
        if st.button("Generate Summary"):
            with st.spinner("Generating summary..."):
                prompt = f"Summarize the following PDF text: {st.session_state.extracted_text}"
                run_result = run_agent(prompt)
                st.session_state.summary = run_result.final_output
                st.success("Summary generated!")

        if st.button("Create Quiz"):
            with st.spinner("Generating quiz..."):
                prompt = f"Generate a quiz based ONLY on the following full PDF text. Produce MCQs or mixed-style questions: {st.session_state.extracted_text}"
                run_result = run_agent(prompt)
                st.session_state.quiz = run_result.final_output
                st.success("Quiz generated!")

        if st.session_state.summary or st.session_state.quiz:
            if st.button("Save to Memory"):
                save_metadata(st.session_state.filename, st.session_state.summary, st.session_state.quiz)
                st.success("Results saved to memory.json!")

# --- Main Content Area ---
st.header("Results")

tab1, tab2, tab3 = st.tabs(["Extracted Text", "Summary", "Quiz"])

with tab1:
    st.header("Extracted Text")
    if st.session_state.extracted_text:
        st.text_area("Full Text", st.session_state.extracted_text, height=500)
    else:
        st.info("Upload a PDF to extract text.")

with tab2:
    st.header("Summary")
    if st.session_state.summary:
        summary_layout = st.radio(
            "Choose summary layout:",
            ("Card", "Block", "Container"),
            key="summary_layout"
        )
        if summary_layout == "Card":
            st.markdown(f"**Summary:**\n{st.session_state.summary}")
        elif summary_layout == "Block":
            st.code(st.session_state.summary, language="text")
        else: # Container
            with st.container(border=True):
                st.write(st.session_state.summary)
    else:
        st.info("Generate a summary from the extracted text.")

with tab3:
    st.header("Quiz")
    if st.session_state.quiz:
        st.markdown(st.session_state.quiz)
    else:
        st.info("Generate a quiz from the extracted text.")

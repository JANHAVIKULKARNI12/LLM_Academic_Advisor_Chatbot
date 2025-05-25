import streamlit as st
from advisor_chain import build_chain

st.set_page_config(page_title="Academic Advisor Bot 🎓", layout="wide")
st.title("📚 Academic Advisor Chatbot")

st.markdown("Upload PDFs in the `data/` folder and ask questions related to your university, courses, or academic guidance.")

if "chain" not in st.session_state:
    with st.spinner("Setting up the chatbot..."):
        st.session_state.chain = build_chain()

query = st.text_input("💬 Ask a question:")
if query:
    with st.spinner("Thinking..."):
        response = st.session_state.chain.run(query)
        st.write("🤖", response)

import streamlit as st
from ragchatbot import answer_question
from build_knowledge_base import collection
from search import search
# collection must be built/imported here too

st.title("Mahindra Vehicle Assistant")

user_question = st.text_input("Ask me about any Mahindra vehicle:")

if st.button("Ask"):
    if user_question:
        answer = answer_question(collection, user_question)
        st.write(answer)
    else:
        st.write("Please type a question first.")

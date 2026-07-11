import streamlit as st
import whisper
import pyttsx3
import tempfile

from ragchatbot import answer_question
from build_knowledge_base import collection
from search import search
from video_lookup import load_all_vehicles, get_video_path

all_vehicles = load_all_vehicles()
whisper_model = whisper.load_model("base")
tts_engine = pyttsx3.init()

st.title("Mahindra Vehicle Assistant")

st.subheader("Type your question:")
user_question = st.text_input("Ask me about any Mahindra vehicle:")

st.subheader("Or ask by voice:")
audio_value = st.audio_input("Record your question")

final_question = None

if audio_value is not None:
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        tmp_file.write(audio_value.getvalue())
        tmp_path = tmp_file.name

    transcription = whisper_model.transcribe(tmp_path)
    final_question = transcription["text"]
    st.write(f"You said: {final_question}")

elif user_question:
    final_question = user_question

if st.button("Ask"):
    if final_question:
        answer = answer_question(collection, final_question)
        st.write(answer)

        video_path = get_video_path(final_question, all_vehicles)
        if video_path:
            st.video(video_path)

        tts_engine.say(answer)
        tts_engine.runAndWait()
    else:
        st.write("Please type or record a question first.")
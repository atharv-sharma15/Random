import streamlit as st
import whisper
import subprocess
import sounddevice as sd
from scipy.io.wavfile import write as write_wav
from video_lookup import load_all_vehicles, get_video_path, correct_vehicle_names_in_query
from ragchatbot import answer_question
from build_knowledge_base import collection


all_vehicles = load_all_vehicles()
whisper_model = whisper.load_model("base")

st.title("Mahindra Vehicle Assistant")


def handle_question(final_question):
    st.write(f"You asked: {final_question}")

    answer = answer_question(collection, final_question)
    st.write(answer)

    video_path = get_video_path(final_question, all_vehicles)
    if video_path:
        st.video(video_path)

    subprocess.run(["say", answer])


st.subheader("Type your question:")
user_question = st.text_input("Ask me about any Mahindra vehicle:")

if st.button("Ask"):
    if user_question:
        handle_question(user_question)
    else:
        st.write("Please type a question first.")

st.subheader("Or tap to ask by voice:")

if st.button("🎤 Tap to Speak"):
    duration = 6  # seconds — adjust if questions feel cut off or too long
    sample_rate = 16000

    st.write("Listening... speak now.")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    temp_path = "temp_question.wav"
    write_wav(temp_path, sample_rate, recording)

    transcription = whisper_model.transcribe(temp_path)
    final_question = transcription["text"]

    handle_question(final_question)
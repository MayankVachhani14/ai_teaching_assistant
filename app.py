import streamlit as st
import os
from pipeline.extractor import extract_audio
from pipeline.transcriber import transcribe_audio
from pipeline.chunker import chunk_segments
from pipeline.embedder import embed_chunks, model
from pipeline.vector_store import save_index, search_index
from pipeline.qa_engine import get_answer

os.makedirs("uploads", exist_ok=True)
os.makedirs("data", exist_ok=True)

if "video_processed" not in st.session_state:
    st.session_state.video_processed = False

if "show_success" not in st.session_state:
    st.session_state.show_success = False

if "question_asked" not in st.session_state:
    st.session_state.question_asked = False

st.title("AI Teaching Assistant")
st.write("Upload an educational video and ask questions from it!")

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "mov"])

if uploaded_file is not None:

    video_path = f"uploads/{uploaded_file.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Video uploaded successfully!")

    if st.button("Process Video"):

        progress = st.progress(0)
        status = st.empty()

        status.text("Step 1/5 - Extracting audio...")
        audio_path = extract_audio(video_path)
        progress.progress(20)

        status.text("Step 2/5 - Transcribing audio...")
        segments = transcribe_audio(audio_path)
        progress.progress(40)

        status.text("Step 3/5 - Chunking transcript...")
        chunks = chunk_segments(segments)
        progress.progress(60)

        status.text("Step 4/5 - Generating embeddings...")
        embeddings = embed_chunks(chunks)
        progress.progress(80)

        status.text("Step 5/5 - Saving to vector store...")
        save_index(embeddings, chunks)
        progress.progress(100)

        status.text("")
        st.session_state.video_processed = True
        st.session_state.show_success = True
        st.session_state.question_asked = False

if st.session_state.video_processed:

    if st.session_state.show_success and not st.session_state.question_asked:
        st.success("Done! You can now ask questions.")

    st.write("---")
    question = st.text_input("Ask a question from the video")

    if question:
        st.session_state.question_asked = True

        with st.spinner("Finding answer..."):
            query_embedding = model.encode(question)
            relevant_chunks = search_index(query_embedding)
            answer = get_answer(question, relevant_chunks)

        st.subheader("Answer")
        st.write(answer)
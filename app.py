import streamlit as st
import os
from pipeline.extractor import extract_audio
from pipeline.transcriber import transcribe_audio
from pipeline.chunker import chunk_segments
from pipeline.embedder import embed_chunks, model
from pipeline.vector_store import save_index, search_index
from pipeline.qa_engine import get_answer

st.title("AI Teaching Assistant")
st.write("Upload a video and ask questions about its content!")

# VIDEO UPLOAD SECTION

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    video_path = f"upload/{uploaded_file.name}"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("Video uploaded successfully!")

    # PROCESS BUTTON

    if st.button("Process Video"):

    progress = st.progress(0, text="Starting...")

    audio_path = extract_audio(video_path)
    progress.progress(20, text="Audio extracted...")

    segments = transcribe_audio(audio_path)
    progress.progress(40, text="Audio transcribed...")

    chunks = chunk_segments(segments)
    progress.progress(60, text="Text chunked...")

    embeddings = embed_chunks(chunks)
    progress.progress(80, text="Embeddings created...")

    save_index(embeddings, chunks)
    progress.progress(100, text="Done!")

    st.success("Video processed! You can now ask questions.")

# QUESTION ANSWERING SECTION

if os.path.exists("vector_store/index.faiss"):
    
    st.write("---")
    question = st.text_input("Ask a question about the video content:")

    if question:

        with st.spinner("Finding answer..."):

            query.embedding = model.encode(question)
            relevant_chunks = search_index(query.embedding)
            answer = get_answer(question, relevant_chunks)

        st.subheader("Answer:")
        st.write(answer)
        


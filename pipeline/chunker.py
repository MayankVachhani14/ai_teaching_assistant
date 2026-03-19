def chunk_segments(segments, chunk_size=100):

    chunks = []
    current_text = ""
    current_start = None
    current_end = None

    for segment in segments:

        if current_start is None:
            current_start = segment["start"]

        current_text += " " + segment["text"]
        current_end = segment["end"]

        if len(current_text.split()) >= chunk_size:
            chunks.append({
                "text": current_text.strip(),
                "start": current_start,
                "end": current_end
            })
            current_text = ""
            current_start = None

    if current_text.strip():
        chunks.append({
            "text": current_text.strip(),
            "start": current_start,
            "end": current_end
        })

    return chunks
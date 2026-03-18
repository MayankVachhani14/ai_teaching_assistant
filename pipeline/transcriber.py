import whisper 
     
def transcribe_audio(audio_path):
     
    model = whisper.load_model("base")

    result = model.transcribe(audio_path)

    segments = []

    for segment in result["segments"]:
        segments.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        })       

    return segments
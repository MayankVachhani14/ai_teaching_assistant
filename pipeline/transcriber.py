import whisper 

#     
def transcribe_audio(audio_path):
    
    # Load the Whisper model
    model = whisper.load_model("base")

    # Transcribe the audio file
    result = model.transcribe(audio_path)

    # Extract the segments from the transcription result
    segments = []

    # Each segment contains the start time, end time, and the transcribed text
    for segment in result["segments"]:
        segments.append({
            "start": segment["start"],
            "end": segment["end"],
            "text": segment["text"]
        })       

    return segments
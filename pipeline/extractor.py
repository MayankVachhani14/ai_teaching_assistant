import moviepy.editor as mp
import os

def extract_audio(video_path):

    # Make sure data folder exists
    os.makedirs("data", exist_ok=True)

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    audio_path = os.path.join("data", f"{video_name}.wav")

    video = mp.VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path)
    video.close()

    return audio_path
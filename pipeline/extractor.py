import moviepy.editor as mp
import os  

def extract_audio(video_path):
    
    # we get the name of the video file without the extension to use it for naming the audio file
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # here we save the audio file in the data folder with the same name as the video but with .wav extension
    audio_path = f"data{video_name}.wav"

    # we use moviepy to load the video file and extract the audio, then we save it as a .wav file
    video = mp.VideoFileClip(video_path)

    # we write the audio to the specified path
    video.audio.write_audiofile(audio_path)

    video.close()

    return audio_path
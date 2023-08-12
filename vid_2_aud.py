from moviepy.video.io.VideoFileClip import VideoFileClip


def video_to_audio(input_video_path, output_audio_path):
    video_clip = VideoFileClip(input_video_path)
    audio_clip = video_clip.audio

    # Determine the file extension and use it in the output path
    ext = output_audio_path.split('.')[-1]
    if ext.lower() == "wav":
        audio_codec = "pcm_s16le"
    else:  # Assuming it's MP3 if not WAV
        audio_codec = "libmp3lame"
        if not output_audio_path.lower().endswith(".mp3"):
            output_audio_path += ".mp3"

    audio_clip.write_audiofile(output_audio_path, codec=audio_codec, fps=44100)

    video_clip.close()

from moviepy.editor import VideoFileClip, AudioFileClip

input_video_path = r"C:\Users\joshi\PycharmProjects\pythonProject\VoiceInputApp\vide1.mp4"
input_audio_path = r"C:\Users\joshi\PycharmProjects\pythonProject\VoiceInputApp\hindi.mp3"  # or "input_audio.wav"
output_video_path = r"C:\Users\joshi\PycharmProjects\pythonProject\VoiceInputApp\final_vidz.mp4"


def aud_vidz(input_video_path, input_audio_path, output_video_path):
    video_clip = VideoFileClip(input_video_path)
    audio_clip = AudioFileClip(input_audio_path)

    # Set the audio of the video clip to the loaded audio clip
    video_clip = video_clip.set_audio(audio_clip)

    # Write the new video clip with the added audio to the output path
    video_clip.write_videofile(output_video_path, codec="libx264")

    # Close the clips
    video_clip.close()
    audio_clip.close()

import subprocess


# Construct the FFmpeg command
def aud_spd(input_audio_path, output_audio_path):
    ffmpeg_command = [
        "ffmpeg",
        "-i", input_audio_path,
        "-filter:a", "atempo=1.3",
        output_audio_path
    ]

    # Run the FFmpeg command using subprocess
    try:
        subprocess.run(ffmpeg_command, check=True)
        print("Audio speed increased successfully.")
    except subprocess.CalledProcessError as e:
        print("Error occurred:", e)

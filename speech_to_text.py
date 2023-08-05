from pydub import AudioSegment

mp3_file_path = r'C:\Users\joshi\PycharmProjects\pythonProject\VoiceInputApp\sound.mp3'
audio = AudioSegment.from_mp3(mp3_file_path)

wav_file_path = r"C:\Users\joshi\PycharmProjects\pythonProject\VoiceInputApp\sound1.wav"
audio.export(wav_file_path, format='wav')
from pydub import AudioSegment


def convert_mp3_to_wav(mp3_file_path, wav_file_path):
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format='wav')


if __name__ == "__main__":
    convert_mp3_to_wav(mp3_file_path, wav_file_path)

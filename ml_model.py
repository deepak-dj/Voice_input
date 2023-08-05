import googletrans
import gtts
import playsound
import speech_recognition
from torch.utils.data import Dataset
from transformers import MarianMTModel, MarianTokenizer
from transformers import Seq2SeqTrainingArguments

import speech_to_text

input_lang = 'en'
output_lang = 'fr'


mp3_file_path = r"C:\Users\joshi\PycharmProjects\pythonProject\VoiceInputApp\sound.mp3"
wav_file_path = r"C:\Users\joshi\PycharmProjects\pythonProject\VoiceInputApp\sound1.wav"
speech_to_text.convert_mp3_to_wav(mp3_file_path, wav_file_path)
# demo_data_set
toy_dataset = [
    wav_file_path
]

# Prepare the training data
source_texts = [pair[0] for pair in toy_dataset]
target_texts = [pair[1] for pair in toy_dataset]

# Load the pre-trained MarianMT model and tokenizer
model_name = f"Helsinki-NLP/opus-mt-{input_lang}-{output_lang}"
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

# Tokenize the input and target texts for training
inputs = tokenizer.prepare_seq2seq_batch(src_texts=source_texts, tgt_texts=target_texts, return_tensors="pt")

# Only keep the necessary keys
inputs = {key: inputs[key] for key in ["input_ids", "attention_mask"]}

# Fine-tune the model on the toy dataset

training_args = Seq2SeqTrainingArguments(
    per_device_train_batch_size=4,
    num_train_epochs=1,
    save_steps=100,
    output_dir="./output",
    logging_dir="./logs",
    logging_steps=10,
)


# Create a custom evaluation dataset
class TranslationDataset(Dataset):
    def __init__(self, source_texts, tokenizer, target_texts=None):
        self.source_texts = source_texts
        self.tokenizer = tokenizer
        self.target_texts = target_texts

    def __len__(self):
        return len(self.source_texts)

    def __getitem__(self, idx):
        source_text = self.source_texts[idx]
        input_text_encoded = self.tokenizer(source_text, return_tensors="pt")
        return {
            "input_ids": input_text_encoded.input_ids.squeeze(),
            "attention_mask": input_text_encoded.attention_mask.squeeze(),
        }


# Prepare evaluation dataset
eval_dataset = TranslationDataset(source_texts, tokenizer)

# Test the fine-tuned model


def voice_input(wav_file_path):
    # wav_file_path = r'C:\Users\joshi\PycharmProjects\pythonProject\VoiceInputApp\sound1.wav'
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.AudioFile(wav_file_path) as source:
        audio_data = recognizer.record(source)
    input_text = recognizer.recognize_google(audio_data)
    input_text_encoded = tokenizer(input_text, return_tensors="pt")
    translated_ids = model.generate(input_text_encoded.input_ids, decoder_start_token_id=model.config.pad_token_id)
    translated_text = tokenizer.decode(translated_ids[0], skip_special_tokens=True)

    print("Converted Text:")
    print(input_text)

    translator = googletrans.Translator()
    translation = translator.translate(translated_text, dest=output_lang)
    print(translation.text)
    converted_audio = gtts.gTTS(translation.text, lang=output_lang)
    converted_audio.save('demo.mp3')
    playsound.playsound('demo.mp3')


voice_input(wav_file_path)

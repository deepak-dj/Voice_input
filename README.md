# Voice_input


1 - Importing Required Libraries:

googletrans: A Python library for translating text using Google Translate.
gtts (Google Text-to-Speech): A Python library and CLI tool to interface with Google Text-to-Speech API.
playsound: A pure Python implementation with no dependencies to play sound files.
speech_recognition: A library for performing speech recognition with various APIs.
torch.utils.data.Dataset: Part of the PyTorch library, used for creating custom datasets.
transformers: The Hugging Face Transformers library for natural language processing.
speech_to_text: Presumably a custom module containing functions for converting audio files.

2 - Defining Input and Output Languages:

input_lang = 'en': Specifies the input language as English.
output_lang = 'fr': Specifies the output language as French.

3 -File Paths:

mp3_file_path: Path to an MP3 audio file.
wav_file_path: Path to a WAV audio file.
The code converts the provided MP3 file to WAV format using the speech_to_text.convert_mp3_to_wav function.

4- Toy Dataset:

toy_dataset: A list containing paths to WAV files. This is used as a demo dataset for training.

5- Data Preparation:

source_texts: List of source text (WAV file paths) for training.
target_texts: List of target text (WAV file paths) for training.

6- Loading Pre-trained Model and Tokenizer:

model_name: Defines the model name based on the input and output languages.
model: Loads a pre-trained MarianMT model from the Hugging Face Transformers library.
tokenizer: Loads a tokenizer for the same model.

7- Tokenization and Preparation:

Tokenizes the input and target texts using the tokenizer.
Prepares the input data (source text and attention masks) for training.
Training Configuration:

training_args: Configuration settings for the training process, such as batch size, epochs, and output/logging directories.

8- Custom Evaluation Dataset:

Defines a custom dataset class named TranslationDataset for evaluation.
Implements methods like __init__, __len__, and __getitem__.
Evaluation Data Preparation:

Creates an instance of TranslationDataset for evaluation using the source texts and tokenizer.

9- Voice Input and Translation:

voice_input function processes the WAV file using the speech_recognition library to convert speech to text.
The obtained text is tokenized and translated using the pre-trained model and the Google Translate API.
The translated text is converted to speech using Google Text-to-Speech and played using playsound.

10- Calling the voice_input Function:

Finally, the voice_input function is called with the wav_file_path as an argument.
Keep in mind that this code might not run as-is, as there are some missing parts such as the actual implementation of speech_to_text.convert_mp3_to_wav and the missing assignment of target_texts. Additionally, there are some logic errors, like trying to access pair[1] in the toy dataset when the dataset only contains paths to WAV files (single-element pairs).






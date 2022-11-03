# OpenAI Whisper
import os, glob
import whisper
import nltk
nltk.download('punkt')

AUDIO_PATH = "./audio"
SAVE_PATH = "./transcription"

model = whisper.load_model("base")

try:
    os.mkdir(SAVE_PATH)
except FileExistsError:
    pass

for count, audio in enumerate(glob.glob(f"{AUDIO_PATH}/*.wav")):
    result = model.transcribe(audio, fp16=False)
    transcription = result["text"]
    sentence_splitted = nltk.tokenize.sent_tokenize(transcription)

    audio = audio.replace(f"{AUDIO_PATH}/", "")
    TRANSCRIBED_FILENAME = f"{SAVE_PATH}/{count+1}." + audio.split(".")[1] + "--transcribed.txt"

    try:
        with open(TRANSCRIBED_FILENAME, 'w') as f:
            for i, line in enumerate(sentence_splitted):
                if i != 0:
                    f.write(line)
                    f.write("\n")
                else:
                    f.write(line[1:])
                    f.write("\n")

    except FileExistsError:
        pass
# facebook/bart-large-cnn
import os, glob
from transformers import pipeline
import nltk
nltk.download('punkt')

DOC_PATH = "./transcription"
SAVE_PATH = "./summary"

try:
    os.mkdir(SAVE_PATH)
except FileExistsError:
    pass

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def return_summary(FILENAME):
    sentences = []
    with open(FILENAME) as f:
        content = f.readlines()

        for c in content:
            sentences.append(c.replace("\n", " "))
    
    content = " ".join(sentences)
    
    summary = summarizer(content, max_length=150, min_length=30, do_sample=False)[0]["summary_text"]
    return summary

for count, doc in enumerate(glob.glob(f"{DOC_PATH}/*.txt")):
    summary = return_summary(doc)
    sentence_splitted = nltk.tokenize.sent_tokenize(summary)

    doc = doc.replace(f"{DOC_PATH}/", "")
    SUMMARY_FILENAME = f"{SAVE_PATH}/{count+1}." + doc.split(".")[1].split("--transcribed")[0] + "--summary.txt"
    
    try:
        with open(SUMMARY_FILENAME, 'w') as f:
            for line in sentence_splitted:
                f.write(line)
                f.write("\n")
    
    except FileExistsError:
        pass
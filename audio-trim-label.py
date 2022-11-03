import os
from pydub import AudioSegment

AUDIO_FILENAME = "./andrewng-ml/andrew-ng-machine-learning.wav"
LABEL_FILENAME = "./andrewng-ml/label-details.txt"

file = AudioSegment.from_file(AUDIO_FILENAME)
SAVE_PATH = "./audio"

def cut_n_label(startMin, startSec, endMin, endSec, label, count):
    start = startMin*60*1000 + startSec*1000
    end = endMin*60*1000 + endSec*1000

    extract = file[start:end]
    try:
        os.mkdir(SAVE_PATH)
    except FileExistsError:
        pass

    filename = SAVE_PATH + "/" + f"{count}.{AUDIO_FILENAME.split('.')[0]}--{label}.wav"
    extract.export(filename, format="wav")

details = []
with open(LABEL_FILENAME) as f:
    content = f.readlines()

    for c in content:
        label, timeframe = c.split(",")
        start, end = timeframe.split("-")

        startMin, startSec = start.split(":")
        startMin, startSec = int(startMin), int(startSec)

        endMin, endSec = end.split(":")
        endMin, endSec = int(endMin), int(endSec)

        details.append([startMin, startSec, endMin, endSec, label])

count = 0
for d in details:
    count += 1
    startMin, startSec, endMin, endSec, label = d
    cut_n_label(startMin, startSec, endMin, endSec, label, count)
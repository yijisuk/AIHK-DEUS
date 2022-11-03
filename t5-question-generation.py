# mrm8488/t5-base-finetuned-question-generation-ap
import os
import glob
from transformers import AutoModelWithLMHead, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "mrm8488/t5-base-finetuned-question-generation-ap")
model = AutoModelWithLMHead.from_pretrained(
    "mrm8488/t5-base-finetuned-question-generation-ap")


def get_question(answer, context, max_length=64):
    input_text = "answer: %s  context: %s </s>" % (answer, context)
    features = tokenizer([input_text], return_tensors='pt')

    output = model.generate(input_ids=features['input_ids'],
                            attention_mask=features['attention_mask'],
                            max_length=max_length)

    return tokenizer.decode(output[0]).replace("<pad> question: ", "").replace("</s>", "")


KEYPH_PATH = "./keyphrases"
DOC_PATH = "./summary"
SAVE_PATH = "./questions/t5-questions"

try:
    os.makedirs(SAVE_PATH)
except FileExistsError:
    pass

count = 0
for keyphrase_path, doc_path in zip(glob.glob(f"{KEYPH_PATH}/*.txt"), glob.glob(f"{DOC_PATH}/*.txt")):
    count += 1

    with open(keyphrase_path) as f:
        keyphrase = f.readlines()

    sentences = []
    with open(doc_path) as f:
        content = f.readlines()

    for c in content:
        sentences.append(c.replace("\n", " "))

    content = " ".join(sentences)

    questions = []
    for i in range(len(keyphrase)):
        kphrase = keyphrase[i]
        question = get_question(kphrase, content)
        questions.append(question)

    doc = doc_path.replace(f"{DOC_PATH}/", "")
    QUESTION_FILENAME = f"{SAVE_PATH}/{count}." + \
        doc.split(".")[1].split("--summary")[0] + "--questions.txt"

    try:
        with open(QUESTION_FILENAME, 'w') as f:
            for question in questions:
                f.write(question)
                f.write("\n")

    except FileExistsError:
        pass

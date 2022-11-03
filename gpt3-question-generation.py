import os
import glob
import openai

openai.organization = "org-8N0WvHbxuFb28ynqvN9F2fG3"
openai.api_key = "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"

KEYPH_PATH = "./keyphrases"
DOC_PATH = "./summary"
SAVE_PATH = "./questions/gpt3-questions"

try:
    os.makedirs(SAVE_PATH)
except FileExistsError:
    pass


def get_question(answer, context):
    prompt = f"Given the context: {context},\ngenerate a question regarding {answer}. The question should only be relevant to the context.\nA:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.8,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0.1,
        presence_penalty=0.0
    )

    return response["choices"][0]["text"]


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

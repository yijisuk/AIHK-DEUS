import os
import glob
import openai

openai.organization = "org-8N0WvHbxuFb28ynqvN9F2fG3"
openai.api_key = "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"

DOC_PATH = "./summary"
SAVE_PATH = "./answers"

try:
    os.mkdir(SAVE_PATH)
except FileExistsError:
    pass

question = input("Input a question: ")


def get_answer(question, context):
    prompt = f"Given the context: {context},\nprovide an answer to the question: {question}\nA:"

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


context_list = []
for doc in glob.glob(f"{DOC_PATH}/*.txt"):
    sentences = []
    with open(doc) as f:
        content = f.readlines()

    for c in content:
        sentences.append(c.replace("\n", " "))

    content = " ".join(sentences)
    context_list.append(content)

context_sum = " ".join(context_list)

answer = get_answer(question, context_sum)

dir = os.listdir(f"{SAVE_PATH}/")
count = len(dir)
ANSWER_FILENAME = f"{SAVE_PATH}/qna-{count+1}.txt"
try:
    with open(ANSWER_FILENAME, 'w') as f:
        f.write(f"Q: {question}\n")
        f.write(f"A: {answer}")

except FileExistsError:
    pass

print(f"A: {answer}")

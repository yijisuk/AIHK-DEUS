# ml6team/keyphrase-generation-t5-small-openkp
import os
import glob
from transformers import Text2TextGenerationPipeline, AutoModelForSeq2SeqLM, AutoTokenizer


class KeyphraseGenerationPipeline(Text2TextGenerationPipeline):
    def __init__(self, model, keyphrase_sep_token=";", *args, **kwargs):
        super().__init__(
            model=AutoModelForSeq2SeqLM.from_pretrained(model),
            tokenizer=AutoTokenizer.from_pretrained(model),
            *args,
            **kwargs
        )
        self.keyphrase_sep_token = keyphrase_sep_token

    def postprocess(self, model_outputs):
        results = super().postprocess(
            model_outputs=model_outputs
        )
        return [[keyphrase.strip() for keyphrase in result.get("generated_text").split(self.keyphrase_sep_token) if keyphrase != ""] for result in results][0]


generator = KeyphraseGenerationPipeline(
    "ml6team/keyphrase-generation-t5-small-openkp")


def return_keyphrases(text):
    filtered = []
    for phrase in generator(text):
        if phrase not in filtered:
            filtered.append(phrase)

    return filtered


DOC_PATH = "./demo-outputs/summary"
SAVE_PATH = "./demo-outputs/keyphrases"

try:
    os.makedirs(SAVE_PATH)
except FileExistsError:
    pass

for count, doc in enumerate(glob.glob(f"{DOC_PATH}/*.txt")):
    sentences = []
    with open(doc) as f:
        content = f.readlines()

        for c in content:
            sentences.append(c.replace("\n", " "))

    content = " ".join(sentences)

    keyphrases = return_keyphrases(content)

    doc = doc.replace(f"{DOC_PATH}/", "")
    KEYPHRASE_FILENAME = f"{SAVE_PATH}/{count+1}." + \
        doc.split(".")[1].split("--summary")[0] + "--keyphrase.txt"

    try:
        with open(KEYPHRASE_FILENAME, 'w') as f:
            f.write(f"{keyphrases}")

    except FileExistsError:
        pass

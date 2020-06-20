import json
import os
from random import sample

from uploading import upload

CAT_IMG = "cat.jpeg"
PROMPT = "prompt.txt"
RESPONSE = "text-response.txt"
HASHTAGS = "hashtags.txt"
PARAGRAPHS = 4


def getText() -> str:
    with open(RESPONSE, "r") as f:
        response = json.load(f)

    with open(PROMPT, "r") as f:
        prompt = f.read()

    text = response['output']
    noPrompt = text[len(prompt):]
    finalText = "\n\n".join(noPrompt.split("\n\n")[:PARAGRAPHS])

    return finalText


def getTags() -> str:
    with open(HASHTAGS, "r") as f:
        tagStr = f.read()
    tags = list(set(tagStr.split()))
    finalTags = sample(tags, 29)

    return " ".join(finalTags)


if __name__ == "__main__":
    dsc = getText() + "   \n\n" + getTags()
    upload(dsc, CAT_IMG)
    print("uploaded")
    os.system("./cats.sh")
    print("prepared")

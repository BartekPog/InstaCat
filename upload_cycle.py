import json
import subprocess
from random import sample

from uploading import upload

CAT_IMG = "cat.jpeg"
PROMPT = "prompt.txt"
RESPONSE = "text-response.txt"
HASHTAGS = "hashtags.txt"
BANNED = "banned-words.txt"
RELOAD_SCRIPT = "reload.sh"
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


def reloadScript():
    subprocess.run(["./"+RELOAD_SCRIPT])

    with open(BANNED, "r") as f:
        swearWords = f.read().lower().split()

    text = getText()

    while any([word in swearWords for word in text.split()]):
        print("reloading")
        subprocess.run(["./"+RELOAD_SCRIPT])


def fullCycle():
    dsc = getText() + "   \n\n" + getTags()
    print("Uploading")
    upload(dsc, CAT_IMG)

    print("Preparing for next upload")
    reloadScript()


if __name__ == "__main__":
    fullCycle()
    # print("done")

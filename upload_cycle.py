import json
import subprocess
from random import sample, randint
from credentials import api_key

from uploading import upload

CAT_IMG = "data/cat.jpeg"
PROMPT = "data/prompt.txt"
RESPONSE = "data/text-response.txt"
HASHTAGS = "data/hashtags.txt"
BANNED = "data/banned-words.txt"
RELOAD_SCRIPT = "reload.sh"
PARAGRAPHS = 2


def getPrompt() -> str:
    with open(PROMPT, "r") as f:
        prompt = f.read()

    try:
        with open(RESPONSE, "r") as f:
            response = json.load(f)

        prevPrompt = response['output'].split(".")[0]+"."

    except:
        prevPrompt = "This kitten is adoreable. isn't it?"+" "*randint(0, 7)

    return " ".join([prevPrompt, prompt])


def getScriptString() -> str:
    return ["./"+RELOAD_SCRIPT, api_key, getPrompt(), RESPONSE, CAT_IMG]


def getText() -> str:
    prompt = getPrompt()

    try:
        with open(RESPONSE, "r") as f:
            response = json.load(f)

        text = response['output']
    except:
        reloadScript()
        with open(RESPONSE, "r") as f:
            response = json.load(f)

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
    subprocess.run(getScriptString())

    with open(BANNED, "r") as f:
        swearWords = f.read().lower().split()

    text = getText()

    while any([word in swearWords for word in text.split()]):
        print("reloading")
        subprocess.run(getScriptString())


def fullCycle():
    dsc = getText() + "   \n\n" + getTags()
    print("Uploading")
    upload(dsc, CAT_IMG)

    print("Preparing for next upload")
    reloadScript()


if __name__ == "__main__":
    fullCycle()
    print("done")

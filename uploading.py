from credentials import username, password
from instabot import Bot


def upload(description: str, img: str):
    bot = Bot()
    bot.login(username=username, password=password)
    bot.upload_photo(img, caption=description)

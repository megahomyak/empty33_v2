from configparser import ConfigParser

_secrets_parser = ConfigParser()
_secrets_parser.read("vk/vk_secret_constants.ini", encoding="utf-8")

_public_parser = ConfigParser()
_public_parser.read("vk/vk_public_constants.ini", encoding="utf-8")


_secrets_sector = _secrets_parser["SECRETS"]
TOKEN = _secrets_sector["token"]


_public_sector = _public_parser["PUBLIC"]
GROUP_ID = int(_public_sector["group_id"])
TAG = _public_sector["tag"]
SYMBOLS_LIMIT = int(_public_sector["symbols_limit"])
CHAT_ERROR_MESSAGE = _public_sector["chat_error_message"]


with open("simple_replies.txt", "r", encoding="utf-8") as f:
    SIMPLE_REPLIES = list(filter(None, f.read().split("\n")))

with open("replies_with_tag.txt", "r", encoding="utf-8") as f:
    REPLIES_WITH_TAG = list(filter(None, f.read().split("\n")))

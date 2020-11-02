from configparser import ConfigParser


_config_parser = ConfigParser()
_config_parser.read("vk/vk_constants.ini", encoding="utf-8")


_secrets_sector = _config_parser["SECRETS"]

TOKEN = _secrets_sector["token"]
GROUP_ID = int(_secrets_sector["group_id"])


_public_sector = _config_parser["PUBLIC"]

TAG = _public_sector["tag"]
SYMBOLS_LIMIT = int(_public_sector["symbols_limit"])

REPLIES = [text.strip() for text in _public_sector["replies"].split("|")]

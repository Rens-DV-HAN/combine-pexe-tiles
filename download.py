import json
from pathlib import Path
from typing import TypedDict

import requests


# Minimal version of https://discord.com/developers/docs/resources/message#attachment-object-attachment-structure
class Attachment(TypedDict):
    id: str
    filename: str
    url: str


# Minimal version of https://discord.com/developers/docs/resources/message#message-object-message-structure
class Message(TypedDict):
    attachments: list[Attachment]
    id: str


def message_has_tile(message: Message):
    return message["attachments"] and message["id"] not in [
        "1373983902720589865",
        "1379735067722518558",
        "1379734692491825163",
        "1376501204066111530",
        "1375035016555397181",
        "1374016601770168404",
        "1374016328746401842",
    ]


def get_file_extension(filename: str):
    return filename[filename.rindex(".") :]


def download_tile_from_message(message: Message):
    if not message_has_tile(message):
        return

    for attachment in message["attachments"]:
        attachment_response = requests.get(attachment["url"])
        if attachment_response.status_code != 200:
            raise requests.exceptions.HTTPError(
                f"Unexpected non-200 status code ({attachment_response.status_code})",
                response=attachment_response,
            )

        attachment_file_extension = get_file_extension(attachment["filename"])
        with open(
            f"tiles/{attachment["id"]}{attachment_file_extension}", "wb"
        ) as attachment_file:
            attachment_file.write(attachment_response.content)


def download_tiles_from_messages():
    for messages_file in Path("messages").iterdir():
        messages_file_text = messages_file.read_text()
        messages = json.loads(messages_file_text)
        for message in messages:
            download_tile_from_message(message)

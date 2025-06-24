# combine-pexe-tiles

A Python project to combine images of tiles made during the project "PEXE" of the study program "HBO-ICT" at the HAN University of Applied Sciences in semester 2 of academic year 2024-2025, into a single image.

## Prerequisites

- Python 3.13+ (not tested on older versions)

## Setup

### Virtual environment

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
3. Install the required packages: `pip install -r requirements.txt`

### (Optional) Messages

In order to download the tiles from the Discord messages, they must be obtained first. How you do this is up to you.

One obvious way to do it would be to use [their API](https://discord.com/developers/docs/resources/message#get-channel-messages). This seems however, without a bot, [not possible](https://www.postman.com/discord-api/discord-api/request/o94fnbu/list-messages?tab=overview).

One way that does work is to open the [#tegeltjes channel](https://discord.com/channels/1283383422139498547/1345014046981885952) in your browser with the network tab of the developer tools open and keep track of all requests to `/api/.../messages`.

However you do it, place the [message objects](https://discord.com/developers/docs/resources/message#message-object-message-structure) in one or multiple `.json` files in the [`/messages`](/messages) folder.

### (Optional) Tiles

If you already have the tile images, you can place them in the [`/tiles`](/tiles) folder.

## Usage

### (Optional) Download the tiles from the messages

Running `python download.py` will iterate over all `.json` files in `/messages` and download all their tile attachments to the [`/tiles`](/tiles) folder.

> [!NOTE]
> The URLs of message attachments expire after a certain period of time. Make sure to run `download.py` shortly after you have obtained the messages.

### Make sure the amount of tiles is equal to the amount the grid expects

The main function in `main.py` uses a 9x9 grid (except the center 3x3) to place the tiles in, so it expects `(9 * 9) - (3 * 3)` = 72 tiles. Make sure this matches the amount of files in [`/tiles`](/tiles). If it doesn't, consider moving some tiles to [`/tiles/ignore`](/tiles/ignore).

### Combine the tiles into a single image

Running `python main.py` will iterate over all files in `/tiles` (excluding subfolders) and combine them by placing them in a 9x9 grid, keeping the center 3x3 empty to place your own text or image. The resulting image will be written to [`result.png`](result.png).

## Testing

A set of test tiles is available in [`/tiles/test`](/tiles/test). These can be used by importing them in [`main.py`](main.py) (`from test_data import test_tiles`) and replacing the value of the `tiles` variable with `test_tiles`.

## License

This project is licensed under the [MIT license](LICENSE.md).

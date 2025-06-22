from statistics import mean
from typing import Iterable

from PIL import Image

from download import download_tiles_from_messages
from test_data.test_data import test_tiles
from type_aliases import FileOrFilePath


def get_average_tile_size(tiles: Iterable[FileOrFilePath]):
    average_tile_sizes = (mean(Image.open(tile).size) for tile in tiles)
    return round(mean(average_tile_sizes))


def main():
    # download_tiles_from_messages()
    tiles = test_tiles

    average_tile_size = get_average_tile_size(tiles)


if __name__ == "__main__":
    main()

from itertools import product
from statistics import mean
from typing import Iterable

from PIL import Image, ImageOps

from download import download_tiles_from_messages
from test_data.test_data import test_tiles
from type_aliases import FileOrFilePath


def get_average_tile_size(tiles: Iterable[FileOrFilePath]):
    average_tile_sizes = (mean(Image.open(tile).size) for tile in tiles)
    return round(mean(average_tile_sizes))


def get_offset_to_center(outer_size: int, inner_size: int):
    return (outer_size - inner_size) // 2


def get_cell_content_coordinate_to_center(
    dimension_index: int, cell_size: int, content_size: int
):
    return dimension_index * cell_size + get_offset_to_center(
        cell_size, content_size
    )


def paste_tile_image_on_image(
    image: Image.Image,
    tile_image: Image.Image,
    cell: tuple[int, int],
    cell_size: int,
):
    (row, column) = cell

    fitting_tile_image = ImageOps.contain(tile_image, (cell_size, cell_size))
    fitting_tile_image_coordinates = (
        get_cell_content_coordinate_to_center(
            column, cell_size, fitting_tile_image.width
        ),
        get_cell_content_coordinate_to_center(
            row, cell_size, fitting_tile_image.height
        ),
    )

    image.paste(fitting_tile_image, fitting_tile_image_coordinates)


def main():
    # download_tiles_from_messages()
    tiles = test_tiles

    cell_size = get_average_tile_size(tiles)
    grid_size = 9
    image_size = (cell_size * grid_size, cell_size * grid_size)

    WHITE = (255, 255, 255)
    image = Image.new("RGB", image_size, WHITE)

    # TODO strict to True?
    for cell, tile in zip(product(range(grid_size), range(grid_size)), tiles):
        with Image.open(tile) as tile_image:
            paste_tile_image_on_image(image, tile_image, cell, cell_size)

    image.save("result.png")


if __name__ == "__main__":
    main()

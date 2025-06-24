from statistics import mean, median
from typing import Iterable

from PIL import Image, ImageOps

from test_data.test_data import test_tiles
from type_aliases import FileOrFilePath


def get_median_tile_size(tiles: Iterable[FileOrFilePath]):
    average_tile_sizes: list[int | float] = []
    for tile in tiles:
        with Image.open(tile) as tile_image:
            average_tile_sizes.append(mean(tile_image.size))

    return round(median(average_tile_sizes))


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
    tiles = test_tiles

    cell_size = get_median_tile_size(tiles)
    GRID_SIZE = 9
    image_size = (cell_size * GRID_SIZE, cell_size * GRID_SIZE)

    WHITE = (255, 255, 255)
    image = Image.new("RGB", image_size, WHITE)

    dimension_indexes = (
        (row, column)
        for row in range(GRID_SIZE)
        for column in range(GRID_SIZE)
        if not (3 <= row <= 5 and 3 <= column <= 5)  # center 3x3 empty
    )
    for cell, tile in zip(dimension_indexes, tiles, strict=True):
        with Image.open(tile) as tile_image:
            paste_tile_image_on_image(image, tile_image, cell, cell_size)

    image.save("result.png")


if __name__ == "__main__":
    main()

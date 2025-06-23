from itertools import cycle, islice
from pathlib import Path

test_tiles = list(islice(cycle(Path("test_data/tiles").iterdir()), 81))

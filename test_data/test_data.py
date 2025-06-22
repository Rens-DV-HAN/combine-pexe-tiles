from itertools import cycle, islice
from pathlib import Path

test_tiles = islice(cycle(Path("test_data/tiles").iterdir()), 81)

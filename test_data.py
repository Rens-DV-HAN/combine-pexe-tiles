from itertools import cycle, islice
from pathlib import Path

test_tiles = list(islice(cycle(Path("tiles/test").iterdir()), 72))

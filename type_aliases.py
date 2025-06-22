import os
from typing import IO

type FileOrFilePath = str | bytes | os.PathLike[str] | os.PathLike[bytes] | IO[
    bytes
]

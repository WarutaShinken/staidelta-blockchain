import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("STAIDELTA_ROOT", "~/.staidelta/mainnet"))).resolve()

DEFAULT_KEYS_ROOT_PATH = Path(os.path.expanduser(os.getenv("STAIDELTA_KEYS_ROOT", "~/.staidelta_keys"))).resolve()

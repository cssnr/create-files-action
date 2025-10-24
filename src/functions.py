from pathlib import Path


def write_file(file: str, string: str, mkdir: bool = False):
    path = Path(file)
    if mkdir and not path.parent.exists():
        print(f"makedirs: \033[33m{path.parent}")
        path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        print(f"write: \033[33m{file}")
        f.write(string)

from pathlib import Path


def get_input_file(file: str) -> str:
    src_dir: Path = Path(file).parent
    input_path: Path = src_dir / "input.txt"

    return input_path.read_text(encoding="utf-8").strip()

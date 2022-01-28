from .utils import get_repository_datafolder


def open_tiny_shakespeare() -> str:
    shkspr_folder = get_repository_datafolder() / "shakespeare"

    return (shkspr_folder / "shakespeare.txt").read_text()

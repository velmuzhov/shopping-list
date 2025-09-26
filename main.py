from pathlib import Path
from datetime import date
from config import DEST

BASE_DIR = Path(__file__).parent

def getting_date() -> str:
    return date.today().strftime("%y%m%d")

def splitting_source(path: Path) -> list[str]:
    with open(path) as file:
        return file.read().lower().strip().split(",")
         
def write_output(path: Path, items: list[str]) -> None:
    with open(path, "w") as file:
        file.write(f"# {getting_date()}\n\n")
        for item in items:
            file.write(f"- [ ] {item}\n")


def main():
    write_output(
        path=Path(DEST / getting_date()).with_suffix(".md"),
        items=splitting_source(path=Path(BASE_DIR / "source.txt"))
    )

if __name__ == "__main__":
    main()

import re

KEYWORDS: list[str] = ["START", "HALT", "STATE", "LOOP", "STATEMENT"]

class Scanner:
    def __init__(self) -> None:
        self._source_code: str = ""
        self._tokens: list[str] = []
        self._current_idx: int = 0

    def load_source_code(self, file_path: str) -> None:
        with open(file_path, "r") as file:
            self._source_code = file.read()

    def get_next_character(self) -> str:
        if self._current_idx >= len(self._source_code):
            return ""
        character: str = self._source_code[self._current_idx]
        self._current_idx += 1
        return character
    
    def output_source_code(self) -> None:
        print(self._source_code)


def main():
    scanner: Scanner = Scanner()
    scanner.load_source_code("language.txt")
    scanner.output_source_code()

if __name__ == "__main__":
    main()
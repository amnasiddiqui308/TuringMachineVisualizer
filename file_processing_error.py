class FileProcessingException(Exception):
    def __init__(self, message: str, filename: str, line: int) -> None:
        super().__init__(message)
        self.message = message
        self.filename: str = filename
        self.line: int = line

    def __str__(self):
        return f"{self.message} in {self.filename} at line {self.line}"


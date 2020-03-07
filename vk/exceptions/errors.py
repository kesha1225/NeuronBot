class APIException(Exception):
    def __init__(self, code: int, text: str):
        self.code = code
        self.text = text
        self.message = f"[{self.code}] {self.text}"
        super().__init__(self.message)


class KeyboardException(Exception):
    pass

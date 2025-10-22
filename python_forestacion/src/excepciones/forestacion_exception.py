class ForestacionException(Exception):
    """Excepción base para el sistema de forestación"""

    def __init__(self, error_code: str, message: str):
        super().__init__(message)
        self._error_code = error_code
        self._user_message = message

    def get_error_code(self) -> str:
        return self._error_code

    def get_user_message(self) -> str:
        return self._user_message

    def get_full_message(self) -> str:
        return f"[{self._error_code}] {self._user_message}"
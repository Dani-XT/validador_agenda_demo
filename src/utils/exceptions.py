class AppError(Exception):
    default_title = "Error"
    default_level = "error"

    def __init__(self, message: str | None = None):
        self.message = message or "Ocurrió un error inesperado."
        super().__init__(self.message)

    @property
    def title(self) -> str:
        return self.default_title

    @property
    def level(self) -> str:
        return self.default_level

    def __str__(self) -> str:
        return self.message
    

class RUTInvalidoError(AppError):
    default_title = "RUT Invalido"

class BadStatusError(AppError):
    default_title = "Error en respuesta"

class HelpFileNotFoundError(AppError):
    default_title = "Archivo no encontrado"

class HelpFileOpenError(AppError):
    default_title = "Error al abrir ayuda"
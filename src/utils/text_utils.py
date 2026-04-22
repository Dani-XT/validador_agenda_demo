from src.utils.exceptions import RUTInvalidoError
from src.models.consulta_paciente import ESTADOS_AGENDA
import re

def validar_rut(rut: str) -> str:
    # Acepta RUT sin puntos ni guión (ej: 123456789)
    if rut is None:
        raise RUTInvalidoError("Debes ingresar un RUT.")

    rut = rut.strip().upper().replace(" ", "")

    if not rut:
        raise RUTInvalidoError("Debes ingresar un RUT.")

    # Quitar puntos y guiones por si el usuario copia desde otro lado
    rut = rut.replace(".", "").replace("-", "")

    # Un RUT chileno limpio tiene entre 7 y 9 caracteres (6-8 dígitos + 1 DV)
    if len(rut) < 7 or len(rut) > 9:
        raise RUTInvalidoError("El RUT debe tener entre 7 y 9 caracteres (sin puntos ni guión). Ej: 123456789")

    cuerpo = rut[:-1]
    dv = rut[-1]

    if not cuerpo.isdigit():
        raise RUTInvalidoError("El RUT debe contener solo números seguido del dígito verificador. Ej: 123456789")

    if not (dv.isdigit() or dv == "K"):
        raise RUTInvalidoError("El dígito verificador debe ser un número o la letra K.")

    return f"{cuerpo}-{dv}"

def format_nombre(value: str) -> str:
    if not value:
        return ""
    
    return " ".join(word.capitalize() for word in value.strip().lower().split())


def format_correo(value: str) -> str:
    if not value:
        return ""
    
    return value.strip().lower()


def format_telefono_cl(value: str) -> str:
    if not value:
        return ""
    
    digits = re.sub(r"\D", "", value)

    # caso esperado desde tu API: 938905286
    if len(digits) == 9 and digits.startswith("9"):
        return f"+56 {digits[0]} {digits[1:5]} {digits[5:]}"
    
    # por si algún día viene con 56 incluido
    if len(digits) == 11 and digits.startswith("569"):
        return f"+56 {digits[2]} {digits[3:7]} {digits[7:]}"
    
    return value.strip()


def format_estado(codigo: int | str) -> str:
    try:
        return ESTADOS_AGENDA.get(int(codigo), str(codigo))
    except (ValueError, TypeError):
        return str(codigo)


def format_rut_display(value: str) -> str:
    if not value:
        return ""
    
    rut = re.sub(r"[^0-9Kk]", "", value).upper()

    if len(rut) < 2:
        return value.strip()

    cuerpo = rut[:-1]
    dv = rut[-1]

    # 7 dígitos + dv => total 8
    if len(rut) == 8:
        return f"{cuerpo[0]}.{cuerpo[1:4]}.{cuerpo[4:]}-{dv}"

    # 8 dígitos + dv => total 9
    if len(rut) == 9:
        return f"{cuerpo[:2]}.{cuerpo[2:5]}.{cuerpo[5:]}-{dv}"

    return value.strip()
from dataclasses import dataclass
from typing import Optional

from datetime import date, time


@dataclass(slots=True)
class Paciente:
    nombre: str
    apellido: str
    rut: str
    telefono: str
    correo: str

    @property
    def get_name(self):
        return f'{self.nombre} {self.apellido}'
    
@dataclass(slots=True)
class Agenda:
    fecha: date | str
    hora: time | str
    estado: int | str

@dataclass(slots=True)
class ConsultaPaciente:
    paciente: Paciente
    agenda: Optional[Agenda] = None

ESTADOS_AGENDA: dict[int, str] = {
    47: "No Confirmado",
    48: "Confirmado",
    50: "Confirmado por E-mail",
    51: "Cancelado por E-mail",
}
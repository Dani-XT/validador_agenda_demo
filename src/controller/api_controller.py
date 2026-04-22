import logging

from src.services.api_service import ApiService

from src.models.consulta_paciente import ConsultaPaciente

from src.utils.text_utils import validar_rut

logger = logging.getLogger(__name__)

class ApiController:
    def __init__(self):
        self.service = ApiService()

    def start(self, rut: str) -> ConsultaPaciente | None:
        logger.info("Iniciando consulta de paciente %s", rut)
        # Validaciones
        rut = validar_rut(rut)

        # consulta
        return self.service.consultar_paciente(rut)
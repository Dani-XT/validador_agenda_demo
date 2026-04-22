import logging
import requests

from src.core.app_context_store import get_app_config

from src.models.consulta_paciente import (
    ConsultaPaciente,
    Paciente,
    Agenda,
)

from src.utils.datatime_utils import split_datetime

from src.utils.exceptions import BadStatusError

logger = logging.getLogger(__name__)

class ApiService:

    def consultar_paciente(self, rut) -> ConsultaPaciente:
        config = get_app_config()

        url = config.app_url_api
        token = config.app_token_api

        headers = self._build_headers(token)
        body = self._build_body(rut)

        response = requests.post(url, headers=headers, data=body)
        data = response.json()

        if response.status_code != 200:
            error_msg = data.get("error", f"Error de respuesta {response.status_code}")
            logging.error("Error al realizar consulta %s: %s", response.status_code, error_msg)
            raise BadStatusError(error_msg)
        
        logging.info("Consulta realizada exitosamente %s", response.status_code)

        a_data = data.get("AGENDA", {})
        p_data = data.get("PACIENTE", {})

        logger.info("Obteniendo datos del paciente")
        paciente = Paciente(
            nombre = p_data.get("NOMBRE", ""),
            apellido = p_data.get("APELLIDO", ""),
            rut = p_data.get("RUT", ""),
            telefono = a_data.get("TELEFONO", ""),
            correo = p_data.get("EMAIL", ""),
        )

        fecha, hora = split_datetime(a_data.get("FECHA"))

        logger.info("Obteniendo datos de la agenda")
        agenda = Agenda(
            fecha = fecha or "",
            hora = hora or "",
            estado = int(a_data.get("ESTADO")) or "",
        )

        return ConsultaPaciente(agenda=agenda, paciente=paciente)


    def _build_headers(self, token: str):
        return { 
            'Authorization': f'Bearer {token}', 
            'Content-Type': 'application/x-www-form-urlencoded' 
        }
    
    def _build_body(self, rut: str):
        return {
            'rut': rut
        }
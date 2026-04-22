import os
import logging
from pathlib import Path

from src.core.app_context import AppContext

from src.controller.api_controller import ApiController

from src.ui.views.home_view import HomeView

from src.utils.text_utils import (
    format_nombre,
    format_rut_display,
    format_telefono_cl,
    format_correo,
    format_estado,
)
from src.utils.exceptions import HelpFileNotFoundError, HelpFileOpenError

logger = logging.getLogger(__name__)

class HomeController:
    def __init__(self, app_context: AppContext):
        self.context = app_context
        self.api_controller: ApiController = ApiController()

        self.paths = app_context.runtime

    def on_search_rut(self, view: HomeView):
        rut = view.get_rut_input()

        if not rut:
            view.show_error_message("RUT requerido", "Debes ingresar un RUT para realizar la busqueda.")
            return

        view.clear_outputs()
        view.show_loading_message("Consultando", "Consultando paciente...")

        try:
            result = self.api_controller.start(rut)

            if result is None:
                view.show_patient_not_found()
                return

            paciente = result.paciente
            agenda = result.agenda

            logger.info("Mostrando datos del paciente")
            view.set_patient_data(
                nombre=format_nombre(paciente.get_name),
                rut=format_rut_display(paciente.rut),
                telefono=format_telefono_cl(paciente.telefono),
                correo=format_correo(paciente.correo),
            )

            logger.info("Mostrando datos de la agenda")
            if agenda is not None:
                view.set_agenda_data(
                    fecha=agenda.fecha.strftime("%d-%m-%Y"),
                    hora=agenda.hora.strftime("%H:%M"),
                    estado=format_estado(agenda.estado),
                )

            view.clear_rut_input()

        except Exception as e:
            view.clear_rut_input()
            logger.error("Ocurrio un error %s", str(e))
            view.show_error_message("Error", f"Ocurrió un error al consultar.\n\n{e}")

        finally:
            view.hide_loading_message()

    def on_open_help(self):
        self._open_help_file(self.paths.consultar_readme_file)

    def _open_help_file(self, help_file: Path) -> None:
        if not help_file.exists():
            raise HelpFileNotFoundError("No se encontró el archivo de ayuda.")

        try:
            os.startfile(help_file)
        except Exception as e:
            raise HelpFileOpenError(f"Ocurrió un error al abrir el archivo:\n{e}") from e


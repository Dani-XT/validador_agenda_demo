# Consultar agenda pacientes

Aplicación de escritorio desarrollada en **Python + Tkinter** para consultar información de pacientes y su agenda clínica a partir del **RUT**, consumiendo una API externa y mostrando los resultados en una interfaz simple y visual.

## Descripción

Este sistema permite ingresar el RUT de un paciente, consultar sus datos mediante una API y desplegar en pantalla la siguiente información:

- **Paciente**
  - Nombre
  - RUT
  - Teléfono
  - Correo

- **Agenda**
  - Fecha
  - Hora
  - Estado

Si el paciente no existe o no hay información asociada al RUT ingresado, el sistema muestra un mensaje de error en pantalla.

---

## Objetivo del proyecto

El objetivo principal de esta aplicación es facilitar la validación rápida de agendas de pacientes desde una interfaz amigable, evitando consultas manuales y centralizando la información relevante en una sola pantalla.

---

## Características principales

- Interfaz gráfica construida con **Tkinter**
- Consulta de paciente por **RUT**
- Integración con API externa
- Visualización separada de datos de **paciente** y **agenda**
- Mensajes de error visuales mediante diálogos personalizados
- Carga de configuración desde variables de entorno
- Estructura modular basada en:
  - `views`
  - `controllers`
  - `services`
  - `models`

---

## Arquitectura del proyecto

El proyecto sigue una separación por responsabilidades para evitar acoplamiento innecesario entre la UI y la lógica de negocio.

### Capas principales

#### UI / Frames
Responsables de construir la interfaz gráfica, capturar entradas del usuario y mostrar resultados.

#### Views
Definen el contrato que la UI expone al controlador.

#### Controllers
Orquestan el flujo entre la vista y los servicios.

#### Services
Encapsulan la lógica de integración con la API y la transformación de datos.

#### Models
Representan la información del dominio, por ejemplo:
- `Paciente`
- `Agenda`
- `ConsultaPaciente`

---

## Flujo general

1. El usuario ingresa el **RUT** en la pantalla principal.
2. La vista envía la acción al `HomeController`.
3. El `HomeController` valida la entrada y delega la consulta al `ApiController`.
4. El `ApiController` llama al `ApiService`.
5. El `ApiService` consulta la API externa, transforma la respuesta y construye los modelos.
6. El `HomeController` recibe el resultado y actualiza la vista.
7. Si no existe información, la vista muestra un modal de error.

---

## Estructura sugerida del proyecto

```bash
src/
├── app/
│   ├── bootstrap.py
│   ├── config.py
│   ├── env.py
│   └── paths.py
├── controller/
│   ├── home_controller.py
│   └── api_controller.py
├── core/
│   ├── app_context.py
│   ├── app_context_store.py
│   └── exception_handler.py
├── models/
│   └── consulta_paciente.py
├── services/
│   └── api_service.py
├── ui/
│   ├── components/
│   │   ├── dialogs.py
│   │   ├── error_dialog.py
│   │   └── tooltip.py
│   ├── frames/
│   │   ├── base_frame.py
│   │   └── home_frame.py
│   ├── views/
│   │   ├── base_view.py
│   │   └── home_view.py
│   └── main_window.py
├── utils/
│   └── datatime_utils.py
└── main.py
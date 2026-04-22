import tkinter as tk

from src.ui.frames.base_frame import BaseFrame

from src.core.app_context import AppContext

from src.controller.home_controller import HomeController

class HomeFrame(BaseFrame):
    def __init__(self, master, context: AppContext, page_controller: HomeController):
        super().__init__(master, context, bg="#72B2E6")
        self.controller = page_controller

        self._init_output_vars()
        self._load_assets()
        self._build_header()
        self._build_body()

        self.after(100, lambda: self.rut_entry.focus_set())

    def _init_output_vars(self):
        self.nombre_var = tk.StringVar(value="")
        self.rut_var = tk.StringVar(value="")
        self.telefono_var = tk.StringVar(value="")
        self.correo_var = tk.StringVar(value="")

        self.fecha_var = tk.StringVar(value="")
        self.hora_var = tk.StringVar(value="")
        self.estado_var = tk.StringVar(value="")

    def _load_assets(self):
        frame_img_dir = self.paths.img_dir / "home_frame"

        self.input_img = tk.PhotoImage(file = frame_img_dir / "input.png")
        self.logo_img = tk.PhotoImage(file = frame_img_dir / "logo.png")
        self.help_img = tk.PhotoImage(file = frame_img_dir / "helper.png")
        self.enviar_img = tk.PhotoImage(file = frame_img_dir / "enviar.png")

        # paciente
        self.paciente_logo_img = tk.PhotoImage(file = frame_img_dir / "paciente.png")
        self.paciente_img = tk.PhotoImage(file = frame_img_dir / "paciente_frame.png")

        # agenda
        self.agenda_logo_img = tk.PhotoImage(file = frame_img_dir / "agenda.png")
        self.agenda_img = tk.PhotoImage(file = frame_img_dir / "agenda_frame.png")

        # labels
        self.label_1_img = tk.PhotoImage(file = frame_img_dir / "label_1.png")
        self.label_2_img = tk.PhotoImage(file = frame_img_dir / "label_2.png")
        self.label_3_img = tk.PhotoImage(file = frame_img_dir / "label_3.png")
        self.label_4_img = tk.PhotoImage(file = frame_img_dir / "label_4.png")

    def _build_header(self):
        header = tk.Frame(self, bg="white", height=97)
        header.place(x=0, y=0, relwidth=1)

        logo_label = tk.Label(header, image=self.logo_img, bg="white", bd=0)
        logo_label.place(x=10, y=15)

        tk.Label(header, anchor="nw", text="Ingrese el RUT del Paciente:", font=("MontserratRoman Medium", 18 * -1), bg="white").place(x=219, y=24)
        help_btn = tk.Button(header, image=self.help_img, bg="white", activebackground="white", borderwidth=0, highlightthickness=0, relief="flat", cursor="hand2", command= self.controller.on_open_help)
        help_btn.place(x=455, y=27)

        input_label = tk.Label(header, image=self.input_img, bg="white", bd=0)
        input_label.place(x=215, y=50)

        self.rut_entry = tk.Entry(header, bd=0, bg="#E9D2D6", fg="#000716", highlightthickness=0, width=35, font=("Segoe UI", 12, "bold"))
        self.rut_entry.place(x=230, y=55, height=20)
        self.rut_entry.bind("<Return>", self._enter_search_rut)

        enviar_btn = tk.Button(image=self.enviar_img, bg="white", activebackground="white", borderwidth=0, command=lambda: self.controller.on_search_rut(self), cursor="hand2",)
        enviar_btn.place(x=600, y=50)

    def _build_body(self):

        body = tk.Frame(self, bg="#72B2E6")
        body.place(x=0, y=97, relwidth=1, relheight=1, height=-97)


        # TODO: Paciente
        tk.Label(body, image=self.paciente_logo_img, bg="#72B2E6", bd=0).place(x=40, y=10)
        tk.Label(body, anchor="nw", text="Paciente", font=("OpenSansRoman Bold", 32 * -1), bg="#72B2E6", fg="white").place(x=86, y=10)

        paciente = tk.Label(body, image=self.paciente_img, bg="#72B2E6", bd=0)
        paciente.place(x=18, y=60)

        tk.Label(paciente, anchor="nw", text="Nombre", fg="#246FC6", font=("Poppins Bold", 16 * -1), bg="#FAFAFA").place(x=35, y=15)
        self.nombre_out = tk.Label(paciente, image=self.label_1_img, bg="white", bd=0)
        self.nombre_out.place(x=20, y=40)
        tk.Label(paciente, textvariable=self.nombre_var, fg="#000000", bg="#D9D9D9", font=("AsapRoman Regular", 12 * -1), anchor="w").place(x=35, y=47, width=275, height=18)

        tk.Label(paciente, anchor="nw", text="RUT", fg="#246FC6", font=("Poppins Bold", 16 * -1), bg="#FAFAFA").place(x=35, y=90)
        self.rut_out = tk.Label(paciente, image=self.label_2_img, bg="white", bd=0)
        self.rut_out.place(x=20, y=115)
        tk.Label(paciente, textvariable=self.rut_var, fg="#000000", bg="#D9D9D9", font=("AsapRoman Regular", 12 * -1), anchor="w").place(x=35, y=122, width=120, height=18)

        tk.Label(paciente, anchor="nw", text="Telefono", fg="#246FC6", font=("Poppins Bold", 16 * -1), bg="#FAFAFA").place(x=195, y=90)
        self.telefono_out = tk.Label(paciente, image=self.label_2_img, bg="white", bd=0)
        self.telefono_out.place(x=180, y=115)
        tk.Label(paciente, textvariable=self.telefono_var, fg="#000000", bg="#D9D9D9", font=("AsapRoman Regular", 12 * -1), anchor="w").place(x=195, y=122, width=120, height=18)

        tk.Label(paciente, anchor="nw", text="Correo", fg="#246FC6", font=("Poppins Bold", 16 * -1), bg="#FAFAFA").place(x=35, y=165)
        self.correo_out = tk.Label(paciente, image=self.label_1_img, bg="white", bd=0)
        self.correo_out.place(x=20, y=190)
        tk.Label(paciente, textvariable=self.correo_var, fg="#000000", bg="#D9D9D9", font=("AsapRoman Regular", 12 * -1), anchor="w").place(x=35, y=196, width=275, height=18)

        # TODO: AGENDA
        tk.Label(body, image=self.agenda_logo_img, bg="#72B2E6", bd=0).place(x=390, y=10)
        tk.Label(body, anchor="nw", text="Agenda", font=("OpenSansRoman Bold", 32 * -1), bg="#72B2E6", fg="white").place(x=436, y=10)

        agenda = tk.Label(body, image=self.agenda_img, bg="#72B2E6", bd=0)
        agenda.place(x=375, y=60)

        tk.Label(agenda, anchor="nw", text="Fecha", fg="#246FC6", font=("Poppins Bold", 16 * -1), bg="#FAFAFA").place(x=35, y=15)
        self.fecha_out = tk.Label(agenda, image=self.label_3_img, bg="white", bd=0)
        self.fecha_out.place(x=20, y=40)
        tk.Label(agenda, textvariable=self.fecha_var, fg="#000000", bg="#D9D9D9", font=("AsapRoman Regular", 12 * -1), anchor="w").place(x=35, y=47, width=95, height=18)

        tk.Label(agenda, anchor="nw", text="Hora", fg="#246FC6", font=("Poppins Bold", 16 * -1), bg="#FAFAFA").place(x=175, y=15)
        self.hora_out = tk.Label(agenda, image=self.label_3_img, bg="white", bd=0)
        self.hora_out.place(x=160, y=40)
        tk.Label(agenda, textvariable=self.hora_var, fg="#000000", bg="#D9D9D9", font=("AsapRoman Regular", 12 * -1), anchor="w").place(x=175, y=47, width=95, height=18)

        tk.Label(agenda, anchor="nw", text="Estado", fg="#246FC6", font=("Poppins Bold", 16 * -1), bg="#FAFAFA").place(x=35, y=90)
        self.estado_out = tk.Label(agenda, image=self.label_4_img, bg="white", bd=0)
        self.estado_out.place(x=35, y=120)
        tk.Label(agenda, textvariable=self.estado_var, fg="#000000", bg="#D9D9D9", font=("AsapRoman Regular", 12 * -1), anchor="w").place(x=50, y=127, width=205, height=18)

    def get_rut_input(self) -> str:
        return self.rut_entry.get().strip()

    def clear_outputs(self):
        self.nombre_var.set("")
        self.rut_var.set("")
        self.telefono_var.set("")
        self.correo_var.set("")
        self.fecha_var.set("")
        self.hora_var.set("")
        self.estado_var.set("")

    def set_patient_data(self, nombre: str, rut: str, telefono: str, correo: str):
        self.nombre_var.set(nombre or "")
        self.rut_var.set(rut or "")
        self.telefono_var.set(telefono or "")
        self.correo_var.set(correo or "")

    def set_agenda_data(self, fecha: str, hora: str, estado: str):
        self.fecha_var.set(fecha or "")
        self.hora_var.set(hora or "")
        self.estado_var.set(estado or "")

    def show_patient_not_found(self):
        self.show_error_message("Paciente no registrado", "No existe información asociada al RUT ingresado.")

    def _enter_search_rut(self, event=None):
        self.controller.on_search_rut(self)

    def clear_rut_input(self):
        self.rut_entry.delete(0, tk.END)
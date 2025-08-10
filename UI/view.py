import flet as ft


class View():
    def __init__(self, page: ft.Page):
        super().__init__()
        self._page = page
        self._page.title = "Definizione di Business Area"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.bgcolor = "#748c54"
        self._page.window_height = 800
        self._title = ""
        self._description = ""
        self._btnOttieniFile = None
        self.txt_result = None
        self._controller = None

    def load_interface(self):
        # titolo
        self._title = ft.Text("Definizione di Business Area", color="#202820", size=28,
                              font_family="Montserrat", weight=ft.FontWeight.BOLD)
        self._page.controls.append(self._title)

        # descrizione
        self._description = ft.Text("Il programma sviluppato, partendo da un database in cui sono raccolte "
                                    "informazioni riguardo cooperative di tipo B, permette di generare un "
                                    "file Excel in cui ogni codice ateco è assegnato alla specifica business "
                                    "area di riferimento. "
                                    "Il file generato sarà costituito da due sheet: nel primo i dati saranno "
                                    "ordinati per codice ateco crescente, nel secondo invece saranno raggruppati "
                                    "per business area mantenendo l'ordine alfabetico.", color="#202820",
                                    size=16, font_family="Montserrat")
        self._page.controls.append(self._description)

        # bottone
        self._btnOttieniFile = ft.ElevatedButton(text="Ottieni File", on_click=self._controller.handle_ottieni_file,
                                                 disabled=False, bgcolor="#faffeb", color="#202820")
        self._page.controls.append(self._btnOttieniFile)

        # risultati
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)

        # aggiorno la pagina
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()
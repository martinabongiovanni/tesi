import os
import subprocess
import sys
import openpyxl # per leggere, modificare e scrivere file Excel
from openpyxl import Workbook # per creare un nuovo file Excel
import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self.lista_codice_area = [] # lista di tuple del tipo
                                    # (codice ateco, business area) - (str, Business area)
        self._btnApriFile = None

    def carica_dati_excel(self):
        file_excel = openpyxl.load_workbook("database/AIDA_CoopB.xlsx")
        primo_sheet = file_excel.active
        # definisco una lista in cui ogni elemento è un'intestazione delle colonne del file in input
        header = [cell.value for cell in primo_sheet[1]]

        for row in primo_sheet.iter_rows(min_row=2, values_only=True):
            # definisco un dizionario con chiave l'intestazione della colonna e
            # valore il corrispettivo valore della riga in esame
            dati = dict(zip(header, row))

            # prelevo il codice ateco della coopB in esame
            codice = dati['ATECO 2002_codice']
            if codice is None:
                return
            # associo il codice a una business area chiamando il relativo metodo
            self._model.associazione_codiceAteco_BusinessArea(codice)

        # prelevo dal model la lista di combinazioni (codice, area)
        self.lista_codice_area = self._model.get_lista_combinazioni()

    def salva_excel_ordinato(self):
        '''
        Questa funzione serve per salvare i dati contenuti in self.lista_codice_area in un file Excel.
        Saranno creati due sheet per ordinare i dati rispettivamente in ordine di codice (crescente) e
        in ordine di area (alfabetico).
        '''
        file_excel = Workbook()

        # 1. Ordinamento per codice
        primo_sheet_codice = file_excel.active
        primo_sheet_codice.title = "By Codice"
        self._scrivi_dati(primo_sheet_codice, sorted(self.lista_codice_area, key=lambda x: x[0]))

        # 2. Ordinamento per area
        secondo_sheet_area = file_excel.create_sheet("By Area")
        self._scrivi_dati(secondo_sheet_area, sorted(self.lista_codice_area, key=lambda x: x[1]))

        file_excel.save("output.xlsx")

    def _scrivi_dati(self, sheet, lista):
        # definisco le intestazioni
        sheet.append(["Codice Ateco", "Business Area"])

        # definisco le varie righe
        for element in lista:
            sheet.append([element[0], str(element[1])])
            colore = element[1].colora_area()
            sheet.cell(row=sheet.max_row, column=2).fill = colore

    def handle_ottieni_file(self, e):
        self.carica_dati_excel()
        self.salva_excel_ordinato()
        self._view.txt_result.controls.clear()
        row = ft.Row([ft.Text("Il file è stato generato correttamente!",
                                color="#202820", size=18, weight=ft.FontWeight.BOLD),
                      ft.Icon(ft.Icons.CHECK_CIRCLE_ROUNDED, color="#202820", size=30)])
        self._view.txt_result.controls.append(row)
        self._view.txt_result.controls.append(ft.Text('Clicca su "Apri" per visualizzarne il contento.',
                                                      color="#202820", size=16))
        self._btnApriFile = ft.ElevatedButton(text="Apri", on_click=self.handle_apri_file,
                                              disabled=False, bgcolor="#faffeb", color="#202820")
        self._view.txt_result.controls.append(self._btnApriFile)

        self._view.update_page()

    def handle_apri_file(self, e):
        file = "output.xlsx"

        if not os.path.exists(file):
            self._view.create_alert("Attenzione! File non trovato.")
            return

        try:
            if sys.platform.startswith('darwin'):  # macOS
                subprocess.call(('open', file))
            elif os.name == 'nt':  # Windows
                os.startfile(file)
            elif os.name == 'posix':  # Linux
                subprocess.call(('xdg-open', file))
            else:
                raise OSError("Sistema operativo non supportato.")

        finally:
            self._view.update_page()
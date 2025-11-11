import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    def popola_dropdown_iniziali(self):
        """
        Chiamato dal main DOPO la creazione dell'interfaccia.
        Popola le dropdown. I callback sono già collegati dalla View.
        """
        try:
            lista_musei = self._model.get_musei()
            lista_epoche = self._model.get_epoche()

            self._popola_dropdown_musei(lista_musei)
            self._popola_dropdown_epoche(lista_epoche)

        except Exception as e:
            self._view.show_alert(f"Errore nel caricamento dati: {e}")

        print("Controller: Dropdown popolate.")

    # --- METODI LOGICI PER AGGIORNARE LA VIEW ---

    def _popola_dropdown_musei(self, lista_musei):
        self._view.dd_museo.options.clear()
        self._view.dd_museo.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for museo in lista_musei:
            self._view.dd_museo.options.append(ft.dropdown.Option(text=museo.nome))
        self._view.update()

    def _popola_dropdown_epoche(self, lista_epoche):
        self._view.dd_epoca.options.clear()
        self._view.dd_epoca.options.append(ft.dropdown.Option(text="Nessun filtro"))
        for epoca in lista_epoche:
            self._view.dd_epoca.options.append(ft.dropdown.Option(text=epoca))
        self._view.update()

    def _mostra_risultati(self, artefatti):
        self._view.lv_risultati.controls.clear()
        if not artefatti:
            self._view.lv_risultati.controls.append(ft.Text("Nessun artefatto trovato con questi filtri."))
        else:
            self._view.lv_risultati.controls.append(
                ft.Text(f"Trovati {len(artefatti)} artefatti:", weight=ft.FontWeight.BOLD))
            for artefatto in artefatti:
                self._view.lv_risultati.controls.append(ft.Text(str(artefatto)))
        self._view.update()

    def _pulisci_risultati(self):
        self._view.lv_risultati.controls.clear()
        self._view.update()



    def on_cambio_museo(self, e):
        scelta = e.control.value
        if scelta == "Nessun filtro":
            self.museo_selezionato = None
        else:
            self.museo_selezionato = scelta
        print(f"Controller: Museo selezionato: {self.museo_selezionato}")
        self._pulisci_risultati()

    def on_cambio_epoca(self, e):
        scelta = e.control.value
        if scelta == "Nessun filtro":
            self.epoca_selezionata = None
        else:
            self.epoca_selezionata = scelta
        print(f"Controller: Epoca selezionata: {self.epoca_selezionata}")
        self._pulisci_risultati()



    def handle_mostra_artefatti(self, e):
        try:
            print(f"Controller: Bottone premuto! Cerco artefatti...")

            lista_artefatti = self._model.get_artefatti_filtrati(
                self.museo_selezionato,
                self.epoca_selezionata
            )
            self._mostra_risultati(lista_artefatti)

            if not lista_artefatti:
                self._view.show_alert("Nessun artefatto trovato...")

        except Exception as e:
            self._view.show_alert(f"Errore nella ricerca: {e}")


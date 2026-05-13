import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.clean()
        anno = self._view._txtAnno.value
        if anno == "":
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text("Inserire un numero: ", color="red"))
            self._view.update_page()
            return
        anno = int(anno)
        if anno < 1816 or anno > 2016:
            self._view._txt_result.clean()
            self._view._txt_result.controls.append(ft.Text("Inserire un numero tra 1816 e 2016: ", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(anno)
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamente"))

        componentiConn = self._model.getComponentiConn()
        self._view._txt_result.controls.append(ft.Text(f"il grafo ha {componentiConn} componenenti connesse"))

        nodi = self._model._grafo.nodes()
        nodi_ordinati = sorted(nodi, key=lambda x: x.StateNme)
        for nodo in nodi_ordinati:
            grado = self._model._grafo.degree(nodo)
            self._view._txt_result.controls.append(ft.Text(f"{nodo.StateNme} -- {grado} vicini"))
            self._view.update_page()

        vertici = self._model._grafo.nodes()
        print(len(vertici))
        archi = len(self._model._grafo.edges())
        print(archi)


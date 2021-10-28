class Especie:
    def __init__(self, nom_esp):
        self._nom_esp = nom_esp

    def get_nom_esp(self):
        return self._nom_esp

    def set_nom_esp(self, nom_esp):
        self._nom_esp = nom_esp
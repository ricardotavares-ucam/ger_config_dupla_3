class Veterinario:

    def __init__(self, nome_vet, endereco_vet, tel_vet):
        self._nome_vet = nome_vet
        self._endereco_vet = endereco_vet
        self._tel_vet = tel_vet

        def get_nome_vet(self):
            return self._nome_vet
        def get_endereco_vet(self):
            return self._endereco_vet
        def get_tel_vet(self):
            return self._tel_vet
        
        def set_nome_vet(self, nome_vet):
            self._nome_vet = nome_vet
        def set_endereco_vet(self, endereco_vet):
            self._endereco_vet = endereco_vet
        def set_tel_vet(self, tel_vet):
            self._tel_vet = tel_vet
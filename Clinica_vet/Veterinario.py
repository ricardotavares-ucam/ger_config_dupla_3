class Veterinario:

    def __init__(self, **kwargs):
        self._nome = kwargs['nome']
        self._endereco = kwargs['endereco']
        self._numero_tel = kwargs['numero_tel']

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self,endereco):
        self._endereco = endereco

    @property
    def numero_tel(self):
        return self._numero_tel
    
    @numero_tel.setter
    def numero_tel(self, numero_tel):
        self._numero_tel = numero_tel
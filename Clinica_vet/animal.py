class Animal:
    def __init__(self, nome_animal, idade_animal, sexo_animal):
        self._nome_animal = nome_animal
        self._idade_animal = idade_animal
        self._sexo_animal = sexo_animal

        def get_nome_animal(self):
            return self._nome_animal
        def get_idade_animal(self):
            return self._idade_animal
        def get_sexo_animal(self):
            return self._sexo_animal

        def set_nome_animal(self, nome_animal):
            self._nome_animal = nome_animal
        def set_idade_animal(self, idade_animal):
            self._idade_animal = idade_animal
        def set_sexo_animal(self, sexo_animal):
            self._sexo_animal = sexo_animal

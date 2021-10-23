from datetime import datetime, timedelta

class Consulta:
    def __init__(self, **kwargs):
        self._datetime_consulta = None
        self._historico = kwargs['historico']

@property
def datetime_consulta(self):
    return self._datetime_consulta


@property
def historico(self):
        return self._historico
    
@historico.setter
def historico(self, historico):
        self._historico = historico

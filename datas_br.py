from datetime import datetime

class DatasBr:
    def __init__(self):
        self.__momento_cadastro = datetime.today()
        self.__definir_meses()
        self.__definir_mes_cadastro()
        self.__definir_dias()
        self.__definir_dia_da_semana()

    def __definir_mes_cadastro(self):
        numero = self.__momento_cadastro.month
        self.__mes_cadastro = self.__meses_do_ano[numero-1].title()

    def __definir_dia_da_semana(self):
        numero = self.__momento_cadastro.weekday()
        self.__dia_da_semana = self.__dias_da_semana[numero].title()

    def __definir_meses(self):
        self.__meses_do_ano = [
            'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
            'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
        ]

    def __definir_dias(self):
        self.__dias_da_semana = ['segunda-feira', 'terça-feira',
                                 'quarta-feira', 'quinta-feira', 'sexta-feira',
        'sábado', 'domingo']

    @property
    def mes_cadastro(self):
        return self.__mes_cadastro

    @property
    def dia_da_semana(self):
        return self.__dia_da_semana

    @property
    def momento_cadastro(self):
        return self.__momento_cadastro
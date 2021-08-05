from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.__momento_cadastro = datetime.today()
        self.__definir_meses()
        self.__definir_mes_cadastro()
        self.__definir_dias()
        self.__definir_dia_da_semana()
        self.__formatar_momento_cadastro()

    def __str__(self):
        return self.__momento_cadastro

    def __formatar_momento_cadastro(self):
        self.__momento_cadastro = self.__momento_cadastro.strftime("%d/%m/%Y %H:%M")

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

    def capturar_tempo_cadastro(self):
        self.__tempo_cadastro =  (datetime.today() + timedelta(days=30)) - datetime.strptime(str(self.__momento_cadastro), "%d/%m/%Y %H:%M")
        return self.__tempo_cadastro

    @property
    def mes_cadastro(self):
        return self.__mes_cadastro

    @property
    def dia_da_semana(self):
        return self.__dia_da_semana

    @property
    def momento_cadastro(self):
        return self.__momento_cadastro
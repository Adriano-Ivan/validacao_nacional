import requests

class BuscaEndereco:

    def __init__(self, cep):
        cep = str(cep)
        if(self.__cep_e_valido(cep)):
            self.__cep = cep
            self.__format_cep()
        else:
            raise ValueError('CEP inválido !')

    def __str__(self):
        return self.__cep

    def __cep_e_valido(self, cep):
        if(len(cep) == 8):
            return True
        else:
            return False

    def __format_cep(self):
        self.__cep = f'{self.__cep[:5]}-{self.__cep[5:]}'

    def acessa_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.__cep}/json/'
        url = requests.get(url)
        return url

    @property
    def cep(self):
        return self.__cep
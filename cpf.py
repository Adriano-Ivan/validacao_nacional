
class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if(self.__cpf_e_valido(documento)):
            self._cpf = documento
            #self._cpf = self.__formata_cpf()
            print('CPF válido !')
        else:
            raise ValueError('CPF inválido !')

    def __str__(self):
        return self.__formata_cpf()

    def __cpf_e_valido(self, documento):
        if(len(documento) == 11):
            return True
        else:
            return False

    def __formata_cpf(self):
        fatia_um = self._cpf[:3]
        fatia_dois = self._cpf[3:6]
        fatia_tres = self._cpf[6:9]
        fatia_quatro = self._cpf[9:]

        return f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'

    @property
    def cpf(self):
        return self._cpf
from validate_docbr import CPF, CNPJ

class CpfCnpj:
    def __init__(self, documento, tipo_documento):
        self._tipo_documento = tipo_documento
        documento = str(documento)

        if(self._tipo_documento.lower() == 'cpf'):
            if(self.__cpf_e_valido(documento)):
                self._cpf = documento
                #self._cpf = self.__formata_cpf()
                print('CPF válido !')
            else:
                raise ValueError('CPF inválido !')
        elif(self._tipo_documento.lower() == 'cnpj' ):
            if(self.__cnpj_e_valido(documento)):
                self._cnpj = documento
                print('CNPJ é válido !')
            else:
                raise ValueError('CNPJ é inválido !')
        else:
            print('O tipo de documento deve ser informado e deve ser válido !')

    def __str__(self):
        if(self._tipo_documento == 'cpf'):
            return self.__formata_cpf()
        elif(self._tipo_documento == 'cnpj'):
            return self.__formata_cnpj()

    def __cnpj_e_valido(self, cnpj):
        if(len(cnpj) == 14):
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError('Quantidade de dígitos inválida')

    def __cpf_e_valido(self, documento):
        if(len(documento) == 11):
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida !')

    def __formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self._cpf)
        # fatia_um = self._cpf[:3]
        # fatia_dois = self._cpf[3:6]
        # fatia_tres = self._cpf[6:9]
        # fatia_quatro = self._cpf[9:]
        #
        # return f'{fatia_um}.{fatia_dois}.{fatia_tres}-{fatia_quatro}'
    def __formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self._cnpj)

    @property
    def cpf(self):
        return self._cpf
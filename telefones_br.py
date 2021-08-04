import re

class TelefonesBr:
    def __init__(self, telefone):
        if(self.__valida_telefone(telefone)):
            self.__numero = telefone
            self.__format_numero()
        else:
            raise ValueError('Número inválido !')

    def __str__(self):
        return self.__numero_formatado

    def __valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if(resposta):
            return True
        else:
            return False

    def __format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.__numero)
        self.__numero_formatado = f'+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}'

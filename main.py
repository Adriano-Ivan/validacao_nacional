import re
from telefones_br import TelefonesBr

# padrao = re.compile("[0-9][a-z]{1,2}?[0-9]")
# texto = '1a3 1ad7 1a2 1cc dd1'
#
# busca = padrao.match(texto)
# busca2 = padrao.search(texto)
# # outra_forma = re.search(padrao, '7a3')
#
# if(busca):
#     print(busca.group())
# else:
#     print('Não combina')
#
#
# if(busca2):
#     print(busca2.group())
# else:
#     print('Não combina.')

# padrao_email = "\w{5,50}@[a-z]{3,10}.com.br"
# texto = "adfdfdsafdasfasdfasf hamda@gmail.com.br dfdfdf"
# resposta = re.search(padrao_email, texto)

# padrao_compile = re.compile(padrao_email)
# busca_email = padrao_compile.search(texto)
#teste
# print(resposta.group())

telefone = 'aadfd 552378892134'
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
# padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# resposta = re.search(padrao, telefone)
# print(resposta.group())
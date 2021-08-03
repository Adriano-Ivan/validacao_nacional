from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

# cpf_um = Cpf("15316264754")
# print(cpf_um)

cnpj = '46966413000126'
cpf = '57525975019'
# cnpj = CNPJ()
# print(cnpj.validate('46966413000126'))

documento = CpfCnpj(cpf, 'cpf')
print(documento)
from endereco import Address

class Empresa():
    def __init__(self, nome, cnpj):
        self.nome = nome
        self.cnpj = cnpj
        self.address = Address()

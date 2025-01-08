from banco.endereco import Endereco

class Usuario:
    def __init__(self, nome, cpf, senha, endereco):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.endereco = endereco

    def __str__(self):
        return f"Usuário: {self.nome} - CPF: {self.cpf}"

    def to_dict(self):
        return {
            'nome': self.nome,
            'cpf': self.cpf,
            'senha': self.senha,
            'endereco': self.endereco.to_dict()
        }

    @staticmethod
    def from_dict(data):
        endereco = Endereco.from_dict(data['endereco'])
        return Usuario(data['nome'], data['cpf'], data['senha'], endereco)
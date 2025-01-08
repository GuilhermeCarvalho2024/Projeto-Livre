from banco.cadastro import Cadastro

class Login:
    def __init__(self):
        self.cadastro = Cadastro()

    def autenticar(self, cpf, senha):
        for conta in self.cadastro.contas:
            if conta.cpf == cpf and conta.senha == senha:
                return conta
        print("CPF ou senha incorretos.")
        return None
from banco.conta import Conta
from banco.utils import ler_json, escrever_json

class Cadastro:
    def __init__(self):
        self.contas = self.carregar_dados()

    def cadastrar_conta(self, nome, cpf, senha, endereco):
        if cpf in [conta.cpf for conta in self.contas]:
            print("CPF já cadastrado.")
        else:
            novo_usuario = Conta(nome, cpf, senha, endereco)
            self.contas.append(novo_usuario)
            self.salvar_dados()
            print("Conta cadastrada com sucesso!")

    def salvar_dados(self):
        dados = [conta.to_dict() for conta in self.contas]
        escrever_json('data/contas.json', dados)

    def carregar_dados(self):
        dados = ler_json('data/contas.json')
        return [Conta.from_dict(conta) for conta in dados] if dados else []
from banco.login import Login
from banco.endereco import Endereco

def menu_principal():
    while True:
        print("Sistema Bancário!")
        print("1. Cadastrar Conta")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")
            rua = input("Digite a rua: ")
            numero = input("Digite o número: ")
            cidade = input("Digite a cidade: ")
            estado = input("Digite o estado: ")
            endereco = Endereco(rua, numero, cidade, estado)
            banco.cadastro.cadastrar_conta(nome, cpf, senha, endereco)
        elif opcao == '2':
            cpf = input("Digite seu CPF: ")
            senha = input("Digite sua senha: ")
            usuario = banco.autenticar(cpf, senha)
            if usuario:
                menu_usuario(usuario)

        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")    

def menu_usuario(usuario):
    while True:
        print(f"\nEm que posso te ajudar, {usuario.nome}?")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Transferir")
        print("4. Logout")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor a depositar: "))
            usuario.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a sacar: "))
            usuario.sacar(valor)
        elif opcao == '3':
            cpf_destino = input("Digite o CPF da conta destino: ")
            valor = float(input("Digite o valor a transferir: "))
            conta_destino = next((c for c in banco.cadastro.contas if c.cpf == cpf_destino), None)
            if conta_destino:
                usuario.transferir(conta_destino, valor)
            else:
                print("Conta destino não encontrada.")
        elif opcao == '4':
            print("Logout realizado.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    banco = Login()
    menu_principal()
        
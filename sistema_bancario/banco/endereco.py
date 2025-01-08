class Endereco:
    def __init__(self, rua, numero, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.rua}, {self.numero}, {self.cidade}, {self.estado}"

    def to_dict(self):
        return {
            'rua': self.rua,
            'numero': self.numero,
            'cidade': self.cidade,
            'estado': self.estado
        }

    @staticmethod
    def from_dict(data):
        return Endereco(data['rua'], data['numero'], data['cidade'], data['estado'])
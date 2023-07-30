from classe_pai import dadosCliente

class clienteEmprestimo(dadosCliente):
    def __init__(self, nome, cpf, contato):
        super().__init__(nome, cpf, contato)
        print("Cliente criado com sucesso.")

    def infoExtra(self,emprestimo):
        self.emprestimo= emprestimo
        
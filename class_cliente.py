class Cliente:
    def __init__(self,nome,email,plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic","premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Invalido!")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            raise Exception("Plano Invalido!")


    def ver_filme(self,filme,plano_filme):
        if self.plano == plano_filme:
            print(f"Exibir filme {filme}")
        elif self.plano == "premium":
            print(f"Exibir filme {filme}")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrade de plano!")
        else:
            print("Plano Invalido!")

cliente = Cliente("Erik","erikmfigueiredo@gmail.com","basic")
print(cliente.plano)

cliente.ver_filme("300","premium")

cliente.mudar_plano("premium")
print(cliente.plano)
cliente.ver_filme("300","premium")
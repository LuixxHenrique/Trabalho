from Listados import *


class Estoque:
    def __init__(self):
        self.cadastrar = []

    def salvar_produtos(self):
        entrada_cod = input('Informe o Código: ')
        entrada_valoruni = input('Informe o Valor: ')
        entrada_descricao = input('Informe a Descricao: ')
        self.cadastrar.append(Produtos_Listados(cod=entrada_cod,
                                                valoruni=entrada_valoruni,
                                                descricao=entrada_descricao))
        print('Produto Salvo!')

    def listar_produtos(self):
        for i in range(len(self.cadastrar)):
            print('Codigo:', self.cadastrar[0].cod,
                  '- Valor:', self.cadastrar[0].valoruni,
                  '- Descricao:', self.cadastrar[0].descricao)

    def alterar_valor(self):
        entrada = input('Informe o codigo do produto: ')
        for i in range(len(self.cadastrar)):
            if entrada == self.cadastrar[i].cod:
                self.cadastrar[i].valoruni = input('Novo valor: ')
            else:
                print('Codigo de Produto nao Existe!')

    def alterar_descricao(self):
        entrada = input('Informe o Codigo do Produto: ')
        for i in range(len(self.cadastrar)):
            if entrada == self.cadastrar[i].cod:
                self.cadastrar[i].descricao = input('Nova Descricao: ')
            else:
                print('Codigo de Produto nao Existe!')

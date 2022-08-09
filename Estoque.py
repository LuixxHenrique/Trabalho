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
            print('Codigo:', self.cadastrar[i].cod,
                  '- Valor:', self.cadastrar[i].valoruni,
                  '- Descricao:', self.cadastrar[i].descricao)

    def alterar_valor(self):
        entrada = input('Informe o codigo do produto: ')
        for i in range(len(self.cadastrar)):
            if entrada == self.cadastrar[i].cod:
                self.cadastrar[i].valoruni = input('Novo valor: ')
            else:
                print('Valor Alterado!')

    def alterar_descricao(self):
        entrada = input('Informe o Codigo do Produto: ')
        for i in range(len(self.cadastrar)):
            if entrada == self.cadastrar[i].cod:
                self.cadastrar[i].descricao = input('Nova Descricao: ')
            else:
                print('Descrição Alterada!')

    def exclui_produto(self, cod):
        for i in range(len(self.cadastrar)):
            if cod == self.cadastrar[i].cod:
                str(self.cadastrar[i].remove)
            else:
                print('Codigo Removido!')

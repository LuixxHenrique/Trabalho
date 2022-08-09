from Estoque import *

class Main:
    def __init__(self):
        estoque = Estoque()

        self.produtos = Produtos_Listados(cod=0, valoruni=0, descricao="Teste")
        estoque.entrada = self.produtos

        while True:
            entrada = input('Informe o que deseja realizar\n1'
                            '- Cadastrar\n2'
                            '- Listar Produtos\n3'
                            '- Alterar Valor\n4'
                            '- Alterar Descricao\n5'
                            '- Excluir Produto\n0'
                            '- Sair')

            if entrada == '1':
                estoque.salvar_produtos()
            elif entrada == '2':
                estoque.listar_produtos()
            elif entrada == '3':
                estoque.alterar_valor()
            elif entrada == '4':
                estoque.alterar_descricao()
            elif entrada == '5':
                cod = int(input('Informe o código do Produto: '))
                estoque.exclui_produto(cod)
            elif entrada == '0':
                break
            else:
                print('Entrada Incorreta!')
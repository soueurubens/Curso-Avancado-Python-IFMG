class Produto:
    def __init__(self, descricao, preco):
        self._descricao = descricao
        self._preco = preco

    def __str__(self):
        return '{d} R${p:.2f}'.format(d=self._descricao, p=self._preco)

class ProdutoEstoque(Produto):
    def __init__(self, descricao, preco):
        super().__init__(descricao, preco)
        self._estoque = 0.0
    @property
    def preco(self):
        return self._preco;
    @property
    def descricao(self):
        return self._descricao;
    @preco.setter
    def preco(self, preco):
        self._preco=preco
    @descricao.setter 
    def descricao(self, descricao):
        self._descricao = descricao

    def entrada(self, quantidade):
        self._estoque += quantidade
    def saida(self, quantidade):
        if quantidade <= self._estoque:
            self._estoque -= quantidade
            return True
        return False

    def __str__(self):
        texto = super().__str__()
        texto += ' | Estoque {e:0.0f}'.format(e=self._estoque)
        return texto

class ProdutoVenda(Produto):
    def __init__(self, descricao, preco, quantidade):
        super().__init__(descricao, preco)
        self._quantidade = quantidade
    @property
    def total(self):
        return self._quantidade * self._preco
    def __str__(self):
        texto = super().__str__()
        texto += 'Qtde {q:.3f}'.format(q=self._quantidade)
        texto += 'Total R${v:.2f}'.format(v=self.total)

class Venda:
    def __init__(self):
        self._lista_produtos = []
        self._total_venda = 0.0

    @property
    def total(self):
        return self._total_venda

    @property
    def numero_produtos(self):
        return len(self._lista_produtos)

    def adiciona_produto(self, produto):
        self._lista_produtos.append(produto)
        self._total_venda += produto.total
    def __str__(self):
        texto = '\n' * 50
        texto += '\n== Produtos =='
        for produto in self._lista_produtos:
            texto += '\n'+str(produto)
        texto += '\n' * 20
        texto += 'Total venda: R${v:0.2f}'.format(self._total_venda)
        texto += '\n' * 50
        return texto

def pergunta(mensagem, tipo=int):
    try:
        perg = input(mensagem)
        return tipo(perg)
    except:
        print("Valor inválido! Infome novamente.")
def confirma(mensagem, resposta):
    texto = input(mensagem)
    if texto.lower() == resposta.lower():
        return True
    return False

class Caixa:
    def __init__(self):
        self._produtos = {}
        self._vendas = []

    @classmethod
    def menu(cls):
        print()
        print('********************************')
        print('*           CAIXA              *')
        print('********************************')
        print('(C) Cadastrar produto ')
        print('(A) atualizar produto ')
        print('(E) Entrada de estoque          ')
        print('(V) Vender                      ')
        print('(R) Relatório de vendas         ')
        print('(S) Sair                        ')
        print('********************************')
        escolha = input('Informe sua opção: ').upper()
        return escolha

    def dados_brutos(self):
        print("Informe os dados: ")
        descricao = input("Descrição: ").strip()
        preco = pergunta('Preço: ', float)
        return descricao, preco
    def analisar_produtos(self, descricao):
        for produto in self._produtos.values():
            if produto.descricao.lower() == descricao.lower():
                return True
        return False
    def cadastrar_produto(self):
        print('\n' * 5)
        print("\n == Cadastro de produto ==")
        while True:
            resultado = self.dados_brutos()
            descricao, preco = resultado
            # Analisando se o item já esta cadastrado
            if self.analisar_produtos(descricao):
                if confirma("Cadastrar outro produto? (S/N): ", 'S'):
                    continue
                else: break
            # Cadastrando o item 
            produto = ProdutoEstoque(descricao, preco)
            codigo = len(self._produtos)
            self._produtos[codigo] = produto 
            print("Produto cadastrado com sucesso!")
            break
    def atualiza_produto(self):
        print('\n' * 5)
        while True:
            print("== Atualiza produto ==")
            for cod, produto in self._produtos.items():
                print(f'{cod}: {produto}')
            print("----------------------")
        
            cod = pergunta("Codigo: ")
            if cod in self._produtos:
                resposta = self.dados_brutos()
                if resposta:
                    descricao, preco = resposta
                    self._produtos[cod].descricao = descricao
                    self._produtos[cod].preco = preco
                    print("Produto atualizado com sucesso!")
                    print(f'{cod}: {self._produtos[cod]}')
                    break
            else:
                if confirma("Continuar atualizando? (S/N)", 'S'):
                    continue
                else: break
    def entrada_estoque(self):
        while True:
            print('\n' * 5)
            print("=== Adicionando produtos ao estoque ==")
            for cod, produto in self._produtos.items():
                print(f'{cod}: {produto}')
            print("----------------------")
            
            cod = pergunta("Codigo: ", int)
            if cod in self._produtos:
                quantidade = pergunta("Quantidade de entrada: ", int)
                self._produtos[cod].entrada(quantidade)
                print("Quantidade adicionanda com sucesso!")
                print(f'{cod}: {self._produtos[cod]}')
                break;
            else:
                print("Produto não encontrado!")
                if confirma("Cadastrar outro produto? (S/N): ", 'S'):
                    continue
                else: break




caixa = Caixa()
caixa.menu()
caixa.cadastrar_produto()
caixa.atualiza_produto()
caixa.entrada_estoque()
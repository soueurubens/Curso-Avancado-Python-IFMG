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
        texto += 'Estoque {e:0.3f}'.format(e=self._estoque)
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


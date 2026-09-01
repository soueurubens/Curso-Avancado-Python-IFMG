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
        return self._preco
    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco

    @property
    def descricao(self):
        return self._descricao

class Meu_Objeto:
    def __init__(self): # Self se refere a instância da classe (Meu_Objeto)
        self.nome = 'Aleatório'
        self.idade = 26
        print('Construtor chamado com sucesso')
    def imprime(self): # Sempre referenciar o objeto.
        print(f'Olá meu nome é {self.nome} e eu tenho {self.idade} anos.')

Aleatório = Meu_Objeto()
Aleatório.imprime()

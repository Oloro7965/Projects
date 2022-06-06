class jogoDaVelha:
    def __init__(self):
        self.__lista=[['_','_','_'],['_','_','_'],['_','_','_']]
    @property
    def lista(self):
        return self.__lista
    def jogar(self):
        self.mostrarTabuleiro()
        self.jogador1()
    def jogador1(self):
        print('Jogador 1')
        linha=int(input('digite a sua linha '))
        coluna=int(input('digite a coluna '))
        if self.lista[linha-1][coluna-1]=='_':
            self.lista[linha-1][coluna-1]='X'
            if self.verificaGanhador():
                print('jogador 1 ganhou')
            else:
                self.mostrarTabuleiro()
                self.jogador2()
        else:
            print('jogada inválida, tente novamente')
            self.jogador1()
    def jogador2(self):
        print('Jogador 2')
        linha2 = int(input('digite a sua linha '))
        coluna2 = int(input('digite a coluna '))
        if self.lista[linha2-1][coluna2-1] == '_':
            self.lista[linha2-1][coluna2-1] = '0'
            if self.verificaGanhador():
                print('jogador 2 ganhou')
            else:
                self.mostrarTabuleiro()
                self.jogador1()
        else:
            print('jogada inválida,tente novamente')
            self.jogador2()
    def mostrarTabuleiro(self):
        # for cont in range(0,3):
        for linha in self.lista:
            for col in linha:
                print(f'{col} ',end='')
            print()
    def verificaGanhador(self):
        #linha
        for i in range(3):
            if self.lista[i][0]==self.lista[i][1]==self.lista[i][2] and self.lista[i][0]!='_':
                return True
        #coluna
        for c in range(3):
            if self.lista[0][c]==self.lista[1][c]==self.lista[2][c] and self.lista[0][c]!='_':
                return True
        if self.lista[0][0]==self.lista[1][1]==self.lista[2][2] and self.lista[0][0]!='_':
            return True
        if self.lista[2][0]==self.lista[1][1]==self.lista[0][2] and self.lista[2][0]!='_':
            return True
        return False
jogo=jogoDaVelha()
jogo.jogar()

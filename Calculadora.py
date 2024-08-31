import sys

#alteração de acordo com item 5 da Missão Prática
class Calculadora:
    def __init__(self):
        self.__valorA = 0
        self.__valorB = 0
        self.__operacao = '?'

    @property
    def valorA(self):
        return self.__valorA
    
    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB
    
    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao
    
    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self, simbolo):
        return (simbolo in ['+','-','*','/'])

    def calcular(self):
        if(self.validarOperacao(self.__operacao)):
            if(self.__operacao == '/'):
                if(self.__valorA==0 or self.__valorB==0):
                    print('Não é possível realizar essa operação')
                    sys.exit(1)
                else:
                    return self.__valorA / self.__valorB
            else:
                if(self.__operacao=='*'):
                    return self.__valorA * self.__valorB
                elif(self.__operacao=='+'):
                    return self.__valorA + self.__valorB
                elif(self.__operacao=='-'):
                    return self.__valorA - self.__valorB
        else:
            print('Operação não é válida')
            sys.exit(1)

    def mostrarResultado(self):
        print(str(self.valorA) + ' ' + 
              self.operacao + ' ' + 
              str(self.valorB) + ' = ' + 
              str(self.calcular()))
        
    def entrarDados(self):
        a = float(input("Digite o primeiro valor: "))
        self.valorA = a
        b = float(input("Digite o segundo  valor: "))
        self.valorB = b
        op = input("Digite a operação [+,-,/,*]: ")
        self.operacao = op

        
'''
class Calculadora:
    def __init__(self, valorA, valorB, operacao):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao
'''
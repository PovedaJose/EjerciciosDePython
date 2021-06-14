class Condicion:
    contador=0
    def __init__(self,num1=1,num2=1):
        self.number1=num1
        self.number2=num2
        number = num1+num2
        self.number3 = number

    def usoif(self):
        if self.number1 == self.number2:
            print("numero1:{}, numero2:{}: son iguales".format(self.number1,self.number2))
        elif self.number1 == self.number3:
             print("numero1:{}, numero3:{}: son iguales".format(self.number1,self.number3))
        else:
            print("No son iguales")

Ejm1 = Condicion(10,25)
Ejm1.usoif()
# print(Ejm1.number1)
# print(Ejm1.number2)
print(Ejm1.number1)
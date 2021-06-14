class Ciclos:
    def __init__(self,num1=5):
        self.number=num1

    def usowhile(self):

        vocal = input("Ingerse vocal: ").lower()
        while vocal not in ('a','e','i','o','u'):
            vocal = input("Ingrese vocal: ").lower()
        print("Felicitaciones el caracter: {} es una vocal".format(vocal))

ejm1 = Ciclos()
ejm1.usowhile()
class Sintaxis:
    instancia=0
    def __init__(self,dato=""):
        self.frase=dato
        Sintaxis.instancia = Sintaxis.instancia+1

    def uso_variables(self):
        edad, _peso = 24, 74.5
        name='Miguel López'
        genero= 'M'
        civil= True

        usuario = ('Juan', 123, 'miguel@gmail.com', True)

        materias = ['Algebra', 'POO', 'Fisica']
        materias [0] = "Python"
        materias.append("Algoritmo")

        docente = {'nombre': 'Julio', 'edad': 40, 'fac': 'faci'}

        #print(usuario,materias,docente)
        print(usuario, usuario[0],usuario[0:1],usuario[-1])
        print(materias, materias[2:],materias[:2],materias[-1:],materias[:-1])
        print(docente,docente['edad'])
            
obj1 = Sintaxis()
obj1.uso_variables()
from collections import namedtuple

Fish = namedtuple("Fish", ["name", "species", "tank"])

#Esto crea una clase Fish con los atributos publicos nombre, especie y tanque

miPrimerPez = Fish("Sammy", "Tibrón", "Tanque grande")

print(miPrimerPez)

#otra cosa útil es transforma una instancia de una clase en un
#diccionario

print(miPrimerPez._asdict())

from collections import Counter

l = [1,2,3,4,1,2,3,1,2,1]
print(Counter(l))

estudiantes = "Nicolás Claudio Brenda Flor Nicolás Flor"
print(Counter(estudiantes))

print(Counter(estudiantes.split()))
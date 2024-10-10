#Simple
a = 33
b = 200

if b < a:
  print(b,"es mayor que ", a)

#Doble
y = 200
z = 300

if y > z:
    print(y,"es mayor que ",z)
else:
    print(y,"no es mayor que ",z)

#Multiple
f = 200
n = 207
if f > n:
    print(f,"es mayor que ",n)
elif f < n:
    print(f, "es menor que ", n)
else:
    print(f, "es igual que ", n)

#Condiciones Enlazados
x = 28

if x > 10:
    print("Por encima de diez,")
    if x > 20:
        print("y también por encima de 20!")
else:
    print("pero no por encima de 20.")

#Parametros END
print("Estidiar los sabados", end=' ')
print("Es genial")

#print("Estudiar los sabados")
#print("Es genial")

#Parametro SEP
print("Daniela","Luis","Carlos","Camila")#Agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila", sep="")#Quita el espacio
print("Daniela","Luis","Carlos","Camila", sep=",")#Agrega una coma
print("Daniela","Luis","Carlos","Camila", sep="_", end='_Curso_python')#implementacion end y sep
notas=[ ]
totalnotas=int(input("Digite quantas notas serão calculadas: ")) 
x=0
while x<totalnotas:
    nota = float(input("Digite uma nota: "))
    notas.append(nota)
    x+=1
print(notas)
from contador import crea_Con_Reu,creaContador




click1 = creaContador()

click2 = creaContador(5)

clickR1 = crea_Con_Reu()

clickR2 = crea_Con_Reu(5)

print(click1(), clickR1(consulta = True), clickR1(), clickR1(consulta = True)) #1

print(click2(), clickR1(consulta = True), clickR2(), clickR2(consulta = True)) #6

clickR1()
clickR1()
clickR1()

print(clickR1(consulta=True)) #4
clickR1(reset=0) #print el mensaje
print(clickR1(consulta=True)) # 0
print(clickR1())# 0
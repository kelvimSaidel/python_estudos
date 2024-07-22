hora = input('Digite a hora: \n')

try:
 hora = float(hora)
 if  hora >23.0 or hora < 0.0:
    print("Hora invalida");
 elif hora >0.0 and hora < 12.0:
    print("Bom dia")
 elif hora>= 13.0 and hora<= 18.0:
    print("Boa tarde")
    #elif hora> 6.0 and hora<= 0.0:
 else:
   print("Boa noite")

except:
   print("Hora invalida")

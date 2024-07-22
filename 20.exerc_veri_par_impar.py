numero = input('Digite um numero inteiro: \n')

try:
 numero = int(numero)
except:
   print("Número invalido")

if numero%2==0:
    print("Par")
else:
    print("Impar")
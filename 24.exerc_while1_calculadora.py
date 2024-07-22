valor = 0

print('*Calculadora*')
while True:
 
   print('1 - Soma(+):')
   print('2 - Subtração(-):')
   print('3 - Multiplicação(*):')
   print('4 - Divisão(/):')
   try:
      operacao = input('Digite a operação: \n')
      if operacao not in ('1','2','3','4'):
          print('---------------------')
          print("Operacao inválida");
          print('---------------------')
      else:
         primeiroN = input('Digite o primeiro numero: \n')
         segundoN = input('Digite o segundo numero: \n')
         primeiroN = int(primeiroN)
         segundoN = int(segundoN)

         if operacao == '1':
            valor = primeiroN + segundoN
         elif operacao == '2':
            valor = primeiroN - segundoN
         elif operacao == '3':
            valor = primeiroN * segundoN
         elif operacao == '4':
            valor = primeiroN // segundoN
         print('---------------------')
         
         print(f'Resultado: {valor}')
            
         print('---------------------')
   except:
    print("O valor digitado não é um numero")


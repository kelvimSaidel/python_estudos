import os

palavra_secreta = 'abcd'
tentativas =0;
qtd_letras = len(palavra_secreta)
# qtd_asterisco = (len(palavra_secreta))*'*'
asterisco= [] 
palavra_de_verificao= [] 
novo_asterisco = ''

    
for k in range(qtd_letras):
  asterisco.append('*')
  palavra_de_verificao.append(palavra_secreta[k])

print(f"Adivinha a palavra secreta com {qtd_letras} letras")
while True:
  print(f"Palavra secreta: {novo_asterisco.join(asterisco)}")
  letra = input("Digite a letra: \n").lower()
  if len(letra) > 1:
     print("Só é permitido digitar uma letra por vez")
     continue

  # print(palavra_de_verificao)
  # print(asterisco)
  l = 0
  verifica_alteracao = None
  for i in (palavra_de_verificao):
      #  print(i,l)
       if letra == i:
           asterisco[l] = i
           i = ''
           verifica_alteracao = True
       l =l+1  
   
  if verifica_alteracao is None:
   print(f"Palavra secreta: {novo_asterisco.join(asterisco)}")
   print('Não existe essa letra na palavra. Tente de novo')
     
  if novo_asterisco.join(asterisco) == palavra_secreta:
     print(f"Palavra secreta: {novo_asterisco.join(asterisco) }")
     print('Parabéns você terminou o jogo')
     break
   
  tentativas += 1;
  print(f"Tentativas: {tentativas}")
  os.system("cls")  #limpa o terminal


# asterisco = 'XXX'
# letra = 'b'
# palavra_secreta = 'abc'
# asterisco = asterisco.replace('X','Z',1)       
# print(letra,palavra_secreta.find(letra),asterisco,len(asterisco))
# asterisco = asterisco.replace('X',letra, 1)  
# print(letra,palavra_secreta.find(letra)==0,palavra_secreta.find(letra),asterisco)

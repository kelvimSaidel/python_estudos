
try:
   nome = input('Digite o seu nome: \n')
   nome = int(nome)
   print("Nome inválido");

except:
   i = 0;
   nome_com_separadores = '';
   while i<=len(nome)-1:
      # print(nome[i],i,len(nome)-1)
      if i != len(nome)-1:
         nome_com_separadores += nome[i]+'*'
      else :
         nome_com_separadores += nome[i]
      i+=1;
   print(nome_com_separadores)
  

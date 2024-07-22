lista_a = ["1","2","3"]; # definimos a lista a
print("--apontando o valor de uma lista para outra--")
lista_b =lista_a; # pensamos que copiamos a lista para lista b
lista_a[0] = "7" ; # então alteramos um valor na lista a
print(lista_a); # e printamos a lista a e b achando que retornara "1","2","3"
print(lista_b); 
# mas não retorna, invés disso retorna "7","2","3" isso porque a lista b
# só aponta para lista A então qualquer alteração que fizer em qualquer ponto
# do código na lista a irá alterar a lista b mesmo que essa alteração esteja
# sendo feita muito depois de definimos a lista a
# se quisermos copiar lista a para a lista b e não apontar devemos fazer o
#seguinte
print("--copiando o valor de uma lista para outra--")
lista_b = lista_a.copy();
lista_a[0] = "8" ; 
print(lista_b);
print(lista_a);

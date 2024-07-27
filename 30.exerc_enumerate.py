lista = ['maria','joao','carlos']

## tipos enumerados podem colocar indices nas lista
## pode também desacoplar no for como no exemplo abaixo
## invés de... criar uma variavel pra colocar o enumerate
## e variaveis pra colocar os itens desacoplados
## podemos simplesmente fazer tudo no for
for indice, nome in enumerate(lista): 
     print("%s indice e %s" % (indice,nome))
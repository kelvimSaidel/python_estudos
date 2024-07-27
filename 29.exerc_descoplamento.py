## pode fazer um split de uma lista direto em variaveis
# como abaixo
lista = ["maria","Helena","Luiz"]
nome1, nome2, nome3 = lista
print(f"{nome1} {nome2} {nome3}")

##
nome1, nome2, nome3 = ["Joao","Carlos","André"]
print(f"{nome1} {nome2} {nome3}")

## Pode também retirar só um item da lista e colocar o
# resto em outra lista chama..."resto ou qualquer coisa"
nome1,*resto = lista
format = "nome {}  e lista {}"
print(format.format(nome1,resto))

## mas normalmente é utilizado o _ para resto, somente
# é dado nome quando vai ser utilizado em outra parte 
# do codigo
resto,nome2, *_ = lista
format = "antes do nome 2 {a} nome {b} depois nome2 {c}"
print(format.format(a=resto,b=nome2,c=_))



tupla = 'teste','10','30' ## um pouco mais rapida que
## os vetores porém imutavel, não pode alterar
## e nao tem método
print(tupla[1])
#pode transformar uma tupla em uma lista
tupla = list(tupla)
print(tupla)
#pode transformar uma lista em uma tupla
tupla = tuple(tupla)
print(tupla)
#conchetes [] significa lista () parenteses tupla
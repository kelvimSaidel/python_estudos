nome = 'Kelvim silva saidel {a}, {b}, {c:.2f}'
altura = 1.80
peso = 95
imc = 95/(1.80 **2)

format = nome.format(a= altura,b=peso,c=imc)

print(format);

nome = 'Kelvim silva saidel {}, {}, {:.2f}'
altura = 1.80
peso = 95
imc = 95/(1.80 **2)

format = nome.format(altura,peso,imc)

print(format);


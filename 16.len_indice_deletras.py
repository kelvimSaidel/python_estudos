nome = input("Digite seu nome: \n")
idade = input("Digite sua idade: \n")


if nome and idade:
    print(f" Seu nome invertido é {nome[-1::-1]}")
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços') 
    print(f"seu nome tem {len(nome)} letras")
    print(f"a primeira letra do seu nome é {nome[0]}")
    print(f"a ultima letra do seu nome é {nome[-1]}")
else:
    print("Desculpe, mas você deixou os campos vazios");

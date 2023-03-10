# Estrutura do Try
# try = tudo que tiver abaixo do try, é oque será executado
# except =quando der algum erro no try, irá cair no except
# else = Quando nao der erro no try, irá executar oque está no else
# finally = Será executado independente se der erro ou nao


def soma(a, b):
    try:
        resultado = a+b

        if resultado == 10:
            print("Parabens")
    except exception as err:
        print('ERRO - ' + str(err))
    else:
        print(resultado)


soma(5, 5)

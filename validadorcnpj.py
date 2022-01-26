def conversor(cnpj):

    cnpj_sem_ponto = ''

    for caractere in cnpj:
        if caractere == '.' or caractere == '-' or caractere == '/':
            pass
        else:
            cnpj_sem_ponto += caractere

    cnpj_convertido = cnpj_sem_ponto[:12]
    return cnpj_convertido


def cnpj_sem_ponto(cnpj):
    cnpj_sem_ponto = ''

    for caractere in cnpj:
        if caractere == '.' or caractere == '-' or caractere == '/':
            pass
        else:
            cnpj_sem_ponto += caractere

    return cnpj_sem_ponto


def primeiro_digito(cnpj):
    multiplicador_5 = 5
    multiplicador_9 = 9
    soma = 0

    for caractere in cnpj:

        numero = int(caractere)

        if multiplicador_5 <= 1:
            soma += multiplicador_9 * numero
            multiplicador_9 -= 1

        else:
            soma += multiplicador_5 * numero
            multiplicador_5 -= 1

    digito = 11 - (soma % 11)
    digito_str = str(digito)

    if digito > 9:
        return cnpj + '0'
    else:
        return cnpj + digito_str


def segundo_digito (cnpj):
    multiplicador_6 = 6
    multiplicador_9 = 9
    soma2 = 0

    for caractere in cnpj:

        numero = int(caractere)

        if multiplicador_6 <= 1:
            soma2 += multiplicador_9 * numero
            multiplicador_9 -= 1

        else:
            soma2 += multiplicador_6 * numero
            multiplicador_6 -= 1

    digito2 = 11 - (soma2 % 11)
    digito2_str = str(digito2)

    if digito2 > 9:
        return cnpj + '0'
    else:
        return cnpj + digito2


cnpj = '04.252.011/0001-10'

a = cnpj_sem_ponto(cnpj)
x = conversor(cnpj)
y = primeiro_digito(x)
z = segundo_digito(y)

if z == a:
    print("CNPJ válido")
else:
    print("CNPJ inválido")

print(a)
print(z)

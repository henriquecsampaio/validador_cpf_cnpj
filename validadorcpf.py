#recebe o CPF do usuário:

while True:
    cpf = str(input("Por favor digite seu CPF (com '.' e '-'): "))
    if cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
        break
    else:
        print("Por favor digite um CPF válido! Se atentou aos '.' e '-'?")
        continue

# converte o cpf para ser usado nas operações
cpf_sem_ponto = ''

for caractere in cpf:
    if caractere == '.' or caractere == '-':
        pass
    else:
        cpf_sem_ponto += caractere

cpf_convertido = cpf_sem_ponto[:9]

print(cpf_convertido)


# verifica o 1º dígito
multiplicador_regressivo = 10

soma = 0

for caractere in cpf_convertido:
    numero = int(caractere)
    multiplicacao = numero * multiplicador_regressivo
    soma += multiplicacao
    multiplicador_regressivo -= 1

print(soma)

operacao_1 = 11 - (soma % 11)
digito_1 = operacao_1 if operacao_1 < 9 else 0
print(digito_1)

#verifica o digito 2
multiplicador_regressivo = 11

soma2 = 0

for caractere in cpf_convertido:
    numero = int(caractere)
    multiplicacao = numero * multiplicador_regressivo
    soma2 += multiplicacao
    multiplicador_regressivo -= 1

print(soma2)

digito_2 = 11 - (soma2 % 11)
print(digito_2)

# dá o resultado
digito_1 = str(digito_1)
digito_2 = str(digito_2)

if digito_1 == cpf[-2] and digito_2 == cpf[-1]:
    print("Seu cpf é válido")
else:
    print("Seu cpf é inválido!")

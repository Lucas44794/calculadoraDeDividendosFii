Codigo = str(input('Código da ação: '))
valorAtual = float(input('Valor atual da ação: '))
aporte = float(input('Digite o valor aportado mensalmente: R$'))
temp = int(input('Por quanto tempo o aporte será efetuado em anos? '))
tempo = temp * 12
mediaDividendo = float(input('Qual a Média dos ultimos 10 dividendos distribuidos? R$'))
reinvestimentoDividendo = str(input('Haverá o reinvestimento de dividendos? [S/N]: ')).strip().upper()[0]
while reinvestimentoDividendo not in 'SsNn':
    print('Resposta incorreta, tente novamente...')
    reinvestimentoDividendo = str(input('Haverá o reinvestimento de dividendos? [S/N]: ')).strip().upper()[0]
mes = total = dividendoTotal = totalAcoes = acoes = Saldo = 0
print()
print()
print()
while True:



    acoes = int(aporte / valorAtual)
    Saldo += aporte % valorAtual
    total += aporte
    if mes != 0:
        dividendoTotal = mediaDividendo * totalAcoes
        dividendoTotal += Saldo
        Saldo = 0
    print(f'No mês {mes + 1} você ganhará {dividendoTotal:.2f} em dividendo.')

    totalAcoes += acoes

    if reinvestimentoDividendo in 'Ss':
        if dividendoTotal >= valorAtual:
            acoesCompradasComDividendo = int(dividendoTotal / valorAtual)
            print(f'No mês {mes + 1} foram adquiridas {acoesCompradasComDividendo} ações compradas usando o dividendo.')
            Saldo += dividendoTotal % valorAtual
            totalAcoes += acoesCompradasComDividendo
        elif dividendoTotal < valorAtual:
            Saldo += dividendoTotal
        print(f'Total de ações: {totalAcoes}')
        print()

        if mes == tempo:
            print(
                f'O valor total que as ações valem com o reinvestimento dos dividendos é: {float(totalAcoes * valorAtual):.2f}')
        mes += 1
    elif reinvestimentoDividendo in 'Nn:':
        print(f'Total de ações: {totalAcoes}')
        print()
        mes += 1

    if mes >= tempo:
        print(f'Foram adquiridas {totalAcoes} ações, total aportado foi {total:.2f}\n  ')
        print(f'Saldo restante {Saldo:.2f}')
        break
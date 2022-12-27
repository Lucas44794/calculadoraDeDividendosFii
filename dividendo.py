Codigo = str(input('Código da ação: ')).strip().upper()
vv = str(input('Valor atual da ação: ')).replace(',', '.')
valorAtual = float(vv)
aapt = str(input('Digite o valor aportado mensalmente: R$')).replace(',', '.')
aporte = float(aapt)
temp = int(input('Por quanto tempo o aporte será efetuado em anos? '))
tempo = temp * 12
dd = str(input('Qual a Média dos ultimos 10 dividendos distribuidos? R$')).replace(',', '.')
mediaDividendo = float(dd)
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
        if mes >= tempo:
            print('-=' * 50)
            print(f'{" " * espaco}{Codigo}{" " * espaco}')
            print('-=' * 50)
            print(f'=>   Foram adquiridas {totalAcoes} ações  ')
            print(f'=>   O total aportado foi {total:.2f}')
            print(f'=>   Saldo restante {Saldo:.2f}')
            print(f'=>   O valor total que as ações valem com o reinvestimento dos dividendos é: {float(totalAcoes * valorAtual):.2f}')
            break

        mes += 1
    elif reinvestimentoDividendo in 'Nn:':

        print(f'Total de ações: {totalAcoes}')
        print()
        mes += 1
        if mes >= tempo:
            print('-=' * 50)
            print(f'{" " * espaco}{Codigo}{" " * espaco}')
            print('-=' * 50)
            print(f'=>   Foram adquiridas {totalAcoes} ações  ')
            print(f'=>   O total aportado foi {total:.2f}')
            print(f'=>   Saldo restante {Saldo:.2f}')
    espaco = int((100 - len(Codigo)) / 2)

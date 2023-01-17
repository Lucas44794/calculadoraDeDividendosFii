import urllib.request
import requests
from bs4 import BeautifulSoup
from lxml import html

Codigo = str(input('Código da ação: ')).strip().upper()

while True:
    urlErro = f"https://www.google.com/finance/quote/{Codigo}:BVMF"
    paginaErro = requests.get(urlErro)
    erroGeral = html.fromstring(paginaErro.content)
    erro = erroGeral.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[4]/div/div/div[2]/text()')
    erro = str(erro).replace('["','').replace('"]','')
    erro = str(erro).strip()
    if erro == "We couldn't find any match for your search.":
        Codigo = str(input('Código da ação: ')).strip().upper()
    else:
        break

url2 = f"https://www.google.com/finance/quote/{Codigo}:BVMF"
url = url2
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'lxml')
list_item = soup.find('div', attrs={'class': 'YMlKec fxKbKc'})
ap = str(list_item).replace('<div class="YMlKec fxKbKc">R$', '')
ar = str(ap).replace('</div>', '')
vv = str(ar).replace(',', '.')
valorAtual = float(vv)

aapt = str(input('Digite o valor aportado mensalmente: R$')).replace(',', '.')
aporte = float(aapt)
temp = int(input('Por quanto tempo o aporte será efetuado em anos? '))
tempo = temp * 12

ulr3 = f"https://www.fundsexplorer.com.br/funds/{Codigo}"
url4 = ulr3
page2 = requests.get(url4)
site2 = html.fromstring(page2.content)
precoDividendo12mesestxt = site2.xpath('//*[@id="dividends"]/div/div/div[2]/div[1]/div/div[2]/table/tbody/tr[1]/td[5]/text()')
precoDividendo12mesestxt = str(precoDividendo12mesestxt).replace('R$', '').replace(',', '.').replace('[', '').replace(']', '').replace("'",'')
precoDividendo12mesestxt = str(precoDividendo12mesestxt).strip()
precoDividendo12meses = float(precoDividendo12mesestxt)


mediaDividendo = precoDividendo12meses / 12
reinvestimentoDividendo = str(input('Haverá o reinvestimento de dividendos? [S/N]: ')).strip().upper()[0]
while reinvestimentoDividendo not in 'SsNn':
    print('Resposta incorreta, tente novamente...')
    reinvestimentoDividendo = str(input('Haverá o reinvestimento de dividendos? [S/N]: ')).strip().upper()[0]
while True:
    visualizar = str(input('Deseja ver os calculos mensalmente? [S/N]: ')).strip().upper()[0]
    if visualizar in 'SN':
        break
total = dividendoTotal = totalAcoes = acoes = Saldo = 0
mes = 1
print('\n \n \n')

while True:
    acoes = int(aporte / valorAtual)
    Saldo += aporte % valorAtual
    total += aporte
    if mes != 1:
        dividendoTotal = mediaDividendo * totalAcoes
        dividendoTotal += Saldo
        Saldo = 0
    if visualizar == 'S':
       print(f'No mês {mes} você ganhará {dividendoTotal:.2f} em dividendo.')

    totalAcoes += acoes

    if reinvestimentoDividendo in 'Ss':
        if dividendoTotal >= valorAtual:
            acoesCompradasComDividendo = int(dividendoTotal / valorAtual)
            if visualizar == 'S':
                print(f'Com o valor aportado, foram adquiridas {int(aporte / valorAtual)} ações.')
                print(f'Foram adquiridas {acoesCompradasComDividendo} ações compradas usando o dividendo.')
            Saldo += dividendoTotal % valorAtual
            totalAcoes += acoesCompradasComDividendo
        elif dividendoTotal < valorAtual:
            Saldo += dividendoTotal
        if visualizar in 'S':
            print(f'Total de ações: {totalAcoes}')
            print()
        if mes >= tempo:
            print('-=' * 50)
            print(f'{" " * espaco}{Codigo}{" " * espaco}')
            print('-=' * 50)
            print(f'=>   Foram adquiridas {totalAcoes} ações  ')
            print(f'=>   O total aportado foi {total:.2f}')
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
            break
    espaco = int((100 - len(Codigo)) / 2)

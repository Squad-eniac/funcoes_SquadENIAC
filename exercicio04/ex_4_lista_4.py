'''Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
Dólar Americano: R$ 4,91
Peso Argentino: R$ 0,02
Dólar Australiano: R$ 3,18
Dólar Canadense: R$ 3,64
Franco Suiço: R$ 0,42
Euro: R$ 5,36
Libra esterlina: R$ 6,21'''


moedas = {
    'Dólares Americanos': 4.91,
    'Pesos Argentinos': 0.02,
    'Dólares Australianos': 3.18,
    'Dólares Canadenses': 3.64,
    'Francos Suiços': 0.42,
    'Euros': 5.36,
    'Libras esterlinas': 6.21
}

def converter_moeda_estrangeira(valorNaCarteira):
    for nomeMoeda, conversaoMoeda in moedas.items():
        print(f'- {valorNaCarteira / conversaoMoeda:.2f}  {nomeMoeda}')


print('--- Conversor de moedas estrangeiras ---')
try:
    valorNaCarteira = float(input('\nPor favor, digite o quanto dinheiro você tem na sua carteira: R$ '))
except ValueError:
    print('Erro, a entrada digitada é inválida! Digite um número')
else:
    print(f'Com R$ {valorNaCarteira:.2f} você pode comprar:')
    converter_moeda_estrangeira(valorNaCarteira)

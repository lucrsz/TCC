import pandas as pd
import matplotlib.pyplot as plt

#leitura do arquivo .csv
dados = pd.read_csv('simulado.csv')

#imprime a tabela

print(dados)

#cria o gráfico de barra agrupado

dados.plot.bar(x='Ponto', y=['PotenciaSimulada(-dbm)', 'PotenciaMedida(-dbm)'], stacked=True)

for i, row in enumerate(dados.iterrows()):
    _, data = row
    for j, value in enumerate(data[['PotenciaSimulada(-dbm)', 'PotenciaMedida(-dbm)']]):
        plt.text(i, value, str(value), ha='center', va='bottom')

plt.title('Potência simulada x Potência aferida em campo')

#imprime o gráfico

plt.show()

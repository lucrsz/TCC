import pandas as pd
import matplotlib.pyplot as plt

# leitura do arquivo .csv

dados = pd.read_csv('caminho.csv')

# imprime o arquivo .csv

print(dados)

# cria o gráfico de barras com a coluna X
plt.figure(figsize=(8, 6))
plt.bar(dados['ColunaX'], dados['ColunaY'])
plt.xlabel('Coluna X')
plt.ylabel('Coluna Y')
plt.title('Gráfico X')

# coloca os valores das barras
for i, v in enumerate(dados['ColunaY']):plt.text(i, v, str(v), ha='center', va='bottom')

plt.show()

# cria o gráfico de barras com a coluna Y
plt.figure(figsize=(8, 6))
plt.bar(dados['ColunaX'], dados['ColunaY'])
plt.xlabel('Coluna X')
plt.ylabel('Coluna Y')
plt.title('Gráfico Y')

# coloca os valores das barras
for i, v in enumerate(dados['ColunaY']):plt.text(i, v, str(v), ha='center', va='bottom')

#imprime o gráfico

plt.show()

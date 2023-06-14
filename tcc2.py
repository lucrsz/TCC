import pandas as pd

# leitura do arquivo .csv
dados = pd.read_csv('caminho.csv')

# calcula a média dos valores de uma coluna X
media = dados['colunaX'].mean()

# calcula a mediana dos valores de uma coluna X
mediana = dados['colunaX'].median()

# Calcular a moda dos valores de uma coluna x
moda = dados['colunaX'].mode()

# criar a tabela com os dados da média, mediana e moda
tabela = pd.DataFrame({'Resultado': ['Média', 'Mediana', 'Moda'],'Valor': [media, mediana, moda]})

# imprime o resultado
print(tabela)

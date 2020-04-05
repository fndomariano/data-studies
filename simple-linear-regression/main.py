#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.linear_model import LinearRegression

#importa a base
base = pd.read_csv('dataset.csv')
base.head()
nan_values = base.isna().sum()
base.describe()

#limpa os valores nulos
base = base.dropna()

#plota o gráfico para ver se os dados estao normalizados
    consumption = base.iloc[:, -1].values
    plt.hist(consumption)


#converte os valores
base['avg_temperature'] = base['avg_temperature'].str.replace(',', '.')
base['avg_temperature'] = base['avg_temperature'].astype(float)

base['min_temperature'] = base['min_temperature'].str.replace(',', '.')
base['min_temperature'] = base['min_temperature'].astype(float)

base['max_temperature'] = base['max_temperature'].str.replace(',', '.')
base['max_temperature'] = base['max_temperature'].astype(float)

base['min_temperature'] = base['min_temperature'].str.replace(',', '.')
base['min_temperature'] = base['min_temperature'].astype(float)

base['precipitation'] = base['precipitation'].str.replace(',', '.')
base['precipitation'] = base['precipitation'].astype(float)

base['is_weekend'] = base['is_weekend'].astype(bool)


#mapa de calor para ver a correlacao
sns.heatmap(base.corr(), annot=True)

# visualizando o grafico para ver a lineraidade
x = base['max_temperature'].values
x = x.reshape(-1, 1)
y = base['beer_consumption'].values
plt.scatter(x, y)
plt.xlabel('Maximum temperature')
plt.ylabel('Beer consumption')

#treino
model = LinearRegression()
model.fit(x, y)

#exibicao
plt.scatter(x, y)
plt.plot(x, model.predict(x), color='red')
plt.xlabel('Maximum temperature')
plt.ylabel('Beer consumption')

model.predict(38)
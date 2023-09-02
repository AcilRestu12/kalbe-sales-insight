# -*- coding: utf-8 -*-
"""Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19g1NLb07qwmyxPPIU8_jPn3R7sRRc3Te

## Import Library
"""

import math
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.preprocessing import MinMaxScaler
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf

"""## Data Understanding"""

# Read Dataset
df_customer = pd.read_csv('dataset/customer.csv', delimiter=';')
df_product = pd.read_csv('dataset/product.csv', delimiter=';')
df_store = pd.read_csv('dataset/store.csv', delimiter=';')
df_transaction = pd.read_csv('dataset/transaction.csv', delimiter=';')

# Menampilkan 5 data teratas dari data customer
df_customer.head()

# Menampilkan 5 data teratas dari data product
df_product.head()

# Menampilkan 5 data teratas dari data store
df_store.head()

# Menampilkan 5 data teratas dari data transaction
df_transaction.head()

# Melakukan data cleansing
df_customer['Income'] = df_customer['Income'].replace('[,]', '.', regex=True).astype('float')
df_store['Latitude'] = df_store['Latitude'].replace('[,]', '.', regex=True).astype('float')
df_store['Longitude'] = df_store['Longitude'].replace('[,]', '.', regex=True).astype('float')

# Mengubah format date
df_transaction['Date'] = pd.to_datetime(df_transaction['Date'], format="%d/%m/%Y")

# Merge Dataset
df_merge = pd.merge(df_transaction, df_customer, on=['CustomerID'])
df_merge = pd.merge(df_merge, df_product, on=['ProductID'])
df_merge = pd.merge(df_merge, df_store, on=['StoreID'])

# Menampilkan informasi attribut
df_merge.info()

# Mengecek missing value
print('Jumlah missing value untuk setiap kolom')
df_merge.isnull().sum()

# Mengecek data duplicate
duplicate_count = df_merge.duplicated().sum()
print(f"Jumlah data duplikat secara keseluruhan: {duplicate_count}")

# Menampilkan correlation matrix
df_merge.corr(numeric_only=True)

# Distribusi Jumlah Quantity
plt.figure(figsize=(10, 6))
sns.histplot(data=df_merge, x='Qty', bins=30, kde=True)
plt.title('Distribution of Daily Quantity')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.show()

# Menampilkan grafik total quantity per hari
plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Qty', data=df_merge.groupby('Date')['Qty'].sum().reset_index())
plt.title('Total Daily Quantity')
plt.xlabel('Date')
plt.ylabel('Total Quantity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Korelasi antara Quantity dengan Harga
plt.figure(figsize=(10, 6))
sns.lineplot(x='Qty', y='Price_x', data=df_merge)
plt.title('Correlation between Quantity and Price')
plt.xlabel('Quantity')
plt.ylabel('Price')
plt.show()

# Decompose Time Series
decomposition = seasonal_decompose(df_merge.groupby('Date')['Qty'].sum(), period=30)  # Misalnya, periode musiman 30 hari
fig = decomposition.plot()
fig.set_size_inches(12, 6)
plt.show()

"""## Data Preparation"""

# Menghilangkan missing value
df_merge = df_merge.dropna()

# Membuat data frame baru untuk time series
df = df_merge.groupby(['Date'])['Qty'].sum().reset_index()
df = df.set_index('Date')
df.sort_values('Date')

# Pisahkan data untuk pelatihan dan pengujian
train_size = int(0.7 * len(df))
train_data = df[:train_size]
test_data = df[train_size:]

"""## Modeling"""

# Test Augmented Dickey-Fuller untuk menguji data stasioner atau tidak
result = adfuller(df['Qty'])
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])        # p-value < 0.05 -> hipotesis nol diterima & deret ini dianggap stasioner => d = 0
print('Critical Values:')
for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))

# Plot ACF dan PACF
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
plot_acf(df['Qty'], lags=25, ax=ax1)
plot_pacf(df['Qty'], lags=25, ax=ax2)
plt.show()

# Inisialisasi model ARIMA
p, d, q = 4, 0, 4 # Ganti dengan nilai yang sesuai analisis data yang telah dilakukan
model = ARIMA(train_data, order=(p, d, q))

# Latih model SARIMAX
model = model.fit()

"""## Evaluation"""

# Lakukan prediksi pada data test
predictions = model.get_forecast(steps=len(test_data)).predicted_mean

# Membulatkan angka hasil prediksi
predictions.apply(lambda x: math.floor(x))

# Hitung Mean Squared Error
mse = mean_squared_error(test_data, predictions)

# Tampilkan hasil MSE
print(f"Mean Squared Error: {mse}")

# Menampilkan grafik hasil prediksi
plt.figure(figsize=(12, 6))
plt.plot(train_data['Qty'])
plt.plot(test_data['Qty'])
plt.plot(predictions, color='red')
plt.title('Hasil Prediksi')
plt.ylabel('Total Quantity')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
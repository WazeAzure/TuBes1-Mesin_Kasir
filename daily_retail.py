import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import datetime
from csv import writer

def save_data(arr, diskon, tot):
    with open('retails.csv', 'a', newline='') as f:
        write = writer(f)
        date = datetime.datetime.now()
        write.writerow([date , arr, diskon, tot])

def per_hour(date, df):

    df = df.loc[date]
    
    print(df)
    max = df['revenue'].max()
    min = df['revenue'].min()

    print("Penjualan hari ini terbesar adalah Rp{:,.1f}".format(max))
    print("Penjualan harian terkecil adalah Rp{:,.1f}".format(min))

    df = df.resample('H').sum()

    df['revenue'].plot(kind='bar')
    plt.title('Penjualan Per Jam')
    plt.show()

def per_day(df):
    df = df.groupby(['date']).sum()
    df = df.resample('D').sum()
    df.plot(kind='bar')
    plt.title('Penjualan per Hari')
    plt.show()

def per_week(df):
    df = df.resample('7D').sum()
    df.plot(kind='bar')
    plt.title('Penjualan per Minggu')
    plt.show()

def main():
    df = pd.read_csv('retails.csv')

    # Group by date
    temp = df
    print(df)
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index(['date'])
    df = df.sort_index()
    print(df.describe())
    print(df)

    per_hour("2022-10-28", df)
    per_day(df)
    per_week(df)

main()
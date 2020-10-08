import pandas as pd
import datetime
from datetime import datetime
from time import strptime
import calendar
from tkinter import *
import tkinter as tk
import os
import matplotlib.pyplot as plt


abbr_to_num = {name: num for num,
               name in enumerate(calendar.month_abbr) if num}


def parser(dataframe):
    dataframe = dataframe.rename(columns={'day/month': 'Date'})

    for i in range(dataframe.shape[0]):
        dataframe.Date[i] = dataframe.Date[i].replace('Jul', (str(
            abbr_to_num['Jul'])+'.2019')).replace('Aug', (str(abbr_to_num['Aug'])+'.2019'))
        dataframe.Time[i] = datetime.strptime(dataframe.Time[i], "%I:%M %p")
        dataframe.Time[i] = datetime.strftime(dataframe.Time[i], "%H:%M")

    dataframe = dataframe.set_index('Date')

    return dataframe


# print(dataframe)
# print(dataframe.columns)

def Graph_1(event):
    dataframe = pd.read_csv("C:/Users/38096/Desktop/data_lab1.csv", sep=';')
    dataframe = parser(dataframe)
    #print(dataframe)
    x = dataframe['Time']
    y = dataframe['Temperature']
    plt.plot(x, y, label='Temperature', color='red')
    plt.title("Temperature during day")
    plt.xlabel("Time", fontsize=15)
    plt.ylabel("Temperature", fontsize=15)
    plt.grid()
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.show()


def Graph_2(event):
    dataframe = pd.read_csv("C:/Users/38096/Desktop/data_lab1.csv", sep=';')
    dataframe = parser(dataframe)
    #print(dataframe)
    x = dataframe['Time']
    y = dataframe['Dew Point']
    plt.scatter(x, y, label='Dew Point', color='black')
    plt.title("Dew Point  during day")
    plt.xlabel("Time", fontsize=15)
    plt.ylabel("Dew Point", fontsize=15)
    plt.grid()
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.show()


def Graph_3(event):
    dataframe = pd.read_csv("C:/Users/38096/Desktop/data_lab1.csv", sep=';')
    dataframe = parser(dataframe)
    #print(dataframe)
    x = dataframe['Time']
    y = dataframe['Condition']
    plt.bar(x, y, label='Condition', color='blue')
    plt.title("Condition  during day")
    plt.xlabel("Time", fontsize=15)
    plt.ylabel("Condition", fontsize=15)
    plt.grid()
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.show()


def Graph_4(event):
    dataframe = pd.read_csv("C:/Users/38096/Desktop/data_lab1.csv", sep=';')
    dataframe = parser(dataframe)
    #print(dataframe)
    x = dataframe['Time']
    y = dataframe['Wind Speed']
    plt.bar(x, y, label='Wind Speed', color='green')
    #plt.scatter(x, y, label='Wind Speed', color='green')
    plt.title("Wind Speed  during day")
    plt.xlabel("Time", fontsize=15)
    plt.ylabel("Wind Speed", fontsize=15)
    plt.grid()
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.show()

def Graph_5(event):
    dataframe = pd.read_csv("C:/Users/38096/Desktop/data_lab1.csv", sep=';')
    dataframe = parser(dataframe)
    print(dataframe)
    humidity = dataframe.groupby('Humidity').size()
    humidity.plot(kind='pie', subplots=True, figsize=(8, 8))
    plt.title("Pie Chart of humidity")
    plt.ylabel("")
    plt.show()
    plt.show()
def Graph_6(event):
    dataframe = pd.read_csv("C:/Users/38096/Desktop/data_lab1.csv", sep=';')
    dataframe = parser(dataframe)
    #print(dataframe)
    x = dataframe['Time']
    y = dataframe['Wind']
    plt.scatter(x, y, label='Wind direction', color='green')
    plt.title("Wind direction during days")
    plt.xlabel("Time", fontsize=15)
    plt.ylabel("Wind", fontsize=15)
    plt.grid()
    plt.legend()
    plt.gcf().autofmt_xdate()
    plt.show()


def Clean(event):
    plt.close()


root = Tk()

root.title('Analysis')

panelFrame = Frame(root, height=60, bg='gray',width=300)
panelFrame1 = Frame(root, height=60, bg='light gray',width=300)
panelFrame2 = Frame(root, height=60, bg='gray',width=300)

panelFrame.pack(side='top', fill='x')
panelFrame1.pack(side='top', fill='x')
panelFrame2.pack(side='top', fill='x')

Graph_1_Btn = Button(panelFrame, text='Temperature')
Graph_2_Btn = Button(panelFrame, text='Dew point')
Clean_Btn1 = Button(panelFrame, text='Clean')

Graph_3_Btn = Button(panelFrame1, text='Condition')
Graph_4_Btn = Button(panelFrame1, text='Wind Speed')
Clean_Btn2 = Button(panelFrame1, text='Clean')

Graph_5_Btn = Button(panelFrame2, text='Humidity')
Graph_6_Btn = Button(panelFrame2, text='Wind')
Clean_Btn3 = Button(panelFrame2, text='Clean')

Graph_1_Btn.bind("<Button-1>", Graph_1)
Graph_2_Btn.bind("<Button-1>", Graph_2)
Clean_Btn1.bind("<Button-1>", Clean)
Graph_3_Btn.bind("<Button-1>", Graph_3)
Graph_4_Btn.bind("<Button-1>", Graph_4)
Clean_Btn2.bind("<Button-1>", Clean)
Graph_5_Btn.bind("<Button-1>", Graph_5)
Graph_6_Btn.bind("<Button-1>", Graph_6)
Clean_Btn3.bind("<Button-1>", Clean)


Graph_1_Btn.place(x=10, y=10, width=80, height=40)
Graph_2_Btn.place(x=100, y=10, width=70, height=40)
Clean_Btn1.place(x=180, y=10, width=50, height=40)

Graph_3_Btn.place(x=10, y=10, width=80, height=40)
Graph_4_Btn.place(x=100, y=10, width=90, height=40)
Clean_Btn2.place(x=200, y=10, width=50, height=40)

Graph_5_Btn.place(x=10, y=10, width=80, height=40)
Graph_6_Btn.place(x=100, y=10, width=90, height=40)
Clean_Btn3.place(x=200, y=10, width=50, height=40)


root.mainloop()

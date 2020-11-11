import tkinter as tk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt
import os
import geopandas as gpd


#url = 'https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_settlement_dynamics.csv'
#df = pd.read_csv(url, error_bad_lines=False)


def Clean(event):
    plt.close()


def callback(*args):
    labelTest.configure(text="The selected item is {}".format(district.get()))
    labelTest1.configure(text="The selected field is {}".format(field.get()))
    labelTest2.configure(text="The selected graph is {}".format(graph.get()))
    # print(format(district.get()))
    # print(format(field.get()))
    # print(format(graph.get()))


def geo_map(event):
    print("Map")
    url = 'https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_settlement_dynamics.csv'
    df = pd.read_csv(url, error_bad_lines=False)
    df = df.set_index('zvit_date')
    dist = format(district.get())
    fieldneeded = format(field.get())
    graphneeded = format(graph.get())
    print('District to analize: ', dist)
    print('Field taken: ', fieldneeded)
    print('Graph type: ', graphneeded)

    # print(df_dist)
    print('Sorting:')
    df = df.groupby(
        ['zvit_date', 'registration_area'], as_index=False).sum()
    # print(df_dist)
    ######################################
    Ukraine = gpd.read_file(
        'C:/Users/38096/Desktop/ukr_admbnda_adm1_q2_sspe_20171221.shp', encoding='utf-8')
    df_grouped = df.groupby(['registration_area'], as_index=False).sum()
    #print(df_grouped)
    #print(Ukraine.index)
    Ukraine = Ukraine.reindex([23,22,19,18,17,16,25,15,14,13,12,26,24,11,10,21,9,20,8,7,6,5,4,3,2,1,0])
    
    Ukraine['Shape_Leng'] = df_grouped[fieldneeded]
    print(Ukraine['Shape_Leng'])

    fig, ax = plt.subplots(1, 1)
    Ukraine.plot(column='Shape_Leng',ax=ax, legend=True)

    #
    #Ukraine.plot(column = 'adm1Clas',)
    plt.show()


def analize(event):
    url = 'https://raw.githubusercontent.com/VasiaPiven/covid19_ua/master/covid19_by_settlement_dynamics.csv'
    df = pd.read_csv(url, error_bad_lines=False)
    df = df.set_index('zvit_date')
    dist = format(district.get())
    fieldneeded = format(field.get())
    graphneeded = format(graph.get())
    print('District to analize: ', dist)
    print('Field taken: ', fieldneeded)
    print('Graph type: ', graphneeded)
    df_dist = df[df.registration_area.eq(dist)]
    print(df_dist)
    print('Sorting:')
    df_dist = df_dist.groupby(
        ['zvit_date', 'registration_area'], as_index=False).sum()
    print(df_dist)
    df_dist.to_excel(r'C:/Users/38096/Desktop/data.xlsx', index = False)

    if graphneeded == 'Histopram':
        print(df_dist.index)
        y = df_dist[fieldneeded]
        plt.hist(y, bins=30, label=fieldneeded, color='red')
        plt.title(fieldneeded + " histogram")
        plt.xlabel(fieldneeded, fontsize=15)
        plt.ylabel("Frequency", fontsize=15)
        plt.grid()
        plt.legend()
        plt.gcf().autofmt_xdate()
        plt.show()
    if graphneeded == 'Linear':
        x = df_dist.index
        y = df_dist[fieldneeded]
        plt.plot(x, y, label=fieldneeded, color='red')
        plt.title(fieldneeded + 'Linear')
        plt.xlabel("Date", fontsize=15)
        plt.ylabel(fieldneeded, fontsize=15)
        plt.grid()
        plt.legend()
        plt.gcf().autofmt_xdate()
        plt.show()
    if graphneeded == "Pie chart":
        a = df_dist[fieldneeded].value_counts()
        a.plot(kind='pie', subplots=True, figsize=(100, 80), autopct='%1.1f%%')
        ax = plt.gca()
        plt.legend(bbox_to_anchor=(1.1, 1.1), bbox_transform=ax.transAxes)
        plt.title("Pie Chart of ")
        plt.ylabel("")
        plt.show()
    if graphneeded == "Scatter":
        x = df_dist.index
        y = df_dist[fieldneeded]
        plt.scatter(x, y, label=fieldneeded, color='red')
        plt.title(fieldneeded + " scatter")
        plt.xlabel("Date", fontsize=15)
        plt.ylabel(fieldneeded, fontsize=15)
        plt.grid()
        plt.legend()
        plt.gcf().autofmt_xdate()
        plt.show()
    if graphneeded == "Bar":
        x = df_dist.index
        y = df_dist[fieldneeded]
        plt.bar(x, y, label=fieldneeded, color='red')
        plt.title(fieldneeded)
        plt.xlabel("Date", fontsize=15)
        plt.ylabel(fieldneeded, fontsize=15)
        plt.grid()
        plt.legend()
        plt.gcf().autofmt_xdate()
        plt.show()


DistrictList = [
    "Вінницька",
    "Волинська",
    "Дніпропетровська",
    "Донецька",
    "Житомирська",
    "Закарпатська",
    "Запорізька",
    "Івано-Франківська",
    "Київська",
    "Кіровоградська",
    "Луганська",
    "Львівська",
    "Миколаївська",
    "Одеська",
    "Полтавська",
    "Рівненська",
    "Сумська",
    "Тернопільська",
    "Харківська",
    "Херсонська",
    "Хмельницька",
    "Черкаська",
    "Чернівецька",
    "Чернігівська"
]

FieldList = [
    "new_susp",
    "new_confirm",
    "active_confirm",
    "new_death",
    "new_recover"
]

GraphList = [
    "Linear",
    "Histopram",
    "Pie chart",
    "Scatter",
    "Bar"
]

app = tk.Tk()

app.geometry('600x160')

district = tk.StringVar(app)
district.set(DistrictList[0])

field = tk.StringVar(app)
field.set(FieldList[0])

graph = tk.StringVar(app)
graph.set(GraphList[0])

opt = tk.OptionMenu(app, district, *DistrictList)
opt.config(width=200, font=('Helvetica', 12))
opt.pack(side="top")

opt1 = tk.OptionMenu(app, field, *FieldList)
opt1.config(width=400, font=('Helvetica', 12))
opt1.pack()

opt2 = tk.OptionMenu(app, graph, *GraphList)
opt2.config(width=400, font=('Helvetica', 12))
opt2.pack()


panelFrame = Frame(app, height=60, bg='gray', width=1000)
panelFrame.pack(side='top', fill='x')

Graph_Btn = Button(panelFrame, text='Build')
Map_Btn = Button(panelFrame, text='Show on map')
Clean_Btn1 = Button(panelFrame, text='Clean')


Graph_Btn.bind("<Button-1>", analize)
Map_Btn.bind("<Button-1>", geo_map)
Clean_Btn1.bind("<Button-1>", Clean)

Graph_Btn.place(x=10, y=10, width=250, height=40)
Map_Btn.place(x=300, y=10, width=100, height=40)
Clean_Btn1.place(x=500, y=10, width=50, height=40)


btn1 = tk.Button


labelTest = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest.pack(side="top")

labelTest1 = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest1.pack(side="top")

labelTest2 = tk.Label(text="", font=('Helvetica', 12), fg='red')
labelTest2.pack(side="top")


district.trace("w", callback)

field.trace("w", callback)

graph.trace("w", callback)

app.mainloop()

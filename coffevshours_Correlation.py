import numpy as np
import csv;
import plotly.express as px

def getDataSource(data_path):
    cups_coffee =[]
    sleep =[]

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            cups_coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return {"x" : cups_coffee, "y":sleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("correlation table: ", correlation)
    print("correlation : ", correlation[0,1])

def plotGraph(data_path):    
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Cups Of Coffee", y="Sleep in hours")
        fig.show()



def setup():
    data_path = "./cups of coffee vs hours of sleep.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotGraph(data_path)

setup()

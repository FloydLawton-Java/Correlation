import csv
import plotly.express as px
import numpy as np

"""
with open("C:/Users/v0788/Desktop/Python/cups of coffee vs hours of sleep.csv") as f:
    df=csv.DictReader(f)
    figure=px.scatter(df, x="week", y="Coffee in ml")
    figure.show() """

def getDataSource(dataPath):
    CupsofCoffee=[]
    HoursofSleep=[]
    with open(dataPath) as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            CupsofCoffee.append(float(row["Coffee in ml"]))
            HoursofSleep.append(float(row["sleep in hours"]))
    return {"x":CupsofCoffee, "y":HoursofSleep}
def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource["x"], dataSource["y"])
    print("Correlation b/w Cups of Coffee vs Sleeping Hours=\n-----", correlation[0, 1])
def setup():
    dataPath='C:/Users/v0788/Desktop/Python/Correlation/cups of coffee vs hours of sleep.csv'
    dataSource=getDataSource(dataPath)
    findCorrelation(dataSource)
setup()
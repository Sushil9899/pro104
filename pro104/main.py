import plotly.figure_factory as ff
import statistics 
import random
import pandas as pd
import csv




df = pd.read_csv("data.csv")
data =df["Height(Inches)"].tolist()

mean = statistics.mean(data)
mode = statistics.mode(data)
median = statistics.median(data)

print("mean is",mean)
print("mode is",mode)
print("median is",median)




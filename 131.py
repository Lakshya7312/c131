import csv
import pandas as pd

df = pd.read_csv(r"C:\Users\Lenovo\Desktop\Python Projects\Stardata.csv")

# kg = 1.989e+30
finaldata = df.dropna()
finaldata.isnull().sum()
finaldata
#print(finaldata)
#print(df)
finaldata
mass = finaldata["Mass"].tolist()
radius = finaldata["Radius"].tolist()

gravity = []

# print(radius)
def convertToSI(radius, mass):
    
    for i in range(0, len(radius)-1):
        radius[i] = radius[i] * 6.957e+8
        mass[i] = mass[i] * 1.989e+30

convertToSI(radius, mass)

def calculateGravity(radius, mass):
    # print(len(mass))
    G = 6.674e-11
    for i in range(0,len(mass)-1):
        try:
            print(radius[i])
            g = (mass[i] * G) / ((radius[i]) ** 2)
            gravity.append(g)
        except:
            pass
calculateGravity(radius, mass)

df["Gravity"] = gravity
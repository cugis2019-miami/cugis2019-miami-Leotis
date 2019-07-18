# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

print("hellow world")
print("2169" )
print("the division of 5/2 is", 5/2)
#create function to sum any two numbers
def plus(a,b,c):
    plus = a + b + c
    print(plus)
plus(2,3,4)

#create a function to find the area of a triangle
print(1/2*21*69)

box = 5
 # Greeting
def hello(name):
    print(name)
     
hello("leo")    




import math

dir (math)

math.pi

math.asin

math.isfinite

math.pow(69,21)


def cubicroot (a):
    cr = 18
    print("the cubicroot of the",a,"is,cr)
cubicroot(8)    
#math.pow




print("Please enter a variable")
x = 20
def cube(x):
cube = math.pow(x,(1/3))
print ("the cube root of",x"is",cube)

x=20



#diffrent kind on chocolates
def chocolate (m,d,w)   :
    chocolate (5,3,8)
m ="cadburymilk"
m = "cadburywhite"
m = "cadburydark"

print ("There are 5" ,m,"3",d,"8",W,"to share")

# dict data structure 
chocolate1 = {"milk":5}
chocolate2 = {"dark":3}
chocolate3 = {"white":8}



chocolate = {"milk",5,"dark",3,"white",8}

print (chocolate)
print ("the number of chocolates in the box")

chocolate = {"milk":5,"dark":3,"white":8}
print("the number of white cholate in the chocolte box is",
      chocolate["white"])



ages = {"steve":32,"lia":28,"vin":45,"katie":38}
gender = {"steve":"m","lia":"f","vin":"m","katie":"f"}



#panda 
import pandas

dir (pandas)

#data frames


chocolatedf = pandas.DataFrame(chocolatedata, index=["quantity"])#convert to colum
print(chocolatedf)


#list
chocolatedata = [chocolate] #covert dict to list
print(chocolatedata)

#dataframes from list
studentallinfo = [["steve",32,"male"],["lia",28,"female"],["vin",45,"male"] ,["katie",38,"female"]]
df = pandas.DataFrame(studentallinfo)
print(df)

df1 = pandas.DataFrame([studentallinfo])
print(df1)

df12 = pandas.DataFrame([studentallinfo], index=["age"])
print(df12)

df2 = pandas.DataFrame(studentallinfo, columns=["name","age","gender"])
print(df2)






dir(ploty)  from plotly.offlile impoert plot
importplotly.graph_objs as go

agename = go.bar(x=studentlistdf)["name"], y=studentlistdf["age"])

plot([agename])

studentlist = [["steve",32,"male"],["lia",28,"female"],["vin",45,"male"] ,["katie",38,"female"]]

print(studentlist)

studentlistdf = pd.DataFrame(studentlist, columns =["name","age","gender"],
                                 index = [1,2,3,4])

print(studentlistdf)


#aproch our data  
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])

plot([agename])


"""


import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go









df = pd.read_excel("GISdata.xlsx",sheet_name = "womenOccupation")

womenoccupation = go.Bar(x = df["occupation"], y=df["women"], 
                         marker ={"color":df["women"],"colorscale" :"Picnic"}
                         )
                         

plot([womenoccupation])

#fig = go.Figure(data=[womenoccupation])


titles = go.layout(title = "percentage of Women Employed by Occupation",
                   
                  xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Occupation",
                        )
                    ),

                  yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Percentage",)
                          )
                    )
fig = go.Figure(data=[womenoccupation], layout = titles)

plot(fig)
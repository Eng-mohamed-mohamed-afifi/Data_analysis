import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer
#----------------------------------------
#--------Store data as dataframe----------
#----------------------------------------
dataset=pd.read_csv("Wuzzuf_Jobs.csv")
dataset.describe()
#----------------------------------------
#--------Cleaning data-----------
#----------------------------------------
# dataset.sort_values("Title", inplace = True)
# dataset.drop_duplicates(subset ="Title",keep = "first", inplace = True)
#----------------------------------------
#--------Showing Company -----------
#----------------------------------------
print(">>>>>>>>>>popular Company >>>>>>>>>>>")
numOfjops=dataset['Company'].value_counts().head(5)
print(numOfjops)
labels=["Confidential","EGIC","Mishkat Nour","Expand Cart","Majorel Egypt"]
plt.pie(numOfjops,labels = labels)
plt.show()
#----------------------------------------
#--------most popular jops -----------
#----------------------------------------
print(">>>>>>>>>>popular jops >>>>>>>>>>>")
jops=dataset['Title'].value_counts().head(5)
print(jops)
plt.xlabel("jop_title")
plt.ylabel("NumberOfjop")
plt.title("most popular jop")
jopLabels=["Accountant","Sales","GraphicDesigner","Digital M","Sales Manager"]
plt.bar(jopLabels,jops)
plt.show()
#----------------------------------------
#--------most popular areas -----------
#----------------------------------------
areas=dataset['Location'].value_counts().head(5)
print(areas)
plt.xlabel("Location_Name")
plt.ylabel("NumberOfLocation")
plt.title("most popular location")
locLable=[" Cairo"," Maadi","New Cairo"," Nasr City","6th of October"]
plt.bar(locLable,areas)
plt.show()
#----------------------------------------
#--------most popular areas -----------
#----------------------------------------
skills=dataset['Skills'].value_counts().head(5)
print(">>>>>>>>>>popular skills >>>>>>>>>>>")
print(skills)
skillsLabel=["Corporate_Sales"," SAP"," Sales_Target","Finance","Property"]
plt.xlabel("skill")
plt.ylabel("NumberOskills")
plt.title("most popular skills")
plt.bar(skillsLabel,skills)
plt.show()

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
dataset.sort_values("Title", inplace = True)
dataset.drop_duplicates(keep = "first", inplace = True)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 7].values

imputer = SimpleImputer(missing_values = "", strategy = 'most_frequent')
imputer = imputer.fit(X[:, 0:7])
X[:, 0:7] = imputer.transform(X[:, 0:7])
#----------------------------------------
#--------Showing Company -----------
#----------------------------------------
print(">>>>>>>>>>popular Company >>>>>>>>>>>")
numOfjops=dataset['Company'].value_counts().head()
print(numOfjops)
labels=list(numOfjops.keys())
plt.pie(numOfjops,labels = labels)
plt.show()
#----------------------------------------
#--------most popular jops -----------
#----------------------------------------
print(">>>>>>>>>>popular jops >>>>>>>>>>>")
jops=dataset['Title'].value_counts().head()
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
areas=dataset['Location'].value_counts().head()
print(areas)
plt.xlabel("Location_Name")
plt.ylabel("NumberOfLocation")
plt.title("most popular location")
locLable=list(areas.keys())
plt.bar(locLable,areas)
plt.show()
#----------------------------------------
#--------most popular areas -----------
#----------------------------------------
skills=dataset['Skills'].value_counts().head()
print(">>>>>>>>>>popular skills >>>>>>>>>>>")
print(skills)
skillsLabel=list(skills.keys())
plt.xlabel("skill")
plt.ylabel("NumberOskills")
plt.title("most popular skills")
plt.bar(skillsLabel,skills)
plt.show()

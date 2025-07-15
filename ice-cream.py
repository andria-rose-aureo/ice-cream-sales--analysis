import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Day': ['Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday','Saturday', 'Sunday'],
    'Temperature(C)' : [30,32,28,33,31,35,29],
    'Ice Cream Sales': [200, 220, 180, 250,210,300,190]
}

df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(100, 6))
sns.barplot(x='Day', y='Ice Cream Sales', data=df )
plt.title('Ice Cream Sales per Day')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Ice Creams Sold')
plt.grid(True)
plt.show()


plt.figure(figsize=(8, 6))
sns.scatterplot(x='Temperature(C)', y='Ice Cream Sales', data=df , color ='red')
plt.title('Temperature vs. Ice Cream Sales')
plt.xlabel('Temperature (C)')
plt.ylabel('Ice Cream Sales')
plt.grid(True)
plt.show()

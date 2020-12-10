import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('menu.csv', sep=',')
print(df.groupby('Category')[['Calories','Cholesterol','Calories from Fat']].mean())
macdo=df.groupby('Category')[['Calories','Cholesterol','Calories from Fat']].mean()
macdo.plot()
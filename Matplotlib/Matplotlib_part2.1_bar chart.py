import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')

df = pd.read_excel('Gross_profit.xlsx', index_col=0)

##line and bar
#plt.bar(df.index, df['Revenue ($B)'], color='#5a7d9a', label='Revenue ($B)')
#plt.plot(df.index, df['Gross Profit ($B)'], color='#444444', label='Gross Profit ($B)')

##Double bar
#plt.bar(df.index, df['Revenue ($B)'], color='#5a7d9a', label='Revenue ($B)')
#plt.bar(df.index, df['Gross Profit ($B)'], color='#444444', label='Gross Profit ($B)')

x_indexs = np.arange(len(df.index))
width = 0.25

plt.bar(x_indexs-width, df['Revenue ($B)'], color='#5a7d9a',width = width, label='Revenue ($B)')
plt.bar(x_indexs, df['Gross Profit ($B)'], color='#444444',width = width, label='Gross Profit ($B)')

#Label
plt.xlabel("Year")
plt.ylabel("Revenue (USD Billions)")
plt.title("AMZN Revenue Trend")

plt.legend()

plt.xticks(ticks = x_indexs, labels = df.index)

plt.tight_layout()

plt.savefig('bar_part2.png')

plt.show()
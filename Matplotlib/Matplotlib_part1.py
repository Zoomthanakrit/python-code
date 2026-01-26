import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import lineStyles
from matplotlib.ticker import MaxNLocator

#list style
#print(plt.style.available)

plt.style.use('fivethirtyeight')
#plt.style.use('ggplot')
#plt.xkcd() == comic style

#Read data
df = pd.read_excel('Gross_profit.xlsx', index_col=0)

#Line syle and color
plt.plot(df.index, df['Revenue ($B)'], color='#5a7d9a', linestyle='--', marker='o', linewidth = 3, label='Revenue ($B)')
plt.plot(df.index, df['Gross Profit ($B)'], color='b', marker = 'o', linewidth = 5, label='Gross Profit ($B)')

#Label
plt.xlabel("Year")
plt.ylabel("Revenue (USD Billions)")
plt.title("Revenue Trend")

plt.legend()

#Make year to be int
ax = plt.gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.grid(True)
plt.tight_layout()

#Save picture
plt.savefig('plot.png')

plt.show()



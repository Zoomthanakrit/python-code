from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

#Appropriate for data group <5
# #data--------------------------------------------------
# slices = [60,40,30,30]
# label = ['sixty', 'forty','Extra1','Extra2']
# color = ['#008fd5','#fc4f30','#e5ae37', '#6d904f']

#data2
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.15,0]

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90, autopct='%1.1f%%',
        wedgeprops={'edgecolor':'black', 'linewidth':2})

plt.title('Slice of pie chart')
plt.tight_layout()
plt.savefig('pie_part3.png')
plt.show()
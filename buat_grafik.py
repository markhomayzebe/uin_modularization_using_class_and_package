import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

sizes = [15, 30, 45,  10] #100%

fig1, ax1 = plt.subplots() #grafik
ax1.pie(sizes, labels=labels, shadow=True)
plt.show()
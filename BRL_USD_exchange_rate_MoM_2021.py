from matplotlib import pyplot as plt

month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']

exchange_rate = [5.363, 5.421, 5.641, 5.565, 5.295, 5.024]

plt.plot(month, exchange_rate, color='grey', marker='o', linestyle='solid')

plt.title("BRL/USD exchange rate MoM 2021")

plt.ylabel("BRL")
plt.xlabel("Month")

plt.show()